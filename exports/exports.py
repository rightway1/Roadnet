# -*- coding: utf-8 -*-
import csv
import datetime
import os
import re

from PyQt5.QtCore import QThread, QObject, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from Roadnet.exports.export_csv import ExportCSV
from Roadnet.exports.export_esu_lines import ExportESUShapes
from Roadnet.exports.export_lor import ExportListOfRoads
from Roadnet.exports.export_poly import ExportPolyShapes
from Roadnet.roadnet_dialog import ExportCompleteDia, ExportExporting
from Roadnet.admin.export_street_report import StreetReportsExport
from Roadnet import database
from Roadnet.config import AsdTableEnum
from Roadnet.generic_functions import ipdb_breakpoint


class ExportsThread(QThread):
    def __init__(self, params, db, dtf_format=None,
                 path=None, inc_asd=None, closed_streets=None):
        """
        QThread class handling the exports on a separate thread from the main interface
        :param params: dict of values from xml file
        :param db: object database connection
        :param dtf_format: string indication of the user selected format
        :param path: string location of the path to export the report
        :param inc_asd: bool inclusion/exclusion of ASD
        :param closed_streets: inclusion/exclusion of closed streets
        """
        QThread.__init__(self)
        self.dtf_format = dtf_format
        self.path = path
        self.inc_asd = inc_asd
        self.closed_streets = closed_streets
        self.db = db
        self.version_dictionary = {
            "dtf63": 6,
            "dtf71": 7,
            "sdtf": 75,
            "srwr": 75
        }
        self.file_extension = {
            "dtf63": "_01.csv",
            "dtf71": "_LG.csv",
            "sdtf": ["_E_01.csv", "_C_01.csv"],
            "srwr": "_G_01.csv"
        }
        self.code = database.get_from_gaz_metadata(db, "custodian_code")
        self.org = database.get_from_gaz_metadata(db, "owner")
        self.lang = params["Language"]
        self.signals = GeneralSignals()
        self.csv = None

    def run(self):
        """
        Main thread method called with the start method from the main thread.
        """
        now = datetime.datetime.now()
        now_formatted = now.strftime('%Y%m%d')
        version = self.version_dictionary[self.dtf_format]
        if self.dtf_format == 'sdtf':
            if self.inc_asd:
                file_extension = self.file_extension[self.dtf_format][0]
            else:
                file_extension = self.file_extension[self.dtf_format][1]
            csv_filename = os.path.join(self.path,
                                        "{}_{}{}".format(self.code,
                                                         now_formatted,
                                                         file_extension))
        elif self.dtf_format == 'srwr':
            file_extension = self.file_extension[self.dtf_format]
            csv_filename = os.path.join(self.path,
                                        "{}_{}{}".format(self.code,
                                                         now_formatted,
                                                         file_extension))

        else:
            file_extension = self.file_extension[self.dtf_format]
            csv_filename = os.path.join(self.path,
                                        "{}{}".format(self.code,
                                                      file_extension))
        try:
            csv_file = open(csv_filename, 'w', newline='')
            self.csv = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
            exp = ExportCSV(version, self.csv, self.inc_asd, self.closed_streets,
                            self.org, self.lang, self.code, self.db)
            self.signals.task_started.emit()
            if self.dtf_format != "srwr":
                exp.export_lsg_to_dtf()
                csv_file.close()
            else:
                exp.export_srwr()
                csv_file.close()

            # Remove extra quotes from output file to make SDTF compliant
            strip_extra_quotes_in_file(csv_filename)

            self.signals.task_finished.emit()
        except IOError:
            self.signals.file_is_already_open.emit(csv_filename)


def strip_extra_quotes_in_file(csv_filename):
    """
    Strip quotes from empty, number and date fields in the exported CSV file.
    The requirements of the SDTF format are that date fields e.g. 2016-10-21 are
    unquoted, even though they are text fields.

    :param csv_filename: str, path of exported csv file
    """
    # Read in data
    with open(csv_filename, 'r') as infile:
        original_rows = infile.readlines()

    # Write out modified version
    with open(csv_filename, 'w') as outfile:
        for row in original_rows:
            stripped_row = re.sub(r'("\d{4}-\d{2}-\d{2}"|"[\d.]*?")', remove_quotes, row)
            outfile.write(stripped_row)


