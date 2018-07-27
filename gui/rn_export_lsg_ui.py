# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_export_lsg_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_exportLsgDialog(object):
    def setupUi(self, exportLsgDialog):
        exportLsgDialog.setObjectName("exportLsgDialog")
        exportLsgDialog.resize(453, 193)
        exportLsgDialog.setMinimumSize(QtCore.QSize(0, 193))
        exportLsgDialog.setMaximumSize(QtCore.QSize(16777215, 193))
        self.gridLayout_3 = QtWidgets.QGridLayout(exportLsgDialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fileLabel = QtWidgets.QLabel(exportLsgDialog)
        self.fileLabel.setObjectName("fileLabel")
        self.horizontalLayout_2.addWidget(self.fileLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileLineEdit = QtWidgets.QLineEdit(exportLsgDialog)
        self.fileLineEdit.setObjectName("fileLineEdit")
        self.horizontalLayout.addWidget(self.fileLineEdit)
        self.openPushButton = QtWidgets.QPushButton(exportLsgDialog)
        self.openPushButton.setText("")
        self.openPushButton.setObjectName("openPushButton")
        self.horizontalLayout.addWidget(self.openPushButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(exportLsgDialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.dtf63RadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.dtf63RadioButton.setObjectName("dtf63RadioButton")
        self.gridLayout.addWidget(self.dtf63RadioButton, 0, 0, 1, 1)
        self.dtf71RadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.dtf71RadioButton.setObjectName("dtf71RadioButton")
        self.gridLayout.addWidget(self.dtf71RadioButton, 1, 0, 1, 1)
        self.sdtfRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.sdtfRadioButton.setChecked(True)
        self.sdtfRadioButton.setObjectName("sdtfRadioButton")
        self.gridLayout.addWidget(self.sdtfRadioButton, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.asdCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.asdCheckBox.setEnabled(False)
        self.asdCheckBox.setObjectName("asdCheckBox")
        self.gridLayout.addWidget(self.asdCheckBox, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 2)
        self.closedStreetsCheckBox = QtWidgets.QCheckBox(exportLsgDialog)
        self.closedStreetsCheckBox.setObjectName("closedStreetsCheckBox")
        self.gridLayout_3.addWidget(self.closedStreetsCheckBox, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.okPushButton = QtWidgets.QPushButton(exportLsgDialog)
        self.okPushButton.setMaximumSize(QtCore.QSize(94, 16777215))
        self.okPushButton.setObjectName("okPushButton")
        self.horizontalLayout_3.addWidget(self.okPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(exportLsgDialog)
        self.cancelPushButton.setMaximumSize(QtCore.QSize(94, 16777215))
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_3.addWidget(self.cancelPushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)

        self.retranslateUi(exportLsgDialog)
        QtCore.QMetaObject.connectSlotsByName(exportLsgDialog)

    def retranslateUi(self, exportLsgDialog):
        _translate = QtCore.QCoreApplication.translate
        exportLsgDialog.setWindowTitle(_translate("exportLsgDialog", "Export LSG"))
        self.fileLabel.setText(_translate("exportLsgDialog", "Export To"))
        self.dtf63RadioButton.setText(_translate("exportLsgDialog", "DTF 6.3"))
        self.dtf71RadioButton.setText(_translate("exportLsgDialog", "DTF 7.1"))
        self.sdtfRadioButton.setText(_translate("exportLsgDialog", "SDTF 1.0"))
        self.asdCheckBox.setText(_translate("exportLsgDialog", "Include ASD?"))
        self.closedStreetsCheckBox.setText(_translate("exportLsgDialog", "Include Closed Streets"))
        self.okPushButton.setText(_translate("exportLsgDialog", "OK"))
        self.cancelPushButton.setText(_translate("exportLsgDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exportLsgDialog = QtWidgets.QDialog()
    ui = Ui_exportLsgDialog()
    ui.setupUi(exportLsgDialog)
    exportLsgDialog.show()
    sys.exit(app.exec_())

