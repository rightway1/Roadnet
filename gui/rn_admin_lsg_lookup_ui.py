# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_admin_lsg_lookup_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_lsgLookupDialog(object):
    def setupUi(self, lsgLookupDialog):
        lsgLookupDialog.setObjectName("lsgLookupDialog")
        lsgLookupDialog.resize(372, 295)
        self.gridLayout_2 = QtWidgets.QGridLayout(lsgLookupDialog)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonsGroupBox = QtWidgets.QGroupBox(lsgLookupDialog)
        self.buttonsGroupBox.setObjectName("buttonsGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttonsGroupBox)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.locRadioButton = QtWidgets.QRadioButton(self.buttonsGroupBox)
        self.locRadioButton.setObjectName("locRadioButton")
        self.horizontalLayout.addWidget(self.locRadioButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.townRadioButton = QtWidgets.QRadioButton(self.buttonsGroupBox)
        self.townRadioButton.setObjectName("townRadioButton")
        self.horizontalLayout.addWidget(self.townRadioButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.countyRadioButton = QtWidgets.QRadioButton(self.buttonsGroupBox)
        self.countyRadioButton.setObjectName("countyRadioButton")
        self.horizontalLayout.addWidget(self.countyRadioButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout_2.addWidget(self.buttonsGroupBox, 0, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.itemsListView = QtWidgets.QListView(lsgLookupDialog)
        self.itemsListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.itemsListView.setProperty("showDropIndicator", True)
        self.itemsListView.setObjectName("itemsListView")
        self.gridLayout.addWidget(self.itemsListView, 1, 0, 1, 2)
        self.addLookupLineEdit = QtWidgets.QLineEdit(lsgLookupDialog)
        self.addLookupLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.addLookupLineEdit.setObjectName("addLookupLineEdit")
        self.gridLayout.addWidget(self.addLookupLineEdit, 0, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addButton = QtWidgets.QPushButton(lsgLookupDialog)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_2.addWidget(self.addButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.removeButton = QtWidgets.QPushButton(lsgLookupDialog)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout_2.addWidget(self.removeButton)
        self.amendButton = QtWidgets.QPushButton(lsgLookupDialog)
        self.amendButton.setObjectName("amendButton")
        self.verticalLayout_2.addWidget(self.amendButton)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.closeButton = QtWidgets.QPushButton(lsgLookupDialog)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout_2.addWidget(self.closeButton)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.retranslateUi(lsgLookupDialog)
        QtCore.QMetaObject.connectSlotsByName(lsgLookupDialog)

    def retranslateUi(self, lsgLookupDialog):
        _translate = QtCore.QCoreApplication.translate
        lsgLookupDialog.setWindowTitle(_translate("lsgLookupDialog", "Dialog"))
        self.buttonsGroupBox.setTitle(_translate("lsgLookupDialog", "Lookup Table:"))
        self.locRadioButton.setText(_translate("lsgLookupDialog", "Locality"))
        self.townRadioButton.setText(_translate("lsgLookupDialog", "Town"))
        self.countyRadioButton.setText(_translate("lsgLookupDialog", "County"))
        self.addButton.setText(_translate("lsgLookupDialog", "Add"))
        self.removeButton.setText(_translate("lsgLookupDialog", "Remove"))
        self.amendButton.setText(_translate("lsgLookupDialog", "Amend"))
        self.closeButton.setText(_translate("lsgLookupDialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    lsgLookupDialog = QtWidgets.QDialog()
    ui = Ui_lsgLookupDialog()
    ui.setupUi(lsgLookupDialog)
    lsgLookupDialog.show()
    sys.exit(app.exec_())