def remove_quotes(match):
    """
    Remove quotes from regular expression match object.
    :param match: match object
    :return: str, match object text with quotes removed
    """
    return re.sub(r'"', '', match.group(0))


def warning_message(message):
    """
    Generic warning message box with custom message
    :param message: Description of warning
    """
    warning_msg_box = QMessageBox(QMessageBox.Warning, " ", message,
                                  QMessageBox.Ok, None)
    warning_msg_box.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
    warning_msg_box.exec_()


class GeneralSignals(QObject):
    """
    class handling all general signals
    used by the class export_to_srwr
    """
    task_started = pyqtSignal()
    task_finished = pyqtSignal()
    file_is_already_open = pyqtSignal(str)


class ExportDTF:
    """
    class handling exports to CSV of LSG list of roads
    :param iface [object]: Qgis user interface
    :param export_lsg_dk [object]: export options form
    :param params [dict]:  of parameters from xml file
    :param db [object]: database connection
    """

    def __init__(self, iface, export_lsg_dk, params, db):
        self.iface = iface
        self.export_lsg = export_lsg_dk
        self.params = params
        self.db = db
        self.app_root = os.path.dirname(os.path.dirname(__file__))
        self.open_image = QPixmap(os.path.join(self.app_root,
                                               "image",
                                               "folder_open_icon.png"))
        self.export_lsg.ui.openPushButton.setIcon(QIcon(self.open_image))
        self.export_lsg.ui.openPushButton.setToolTip("Select Folder")
        self.home_dir = os.path.expanduser('~')
        self.model_navigation()
        self.running = ExportExporting()
        self.complete = ExportCompleteDia()
        self.complete.ui.cancelPushButton.clicked.connect(self.complete.close)
        self.export_to_dtf = None

    def model_navigation(self):
        """
        function that handles all buttons behaviours
        :return: void
        """
        self.export_lsg.ui.cancelPushButton.clicked.connect(self.close_browser)
        self.export_lsg.ui.openPushButton.clicked.connect(self.select_file)
        self.export_lsg.ui.okPushButton.clicked.connect(self.submit_export)
        self.export_lsg.ui.asdCheckBox.setEnabled(True)
        self.export_lsg.ui.dtf63RadioButton.toggled.connect(self.disable_asd_checkbox)
        self.export_lsg.ui.dtf71RadioButton.toggled.connect(self.disable_asd_checkbox)
        self.export_lsg.ui.sdtfRadioButton.toggled.connect(self.enable_asd_checkbox)

    def enable_asd_checkbox(self):
        """
        enables asd check box when dtf63 format is selected
        :return: void
        """
        self.export_lsg.ui.asdCheckBox.setEnabled(True)

    def disable_asd_checkbox(self):
        """
        disables asd check box when dtf63 format is selected
        :return: void
        """
        self.export_lsg.ui.asdCheckBox.setChecked(False)
        self.export_lsg.ui.asdCheckBox.setEnabled(False)

    def close_browser(self):
        """
        closes dialog window
        :return: void
        """
        self.export_lsg.close()

    def select_file(self):
        """
        open the select file window
        :return: void
        """
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setDirectory(self.home_dir)
        self.export_lsg.ui.fileLineEdit.setText(dialog.getExistingDirectory())

    def submit_export(self):
        """
        function that handles the user export options from the user
        (inclusion of closed streets, format, export file path)
        and pass these parameters to the csv writer
        :return: void
        """
        path = self.export_lsg.ui.fileLineEdit.text()
        if not os.path.isdir(path):
            warning_message("A valid directory must be selected")
        else:
            inc_asd = self.export_lsg.ui.asdCheckBox.isChecked()
            closed_streets = self.export_lsg.ui.closedStreetsCheckBox.isChecked()
            self.export_to_dtf = ExportsThread(self.params, self.db, None, path, inc_asd, closed_streets)
            self.export_to_dtf.signals.task_started.connect(self.task_started)
            self.export_to_dtf.signals.task_finished.connect(self.task_finished)
            self.export_to_dtf.signals.file_is_already_open.connect(self.file_is_already_open_warning)
            self.export_lsg.close()
            if self.export_lsg.ui.dtf63RadioButton.isChecked() is True:
                self.export_to_dtf.dtf_format = "dtf63"
            elif self.export_lsg.ui.dtf71RadioButton.isChecked() is True:
                self.export_to_dtf.dtf_format = "dtf71"
            elif self.export_lsg.ui.sdtfRadioButton.isChecked() is True:
                self.export_to_dtf.dtf_format = "sdtf"
            self.export_to_dtf.start()

    def task_started(self):
        """
        pyqt slot for the task started signal, shows the export in progress window
        """
        self.running.show()

    def task_finished(self):
        """
        pyqt slot for the task finished signal, shows the export finished window
        """
        self.running.close()
        self.complete.show()

    def file_is_already_open_warning(self, csv_filename):
        """
        pyqt slot informing the users the file they are trying to export to is opened
        or used by another process
        :param csv_filename: the name of the open file
        :return:
        """
        warning_message("The file {} is already open (possibly in another application).  "
                        "Close the file and try again".format(csv_filename))
        self.export_lsg.open()


