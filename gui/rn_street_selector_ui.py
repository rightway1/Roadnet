# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_street_selector_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_streetSelectorDialog(object):
    def setupUi(self, streetSelectorDialog):
        streetSelectorDialog.setObjectName("streetSelectorDialog")
        streetSelectorDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        streetSelectorDialog.resize(320, 236)
        streetSelectorDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(streetSelectorDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okPushButton = QtWidgets.QPushButton(streetSelectorDialog)
        self.okPushButton.setObjectName("okPushButton")
        self.horizontalLayout.addWidget(self.okPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(streetSelectorDialog)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.esuLabel = QtWidgets.QLabel(streetSelectorDialog)
        self.esuLabel.setObjectName("esuLabel")
        self.gridLayout.addWidget(self.esuLabel, 0, 0, 1, 1)
        self.usrnTableWidget = QtWidgets.QTableWidget(streetSelectorDialog)
        self.usrnTableWidget.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.usrnTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked)
        self.usrnTableWidget.setAlternatingRowColors(True)
        self.usrnTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.usrnTableWidget.setWordWrap(False)
        self.usrnTableWidget.setObjectName("usrnTableWidget")
        self.usrnTableWidget.setColumnCount(3)
        self.usrnTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.usrnTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.usrnTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.usrnTableWidget.setHorizontalHeaderItem(2, item)
        self.usrnTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.usrnTableWidget.horizontalHeader().setStretchLastSection(True)
        self.usrnTableWidget.verticalHeader().setVisible(False)
        self.usrnTableWidget.verticalHeader().setDefaultSectionSize(30)
        self.usrnTableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.usrnTableWidget, 1, 0, 1, 1)

        self.retranslateUi(streetSelectorDialog)
        QtCore.QMetaObject.connectSlotsByName(streetSelectorDialog)

    def retranslateUi(self, streetSelectorDialog):
        _translate = QtCore.QCoreApplication.translate
        streetSelectorDialog.setWindowTitle(_translate("streetSelectorDialog", "Street Selector"))
        self.okPushButton.setText(_translate("streetSelectorDialog", "OK"))
        self.cancelPushButton.setText(_translate("streetSelectorDialog", "Cancel"))
        self.esuLabel.setText(_translate("streetSelectorDialog", "ESU:"))
        item = self.usrnTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("streetSelectorDialog", "USRN"))
        item = self.usrnTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("streetSelectorDialog", "Street Type"))
        item = self.usrnTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("streetSelectorDialog", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    streetSelectorDialog = QtWidgets.QDialog()
    ui = Ui_streetSelectorDialog()
    ui.setupUi(streetSelectorDialog)
    streetSelectorDialog.show()
    sys.exit(app.exec_())

