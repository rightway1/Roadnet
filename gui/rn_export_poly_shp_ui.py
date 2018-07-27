# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_export_poly_shp_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_exportPolyShpDialog(object):
    def setupUi(self, exportPolyShpDialog):
        exportPolyShpDialog.setObjectName("exportPolyShpDialog")
        exportPolyShpDialog.resize(483, 115)
        exportPolyShpDialog.setMinimumSize(QtCore.QSize(0, 0))
        exportPolyShpDialog.setMaximumSize(QtCore.QSize(16777215, 193))
        self.gridLayout = QtWidgets.QGridLayout(exportPolyShpDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fileLabel = QtWidgets.QLabel(exportPolyShpDialog)
        self.fileLabel.setObjectName("fileLabel")
        self.horizontalLayout_2.addWidget(self.fileLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileLineEdit = QtWidgets.QLineEdit(exportPolyShpDialog)
        self.fileLineEdit.setObjectName("fileLineEdit")
        self.horizontalLayout.addWidget(self.fileLineEdit)
        self.selectFilePushButton = QtWidgets.QPushButton(exportPolyShpDialog)
        self.selectFilePushButton.setText("")
        self.selectFilePushButton.setObjectName("selectFilePushButton")
        self.horizontalLayout.addWidget(self.selectFilePushButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.publicRecordsCheckBox = QtWidgets.QCheckBox(exportPolyShpDialog)
        self.publicRecordsCheckBox.setObjectName("publicRecordsCheckBox")
        self.horizontalLayout_3.addWidget(self.publicRecordsCheckBox)
        self.unassignedPolyCheckBox = QtWidgets.QCheckBox(exportPolyShpDialog)
        self.unassignedPolyCheckBox.setObjectName("unassignedPolyCheckBox")
        self.horizontalLayout_3.addWidget(self.unassignedPolyCheckBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.okPushButton = QtWidgets.QPushButton(exportPolyShpDialog)
        self.okPushButton.setMaximumSize(QtCore.QSize(94, 16777215))
        self.okPushButton.setObjectName("okPushButton")
        self.horizontalLayout_3.addWidget(self.okPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(exportPolyShpDialog)
        self.cancelPushButton.setMaximumSize(QtCore.QSize(94, 16777215))
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_3.addWidget(self.cancelPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.retranslateUi(exportPolyShpDialog)
        QtCore.QMetaObject.connectSlotsByName(exportPolyShpDialog)

    def retranslateUi(self, exportPolyShpDialog):
        _translate = QtCore.QCoreApplication.translate
        exportPolyShpDialog.setWindowTitle(_translate("exportPolyShpDialog", "Export Maintenance Polygons to Shapefile"))
        self.fileLabel.setText(_translate("exportPolyShpDialog", "Export to"))
        self.publicRecordsCheckBox.setText(_translate("exportPolyShpDialog", "Public records only"))
        self.unassignedPolyCheckBox.setText(_translate("exportPolyShpDialog", "Include unassigned polygons"))
        self.okPushButton.setText(_translate("exportPolyShpDialog", "OK"))
        self.cancelPushButton.setText(_translate("exportPolyShpDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exportPolyShpDialog = QtWidgets.QDialog()
    ui = Ui_exportPolyShpDialog()
    ui.setupUi(exportPolyShpDialog)
    exportPolyShpDialog.show()
    sys.exit(app.exec_())