class ExportSRWR:
    """
    class that handles exports to SRWR
    :param iface [object]: QGIS interface
    :param export_srwr_dk [object]: export options dialog window
    :param params [dict]: parameters from xml file
    :param db [object]: database connection
    """

    def __init__(self, iface, export_srwr_dk, params, db):
        self.iface = iface
        self.export_srwr_dk = export_srwr_dk
        self.params = params
        self.db = db
        self.app_root = os.path.dirname(os.path.dirname(__file__))
        self.open_image = QPixmap(os.path.join(self.app_root,
                                               "image",
                                               "folder_open_icon.png"))
        self.export_srwr_dk.ui.openPushButton.setIcon(QIcon(self.open_image))
        self.export_srwr_dk.ui.openPushButton.setToolTip("Select Folder")
        self.csv = None
        self.complete = ExportCompleteDia()
        self.complete.ui.cancelPushButton.clicked.connect(self.complete.close)
        self.running = ExportExporting()
        self.model_navigation()
        self.home_dir = os.path.expanduser('~')
        self.export_to_srwr = None

    def model_navigation(self):
        """
        function that handles all buttons behaviours
        :return: void
        """
        self.export_srwr_dk.ui.cancelPushButton.clicked.connect(self.close_browser)
        self.export_srwr_dk.ui.openPushButton.clicked.connect(self.select_file)
        self.export_srwr_dk.ui.okPushButton.clicked.connect(self.submit_export)

    def close_browser(self):
        """
        close the dialog window
        :return:
        """
        self.export_srwr_dk.close()

    def select_file(self):
        """
        open the select file window
        :return:
        """
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setDirectory(self.home_dir)
        self.export_srwr_dk.ui.fileLineEdit.setText(dialog.getExistingDirectory())

    def submit_export(self):
        """
        Handles the user export options from the user (inclusion of closed streets, export file path) and pass these
        parameters to the csv writer.
        """
        export_path = self.export_srwr_dk.ui.fileLineEdit.text()
        if not os.path.isdir(export_path):
            warning_message("A valid directory must be selected")
        else:
            closed_streets = self.export_srwr_dk.ui.closedStreetsCheckBox.isChecked()
            self.export_to_srwr = ExportsThread(self.params, self.db, dtf_format="srwr", path=export_path,
                                                inc_asd=False, closed_streets=closed_streets)
            self.export_to_srwr.signals.task_started.connect(self.task_started)
            self.export_to_srwr.signals.task_finished.connect(self.task_finished)
            self.export_to_srwr.signals.file_is_already_open.connect(self.file_open_warning)
            self.export_srwr_dk.close()
            self.export_to_srwr.start()

    def task_started(self):
        """
        pyqt slot for the task started signal, shows the export in progress window
        """
        self.running.show()

    def task_finished(self):
        """
        pyqt slot for the task finished signal, shows the export finished window
        """
        self.running.close()
        self.complete.show()

    def file_open_warning(self, csv_filename):
        """
        pyqt slot informing the users the file they are trying to export to is opened
        or used by another process
        :param csv_filename : the name of the open file
        :return:
        """
        warning_message("The file {} is already open (possibly in another application).  "
                        "Close the file and try again".format(csv_filename))
        self.export_srwr_dk.open()


