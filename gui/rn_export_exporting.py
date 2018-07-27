# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_export_exporting.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_exporteExporting(object):
    def setupUi(self, exporteExporting):
        exporteExporting.setObjectName("exporteExporting")
        exporteExporting.resize(195, 76)
        exporteExporting.setMinimumSize(QtCore.QSize(195, 76))
        exporteExporting.setMaximumSize(QtCore.QSize(195, 76))
        exporteExporting.setSizeIncrement(QtCore.QSize(195, 76))
        exporteExporting.setWindowTitle("")
        self.gridLayout = QtWidgets.QGridLayout(exporteExporting)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(exporteExporting)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.retranslateUi(exporteExporting)
        QtCore.QMetaObject.connectSlotsByName(exporteExporting)

    def retranslateUi(self, exporteExporting):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("exporteExporting", "Exporting..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exporteExporting = QtWidgets.QDialog()
    ui = Ui_exporteExporting()
    ui.setupUi(exporteExporting)
    exporteExporting.show()
    sys.exit(app.exec_())

