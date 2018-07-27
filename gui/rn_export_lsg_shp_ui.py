# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_export_lsg_shp_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_exportLsgShpDialog(object):
    def setupUi(self, exportLsgShpDialog):
        exportLsgShpDialog.setObjectName("exportLsgShpDialog")
        exportLsgShpDialog.resize(454, 115)
        exportLsgShpDialog.setMinimumSize(QtCore.QSize(0, 0))
        exportLsgShpDialog.setMaximumSize(QtCore.QSize(16777215, 193))
        self.gridLayout = QtWidgets.QGridLayout(exportLsgShpDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fileLabel = QtWidgets.QLabel(exportLsgShpDialog)
        self.fileLabel.setObjectName("fileLabel")
        self.horizontalLayout_2.addWidget(self.fileLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileLineEdit = QtWidgets.QLineEdit(exportLsgShpDialog)
        self.fileLineEdit.setObjectName("fileLineEdit")
        self.horizontalLayout.addWidget(self.fileLineEdit)
        self.selectFilePushButton = QtWidgets.QPushButton(exportLsgShpDialog)
        self.selectFilePushButton.setText("")
        self.selectFilePushButton.setObjectName("selectFilePushButton")
        self.horizontalLayout.addWidget(self.selectFilePushButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.unassignedEsuCheckBox = QtWidgets.QCheckBox(exportLsgShpDialog)
        self.unassignedEsuCheckBox.setObjectName("unassignedEsuCheckBox")
        self.horizontalLayout_3.addWidget(self.unassignedEsuCheckBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.okPushButton = QtWidgets.QPushButton(exportLsgShpDialog)
        self.okPushButton.setMaximumSize(QtCore.QSize(94, 16777215))
        self.okPushButton.setObjectName("okPushButton")
        self.horizontalLayout_3.addWidget(self.okPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(exportLsgShpDialog)
        self.cancelPushButton.setMaximumSize(QtCore.QSize(94, 16777215))
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_3.addWidget(self.cancelPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.retranslateUi(exportLsgShpDialog)
        QtCore.QMetaObject.connectSlotsByName(exportLsgShpDialog)

    def retranslateUi(self, exportLsgShpDialog):
        _translate = QtCore.QCoreApplication.translate
        exportLsgShpDialog.setWindowTitle(_translate("exportLsgShpDialog", "Export LSG to Shapefile"))
        self.fileLabel.setText(_translate("exportLsgShpDialog", "Export to"))
        self.unassignedEsuCheckBox.setText(_translate("exportLsgShpDialog", "Include unassigned ESU\'s"))
        self.okPushButton.setText(_translate("exportLsgShpDialog", "OK"))
        self.cancelPushButton.setText(_translate("exportLsgShpDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exportLsgShpDialog = QtWidgets.QDialog()
    ui = Ui_exportLsgShpDialog()
    ui.setupUi(exportLsgShpDialog)
    exportLsgShpDialog.show()
    sys.exit(app.exec_())