class ExportLOR:
    def __init__(self, iface, export_lor_dlg, db):
        """
        class that handles simple list of roads exports
        :param iface [object]: QGIS interface
        :param export_lor_dlg [object]: options export dialog window
        :param db [object]: database connection
        """
        self.iface = iface
        self.export_lor_dlg = export_lor_dlg
        self.db = db
        self.code = database.get_from_gaz_metadata(db, "custodian_code")
        self.app_root = os.path.dirname(os.path.dirname(__file__))
        self.open_image = QPixmap(os.path.join(self.app_root,
                                               "image",
                                               "folder_open_icon.png"))
        self.export_lor_dlg.ui.openPushButton.setIcon(QIcon(self.open_image))
        self.export_lor_dlg.ui.openPushButton.setToolTip("Select Folder")
        self.home_dir = os.path.expanduser('~')
        self.complete = ExportCompleteDia()
        self.complete.ui.cancelPushButton.clicked.connect(self.complete.close)
        self.model_navigation()
        self.export_lor_dlg.ui.publicRadioButton.setChecked(True)
        self.toggle_public_or_status(False)

    def model_navigation(self):
        """
        handles buttons behaviours
        :return: void
        """
        self.export_lor_dlg.ui.cancelPushButton.clicked.connect(self.close_browser)
        self.export_lor_dlg.ui.openPushButton.clicked.connect(self.select_file)
        self.export_lor_dlg.ui.okPushButton.clicked.connect(self.submit_export)
        self.export_lor_dlg.ui.publicRadioButton.pressed.connect(lambda: self.toggle_public_or_status(False))
        self.export_lor_dlg.ui.anyRadioButton.pressed.connect(lambda: self.toggle_public_or_status(True))

    def toggle_public_or_status(self, is_status):
        """
        Toggles checkboxes enabled/checked state between the status and public radio buttons.
        :param is_status: bool: True for status
        :return: void
        """
        # Enable/disable
        self.export_lor_dlg.ui.publicCheckBox.setEnabled(is_status)
        self.export_lor_dlg.ui.privateCheckBox.setEnabled(is_status)
        self.export_lor_dlg.ui.proPublicCheckBox.setEnabled(is_status)
        self.export_lor_dlg.ui.trunkCheckBox.setEnabled(is_status)
        # Set/unset check state
        self.export_lor_dlg.ui.publicCheckBox.setChecked(is_status)
        self.export_lor_dlg.ui.privateCheckBox.setChecked(is_status)
        self.export_lor_dlg.ui.proPublicCheckBox.setChecked(is_status)
        self.export_lor_dlg.ui.trunkCheckBox.setChecked(is_status)
        self.export_lor_dlg.ui.t3CheckBox.setChecked(is_status)
        self.export_lor_dlg.ui.t4CheckBox.setChecked(is_status)

    def close_browser(self):
        """
        close the dialog window
        :return: void
        """
        self.export_lor_dlg.close()

    def select_file(self):
        """
        opens the select file window
        :return: void
        """
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setDirectory(self.home_dir)
        self.export_lor_dlg.ui.fileLineEdit.setText(dialog.getExistingDirectory())

    def submit_export(self):
        """
        handles the export main work,
        getting the check box options
        """
        export_path = self.export_lor_dlg.ui.fileLineEdit.text()
        if not os.path.isdir(export_path):
            warning_message("A valid directory must be selected")
        else:
            export = ExportListOfRoads(
                    self.export_lor_dlg.ui.publicRadioButton.isChecked(),
                    self.export_lor_dlg.ui.anyRadioButton.isChecked(),
                    self.export_lor_dlg.ui.publicCheckBox.checkState(),
                    self.export_lor_dlg.ui.proPublicCheckBox.checkState(),
                    self.export_lor_dlg.ui.privateCheckBox.checkState(),
                    self.export_lor_dlg.ui.trunkCheckBox.checkState(),
                    self.export_lor_dlg.ui.t3CheckBox.checkState(),
                    self.export_lor_dlg.ui.t4CheckBox.checkState(),
                    self.export_lor_dlg.ui.lorNoCeckBox.checkState(),
                    self.export_lor_dlg.ui.usrnCheckBox.checkState(),
                    self.export_lor_dlg.ui.townCheckBox.checkState(),
                    self.export_lor_dlg.ui.csvCheckBox.checkState(),
                    export_path,
                    self.code,
                    self.db
            )
            lor_filename = export.export_lor()
            if lor_filename is None:
                self.export_lor_dlg.close()
                self.complete.show()
            else:
                warning_message("The file {} is already open (possibly in another application).  "
                                "Close the file and try again".format(lor_filename))
                self.export_lor_dlg.open()


