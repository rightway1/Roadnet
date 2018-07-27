# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_quick_find_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_quickFindDialog(object):
    def setupUi(self, quickFindDialog):
        quickFindDialog.setObjectName("quickFindDialog")
        quickFindDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        quickFindDialog.resize(361, 66)
        quickFindDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(quickFindDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.usrnLabel = QtWidgets.QLabel(quickFindDialog)
        self.usrnLabel.setObjectName("usrnLabel")
        self.horizontalLayout.addWidget(self.usrnLabel)
        self.usrnLineEdit = QtWidgets.QLineEdit(quickFindDialog)
        self.usrnLineEdit.setObjectName("usrnLineEdit")
        self.horizontalLayout.addWidget(self.usrnLineEdit)
        self.goPushButton = QtWidgets.QPushButton(quickFindDialog)
        self.goPushButton.setObjectName("goPushButton")
        self.horizontalLayout.addWidget(self.goPushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(quickFindDialog)
        QtCore.QMetaObject.connectSlotsByName(quickFindDialog)

    def retranslateUi(self, quickFindDialog):
        _translate = QtCore.QCoreApplication.translate
        quickFindDialog.setWindowTitle(_translate("quickFindDialog", "Quick Find Record"))
        self.usrnLabel.setText(_translate("quickFindDialog", "Enter USRN:"))
        self.goPushButton.setText(_translate("quickFindDialog", "Go"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    quickFindDialog = QtWidgets.QDialog()
    ui = Ui_quickFindDialog()
    ui.setupUi(quickFindDialog)
    quickFindDialog.show()
    sys.exit(app.exec_())

