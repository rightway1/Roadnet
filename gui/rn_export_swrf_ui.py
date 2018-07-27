# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_export_swrf_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_exportSWRF(object):
    def setupUi(self, exportSWRF):
        exportSWRF.setObjectName("exportSWRF")
        exportSWRF.resize(400, 128)
        exportSWRF.setMinimumSize(QtCore.QSize(276, 128))
        exportSWRF.setMaximumSize(QtCore.QSize(400, 128))
        self.gridLayout = QtWidgets.QGridLayout(exportSWRF)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(214, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.okPushButton = QtWidgets.QPushButton(exportSWRF)
        self.okPushButton.setObjectName("okPushButton")
        self.horizontalLayout_3.addWidget(self.okPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(exportSWRF)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_3.addWidget(self.cancelPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileLabel = QtWidgets.QLabel(exportSWRF)
        self.fileLabel.setObjectName("fileLabel")
        self.horizontalLayout.addWidget(self.fileLabel)
        self.fileLineEdit = QtWidgets.QLineEdit(exportSWRF)
        self.fileLineEdit.setObjectName("fileLineEdit")
        self.horizontalLayout.addWidget(self.fileLineEdit)
        self.openPushButton = QtWidgets.QPushButton(exportSWRF)
        self.openPushButton.setText("")
        self.openPushButton.setObjectName("openPushButton")
        self.horizontalLayout.addWidget(self.openPushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.closedStreetsCheckBox = QtWidgets.QCheckBox(exportSWRF)
        self.closedStreetsCheckBox.setObjectName("closedStreetsCheckBox")
        self.gridLayout.addWidget(self.closedStreetsCheckBox, 1, 0, 1, 1)

        self.retranslateUi(exportSWRF)
        QtCore.QMetaObject.connectSlotsByName(exportSWRF)

    def retranslateUi(self, exportSWRF):
        _translate = QtCore.QCoreApplication.translate
        exportSWRF.setWindowTitle(_translate("exportSWRF", "ASD Export"))
        self.okPushButton.setText(_translate("exportSWRF", "OK"))
        self.cancelPushButton.setText(_translate("exportSWRF", "Cancel"))
        self.fileLabel.setText(_translate("exportSWRF", "Export To STDF 1.0"))
        self.closedStreetsCheckBox.setText(_translate("exportSWRF", "Include Closed Streets"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exportSWRF = QtWidgets.QDialog()
    ui = Ui_exportSWRF()
    ui.setupUi(exportSWRF)
    exportSWRF.show()
    sys.exit(app.exec_())