class ExportLsgShp:
    def __init__(self, iface, export_lsg_shp_dlg, db, params):
        """
        class that handles the exports of the ESU shp layer
        :param iface [object]: QGIS interface
        :param export_poly_shp_dlg [object]: export options dialog window
        :param db [object]: database connection
        :param params [dict]: dictionary of parameters from xml file
        """
        self.iface = iface
        self.export_lsg_shp_dlg = export_lsg_shp_dlg
        self.export_lsg_shp_dlg.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.app_root = os.path.dirname(os.path.dirname(__file__))
        image = QPixmap(os.path.join(self.app_root,
                                     "image",
                                     "folder_open_icon.png"))
        self.export_lsg_shp_dlg.ui.selectFilePushButton.setIcon(QIcon(image))
        self.export_lsg_shp_dlg.ui.selectFilePushButton.setToolTip("Select Folder")
        self.db = db
        self.params = params
        self.connect_dialog_buttons()
        self.export_path = None
        self.complete = ExportCompleteDia()
        self.complete.ui.cancelPushButton.clicked.connect(self.complete.close)

    def connect_dialog_buttons(self):
        """
        handles buttons behaviours
        """
        self.export_lsg_shp_dlg.ui.cancelPushButton.clicked.connect(self.export_lsg_shp_dlg.close)
        self.export_lsg_shp_dlg.ui.okPushButton.clicked.connect(self.submit_export)
        self.export_lsg_shp_dlg.ui.selectFilePushButton.clicked.connect(self.set_export_path)

    def set_export_path(self):
        """
        Run the save file dialog to set the export path
        :return: void
        """
        dialog = QFileDialog()
        home_dir = os.path.expanduser('~')
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setDefaultSuffix(".shp")
        esu_file_path = os.path.join(home_dir, "esu.shp")
        self.export_path, save_extension = QFileDialog.getSaveFileName(dialog, "Export LSG ",
                                                                       esu_file_path,
                                                                       filter="ESRI Shapefile (*.shp *.)")
        self.export_lsg_shp_dlg.ui.fileLineEdit.setText(self.export_path)

    def submit_export(self):
        """
        runs the main export class
        """
        out_path = self.export_lsg_shp_dlg.ui.fileLineEdit.text()
        if self.check_path_exists(out_path):
            exp_unassigned = False
            if self.export_lsg_shp_dlg.ui.unassignedEsuCheckBox.isChecked():
                exp_unassigned = True
            self.export_lsg_shp_dlg.close()
            export = ExportESUShapes(self.iface, self.db, exp_unassigned, out_path)
            if export.export_esu_line():
                self.complete.show()
            else:
                self.export_lsg_shp_dlg.open()
                return
            del export

    @staticmethod
    def check_path_exists(file_path):
        """
        Tests if a file path is located in a valid directory
        :param file_path: string path to file
        :return: True if valid
        """
        if os.path.isdir(os.path.dirname(file_path)):
            return True
        else:
            warning_message("A valid location must be selected")
            return False


