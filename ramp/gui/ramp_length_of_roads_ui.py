# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ramp_length_of_roads_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RampLengthOfRoadsDialog(object):
    def setupUi(self, RampLengthOfRoadsDialog):
        RampLengthOfRoadsDialog.setObjectName("RampLengthOfRoadsDialog")
        RampLengthOfRoadsDialog.resize(494, 727)
        RampLengthOfRoadsDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(RampLengthOfRoadsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(RampLengthOfRoadsDialog)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(RampLengthOfRoadsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(RampLengthOfRoadsDialog)
        self.buttonBox.accepted.connect(RampLengthOfRoadsDialog.accept)
        self.buttonBox.rejected.connect(RampLengthOfRoadsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RampLengthOfRoadsDialog)

    def retranslateUi(self, RampLengthOfRoadsDialog):
        _translate = QtCore.QCoreApplication.translate
        RampLengthOfRoadsDialog.setWindowTitle(_translate("RampLengthOfRoadsDialog", "RAMP - Length of Roads"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RampLengthOfRoadsDialog = QtWidgets.QDialog()
    ui = Ui_RampLengthOfRoadsDialog()
    ui.setupUi(RampLengthOfRoadsDialog)
    RampLengthOfRoadsDialog.show()
    sys.exit(app.exec_())

