# -*- coding: utf-8 -*-

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtSql import QSqlQuery, QSqlTableModel
from qgis.PyQt.QtWidgets import QMessageBox
# from Roadnet.generic_functions import ipdb_breakpoint
from Roadnet import config

__author__ = 'Alessandro Cristofori'


class LsgLookUp:
    def __init__(self, iface, db, lsg_lu_dia):
        self.iface = iface
        self.db = db
        self.lsg_lu_dia = lsg_lu_dia
        self.tables = {0: "tlkpLOCALITY",
                       1: "tlkpTOWN",
                       2: "tlkpCOUNTY"}
        self.columns = {0: "loc_ref",
                        1: "town_ref",
                        2: "county_ref"}
        self.items_model = None
        self.set_data()
        self.model_navigation()
        self.item_value = None
        self.changes_made = False
        self.selection_handler()

    def model_navigation(self):
        """
        events handler for buttons in the form
        :return: object
        """
        self.lsg_lu_dia.ui.addButton.clicked.connect(self.add_lookup)
        self.lsg_lu_dia.ui.removeButton.clicked.connect(self.remove_lookup)
        self.lsg_lu_dia.ui.amendButton.clicked.connect(self.amend_lookup)
        self.lsg_lu_dia.ui.closeButton.clicked.connect(self.close_browser)
        self.lsg_lu_dia.ui.locRadioButton.pressed.connect(lambda: self.populate_list(0))
        self.lsg_lu_dia.ui.townRadioButton.pressed.connect(lambda: self.populate_list(1))
        self.lsg_lu_dia.ui.countyRadioButton.pressed.connect(lambda: self.populate_list(2))
        self.lsg_lu_dia.ui.itemsListView.pressed.connect(self.selection_handler)

    def close_browser(self):
        # close the dialog window
        if self.changes_made:
            changes_made_msg_box = QMessageBox(
                QMessageBox.Information, " ",
                "LSG lookup tables updated.\n\n"
                "Restart roadNet to populate menus with new values.",
                QMessageBox.Ok,
                None)
            changes_made_msg_box.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
            changes_made_msg_box.exec_()
        self.lsg_lu_dia.close()

    def set_data(self):
        # initialise the state of the form when opened
        self.lsg_lu_dia.ui.locRadioButton.setChecked(True)
        self.populate_list(0)

    def populate_list(self, table_id):
        """
        populate the list view on initialisation and when radio buttons are toggled
        :param table_id: the id passed from the radio button
        :return: void
        """
        self.lsg_lu_dia.ui.addLookupLineEdit.clear()
        self.items_model = QSqlTableModel(db=self.db)
        self.items_model.setTable(self.tables[table_id])
        self.items_model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.items_model.setSort(2, Qt.AscendingOrder)
        self.items_model.select()
        while self.items_model.canFetchMore():
            self.items_model.fetchMore()
        self.lsg_lu_dia.ui.itemsListView.setModel(self.items_model)
        self.lsg_lu_dia.ui.itemsListView.setModelColumn(2)

    def add_lookup(self):
        """
        get the max value each table model and increment of 1
        add a record to the database when the add button is pressed
        with the incremented value
        :return: void
        """
        ui = self.lsg_lu_dia.ui
        category = None
        if ui.locRadioButton.isChecked():
            category = 0
        elif ui.townRadioButton.isChecked():
            category = 1
        elif ui.countyRadioButton.isChecked():
            category = 2

        if category is None:
            return

        table = self.tables[category]
        ref_col = self.columns[category]
        new_item = ui.addLookupLineEdit.text().strip()
        if new_item == "":
            return

        # Avoid duplicate insertion on double click on 'Add' button
        selection_model = ui.itemsListView.selectionModel()
        if selection_model.selectedIndexes():
            current_item = selection_model.selectedIndexes()[0]
            current_item_text = str(current_item.data())
            if current_item_text == new_item:
                self._show_warning("Cannot add duplicate values")
                return

        # Avoid duplicate insertion by checking database
        sql_find_duplicates = """SELECT name FROM {}
                                 WHERE name IS '{}'""".format(table,
                                                              new_item)
        if config.DEBUG_MODE:
            print('DEBUG_MODE: find_duplicates: {}'.format(
                sql_find_duplicates))
        query = QSqlQuery(sql_find_duplicates, self.db)
        if query.first():  # False unless value already found in table
            self._show_warning("Cannot add duplicate values")
            return

        # Get ID for new item
        max_ref = self.get_max_value(ref_col, table)

        # Create the record to insert
        row_count = self.items_model.rowCount()
        new_record = self.items_model.record(row_count)
        new_record.setValue(1, max_ref + 1)
        new_record.setValue(2, new_item)
        new_record.setValue(3, str(""))
        self.items_model.insertRecord(row_count, new_record)
        if self.items_model.submitAll():  # True if successfully updated
            # clear the line input and selects the newly created value
            ui.addLookupLineEdit.clear()
            index = ui.itemsListView.model().createIndex(
                row_count, 2)
            ui.itemsListView.setCurrentIndex(index)
            self.changes_made = True
        else:
            self._show_warning("Error: {} ".format(self.items_model.lastError().text()))
            return

    def remove_lookup(self):
        """
        this function deletes selected items from the list view and db, only if
        the lookups are not used, in this case it prevents the removal
        displaying the list of the streets that use the lookup
        :return: void
        """
        # Setup
        ui = self.lsg_lu_dia.ui
        table = None
        ref_col = None
        if ui.locRadioButton.isChecked():
            table = self.tables[0]
            ref_col = self.columns[0]
        elif ui.townRadioButton.isChecked():
            table = self.tables[1]
            ref_col = self.columns[1]
        elif ui.countyRadioButton.isChecked():
            table = self.tables[2]
            ref_col = self.columns[2]

        # Get selected item
        item_text = ui.addLookupLineEdit.text()
        table_model = self.items_model
        selection_model = ui.itemsListView.selectionModel()
        selection_index = selection_model.selectedIndexes()
        if not selection_index:
            return
        # if the selected value is <none> fire an alert
        # (<none> cannot be either removed or modified)
        selection_index = selection_index[0]
        if item_text == "" and selection_index.row() == 0:
            self._show_warning("This item cannot be removed")
            return

        # Get list of USRNs attached to record; get item_ref first
        item_name = selection_index.data()
        sql_get_item_ref = """SELECT {0} AS 'item_ref' FROM {1}
                              WHERE name IS '{2}';""".format(ref_col, table, item_name)
        if config.DEBUG_MODE:
            print('DEBUG_MODE: sql_get_item_ref: {}'.format(sql_get_item_ref))

        query = QSqlQuery(sql_get_item_ref, self.db)
        query.first()
        item_ref = query.record().value('item_ref')  # Reference of item

        # then get USRN list.
        sql_get_usrns = """SELECT usrn FROM tblSTREET
                           WHERE {} = {}
                           AND currency_flag = 0""".format(ref_col, item_ref)
        query = QSqlQuery(sql_get_usrns, self.db)
        usrns = []
        # collects all street USRN where the item is used
        while query.next():
            usrns.append(str(query.value(0)))

        # Cannot delete a record with attached USRNs
        if len(usrns) > 0:
            # Create a message
            message = ("This item cannot be deleted because is used by the "
                       "following streets: \n")
            usrns_string = ', '.join(usrns[:20])
            if len(usrns) > 20:
                usrns_string += ' and more...'
            long_message = message + usrns_string
            # Display warning message in box, then exit
            self._show_warning(long_message)
            return

        # No attached records, so delete the row
        table_model.beginRemoveRows(selection_index.parent(),
                                    selection_index.row(),
                                    selection_index.row())
        table_model.removeRow(selection_index.row())
        table_model.endRemoveRows()
        ui.addLookupLineEdit.clear()

        # Check the delete was successful
        if table_model.submitAll():
            # selects the item above the removed one
            index = ui.itemsListView.model().createIndex(
                selection_index.row() - 1, 2)
            ui.itemsListView.setCurrentIndex(index)
            self.selection_handler()
            self.changes_made = True
        else:
            self._show_warning("Error: {}".format(table_model.lastError.text()))

    def amend_lookup(self):
        """
        change the value of existing lookup items
        :return: void
        """
        if self.lsg_lu_dia.ui.addLookupLineEdit.text() == "":
            return
        item_text = self.lsg_lu_dia.ui.addLookupLineEdit.text()
        table_model = self.items_model
        selection_model = self.lsg_lu_dia.ui.itemsListView.selectionModel()
        selection_index = selection_model.selectedIndexes()
        # if nothing is selects exit the function
        if not selection_index:
            return
        selection_index = selection_index[0]
        if item_text == "<none>":
            # if the selected value is <none> fire an alert
            self._show_warning("This item cannot be edited")
            return
        rows = table_model.rowCount()
        i = 1
        while rows > i:
            table_index = self.lsg_lu_dia.ui.itemsListView.model().createIndex(i, 2)
            i += 1
            if item_text == str(table_index.data()):
                self._show_warning("An item with this name already exists")
                return
        if table_model.setData(selection_index, item_text, Qt.EditRole):
            if table_model.submitAll():
                # change the value and selects that same value from the list
                self.lsg_lu_dia.ui.addLookupLineEdit.clear()
                index = self.lsg_lu_dia.ui.itemsListView.model().createIndex(selection_index.row(), 2)
                self.lsg_lu_dia.ui.itemsListView.setCurrentIndex(index)
                self.changes_made = True
            return
        else:
            self._show_warning("Error: {}".format(table_model.lastError.text()))
            return

    def selection_handler(self):
        # print all selected list items to the text box
        sel_model = self.lsg_lu_dia.ui.itemsListView.selectionModel()

        # if no selected items set read only
        if sel_model.hasSelection() is False:
            buttons_enabled = False
            self.lsg_lu_dia.ui.addLookupLineEdit.setText("")
        else:
            sel_item = sel_model.selectedIndexes()[0]
            item_text = str(sel_item.data())
            self.lsg_lu_dia.ui.addLookupLineEdit.setText(item_text)
            buttons_enabled = True

        self.lsg_lu_dia.ui.amendButton.setEnabled(buttons_enabled)
        self.lsg_lu_dia.ui.removeButton.setEnabled(buttons_enabled)

    def get_max_value(self, ref_col, table):
        # Get ID for new item
        sql_find_max_ref = """SELECT MAX({}) AS 'max_ref'
                                  FROM {};""".format(ref_col, table)
        if config.DEBUG_MODE:
            print('DEBUG_MODE: find_max_ref: {}'.format(
                sql_find_max_ref))

        query_max = QSqlQuery(sql_find_max_ref, self.db)
        query_max.first()

        max_ref = 0
        if query_max.isValid():
            if not query_max.isNull('max_ref'):
                max_ref = query_max.value('max_ref')

        # cleanup
        if query_max.isActive():
            query_max.clear()

        return max_ref

    @staticmethod
    def _show_warning(message):
        lookup_msg_box = QMessageBox(QMessageBox.Warning, " ",
                                     message,
                                     QMessageBox.Ok, None
                                     )
        lookup_msg_box.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        lookup_msg_box.exec_()