class ExportPoly:
    """
    Export Polygons. Note the logic behind the the menus.
    """

    def __init__(self, iface, export_poly_dlg, db):
        self.iface = iface
        self.db = db
        self.app_root = os.path.dirname(os.path.dirname(__file__))
        self.export_poly_shp_dlg = export_poly_dlg
        self.export_poly_shp_dlg.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        image = QPixmap(os.path.join(self.app_root,
                                     "image",
                                     "folder_open_icon.png"))
        self.export_poly_shp_dlg.ui.selectFilePushButton.setIcon(QIcon(image))
        self.export_poly_shp_dlg.ui.selectFilePushButton.setToolTip("Select Folder")
        self.connect_dialog_buttons()
        self.export_path = None
        self.complete = ExportCompleteDia()
        self.complete.ui.cancelPushButton.clicked.connect(self.complete.close)

    def connect_dialog_buttons(self):
        """
        Handles buttons behaviours
        :return: void
        """
        self.export_poly_shp_dlg.ui.cancelPushButton.clicked.connect(self.export_poly_shp_dlg.close)
        self.export_poly_shp_dlg.ui.okPushButton.clicked.connect(self.submit_export)
        self.export_poly_shp_dlg.ui.selectFilePushButton.clicked.connect(self.set_export_path)

    def set_export_path(self):
        """
        Run the save file dialog to set the export path
        :return: void
        """
        dialog = QFileDialog()
        home_dir = os.path.expanduser('~')
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setDefaultSuffix(".shp")
        esu_file_path = os.path.join(home_dir, "rdpoly.shp")
        self.export_path, save_extension = QFileDialog.getSaveFileName(dialog, "Export Maintenance Polygons ",
                                                                       esu_file_path,
                                                                       filter="ESRI Shapefile (*.shp *.)")
        self.export_poly_shp_dlg.ui.fileLineEdit.setText(self.export_path)

    def submit_export(self):
        """
        Run the export with the params pulled from the dialog checkboxes.
        :return: void
        """
        out_path = self.export_poly_shp_dlg.ui.fileLineEdit.text()
        if ExportLsgShp.check_path_exists(out_path):
            unassigned = False
            public_only = False
            if self.export_poly_shp_dlg.ui.publicRecordsCheckBox.isChecked():
                public_only = True
            if self.export_poly_shp_dlg.ui.unassignedPolyCheckBox.isChecked():
                unassigned = True
            self.export_poly_shp_dlg.close()
            export = ExportPolyShapes(self.iface, public_only, unassigned, out_path, self.db)
            if export.export_polys():
                self.complete.show()
            else:
                self.export_poly_shp_dlg.open()
                return
            del export


