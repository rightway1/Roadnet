# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_export_complete.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_exportComplete(object):
    def setupUi(self, exportComplete):
        exportComplete.setObjectName("exportComplete")
        exportComplete.resize(197, 82)
        exportComplete.setMinimumSize(QtCore.QSize(197, 82))
        exportComplete.setMaximumSize(QtCore.QSize(197, 82))
        exportComplete.setWindowTitle("")
        self.gridLayout = QtWidgets.QGridLayout(exportComplete)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(exportComplete)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelPushButton = QtWidgets.QPushButton(exportComplete)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(exportComplete)
        QtCore.QMetaObject.connectSlotsByName(exportComplete)

    def retranslateUi(self, exportComplete):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("exportComplete", "Export Complete "))
        self.cancelPushButton.setText(_translate("exportComplete", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exportComplete = QtWidgets.QDialog()
    ui = Ui_exportComplete()
    ui.setupUi(exportComplete)
    exportComplete.show()
    sys.exit(app.exec_())