class ExportStreetReport:
    """
    Export Street Report from Admin menu.
    Works with rn_admin_street_reports
    """
    def __init__(self, iface, db, street_dia, params):
        self.iface = iface
        self.db = db
        self.street_dia = street_dia
        self.params = params
        self.export_path = None
        self.csv_chx = None
        self.report_options = None
        app_root = os.path.dirname(os.path.dirname(__file__))
        self.open_image = QPixmap(os.path.join(app_root,
                                               "image",
                                               "folder_open_icon.png"))
        self.home_dir = os.path.expanduser('~')
        self.street_dia.ui.fileOpenPushButton.setIcon(QIcon(self.open_image))
        self.street_dia.ui.fileOpenPushButton.setToolTip("Select File")
        self.model_navigation()

    def model_navigation(self):
        # handles events on widgets
        self.street_dia.ui.fileOpenPushButton.clicked.connect(self.select_file)

        self.street_dia.ui.cancelPushButton.clicked.connect(self.close_browser)
        self.street_dia.ui.okPushButton.clicked.connect(self.submit_export)
        self.street_dia.ui.changedStsRadioButton.pressed.connect(self.enable_streets)
        self.street_dia.ui.tblsRadioButton.pressed.connect(self.disable_streets)
        self.street_dia.ui.tblsComboBox.currentIndexChanged.connect(self.populate_list)

    def close_browser(self):
        # close the browser
        self.street_dia.close()

    def populate_list(self, current):
        """
        changes the content of the list widget according to the selected value
        in the combo box
        :param current: the current combo box index
        :return: void
        """
        # 0 = None,  1 = maintenance, 2 = reinstatement, 3 = special designation
        qry = {0: [],
               1: ['SELECT * from tlkpRoad_Status', 'Description', 'Road_Status_Ref'],
               2: ['SELECT * from tlkpREINS_CAT', 'Description', 'Reinstatement_Code'],
               3: ['SELECT designation_code,designation_text from tlkpSPEC_DES', 'Designation_Text', 'Designation_code']
               }
        # if the parameter is not null change the query accordingly
        if current != 0:
            query = QSqlQuery(self.db)
            query.exec_(qry.get(current)[0])
            rec = query.record()
            # aval are the names of the indexes columns
            aval = [rec.indexOf(qry.get(current)[1]), rec.indexOf(qry.get(current)[2])]
            self.street_dia.ui.listWidget.clear()
            while query.next():
                # adds values to widget list
                entry = str(query.value(aval[1])) + ": " + str(query.value(aval[0]))
                self.street_dia.ui.listWidget.addItem(entry)
            # Select the first item
            first_item = self.street_dia.ui.listWidget.item(0)
            first_item.setSelected(True)
        else:
            self.street_dia.ui.listWidget.clear()

    def select_file(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setDirectory(self.home_dir)
        save_file_path, save_extension = dialog.getSaveFileName(dialog, "Street Report",
                                                                os.path.join(self.home_dir, "RNStreetReport"))
        self.street_dia.ui.fileLineEdit.setText(save_file_path)

    def disable_streets(self):
        # disable the additional tables reporting option
        # and enable the diachronic reporting option
        self.street_dia.ui.dateEdit.setEnabled(False)
        self.street_dia.ui.tblsComboBox.setEnabled(True)
        self.street_dia.ui.listWidget.setEnabled(True)

    def enable_streets(self):
        # disable the diachronic reporting option
        # enable the additional tables reporting option
        self.street_dia.ui.listWidget.clear()
        self.street_dia.ui.tblsComboBox.setCurrentIndex(0)
        self.street_dia.ui.dateEdit.setEnabled(True)
        self.street_dia.ui.tblsComboBox.setEnabled(False)
        self.street_dia.ui.listWidget.setEnabled(False)

    def submit_export(self):
        """
        when the ok button is presses it runs the main export class,
        gets all data from widgets and instantiate a StreetReportsExport class
        :return:
        """
        self.export_path = self.street_dia.ui.fileLineEdit.text()
        if self.export_path is None or self.export_path == "":
            warning_message("You must select an export file path")
            return
        date = self.street_dia.ui.dateEdit.date().toPyDate()
        if date.year < 1997:
            warning_message("No records present before 01/01/1997")
            return
        if date > datetime.date.today():
            warning_message("Change Date not valid")
            return
        formatted_date = date.strftime("%Y%m%d")

        # dictionary containing another dictionary which keys are
        # the option of the report format (date or optional table)
        # and values are the values selected for each widget
        if self.street_dia.ui.changedStsRadioButton.isChecked():
            self.report_options = {"report": "streets", "change_date": formatted_date}
        else:
            self.report_options = {"report": "srwr",
                                   "categories": self.street_dia.ui.listWidget.selectedItems(),
                                   "table": self.street_dia.ui.tblsComboBox.currentIndex()
                                   }
        # optional CSV formatting option checkbox
        self.csv_chx = self.street_dia.ui.csvCheckBox.isChecked()
        # export class instantiation
        export = StreetReportsExport(self.db, self.export_path,
                                     self.report_options, self.csv_chx,
                                     self.street_dia, self.params)
        # run the export
        export.run_export()
