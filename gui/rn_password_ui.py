# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_password_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_chPasswordDlg(object):
    def setupUi(self, chPasswordDlg):
        chPasswordDlg.setObjectName("chPasswordDlg")
        chPasswordDlg.setWindowModality(QtCore.Qt.ApplicationModal)
        chPasswordDlg.resize(342, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chPasswordDlg.sizePolicy().hasHeightForWidth())
        chPasswordDlg.setSizePolicy(sizePolicy)
        chPasswordDlg.setMinimumSize(QtCore.QSize(342, 180))
        chPasswordDlg.setMaximumSize(QtCore.QSize(342, 180))
        chPasswordDlg.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(chPasswordDlg)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(chPasswordDlg)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.oldPwdLineEdit = QtWidgets.QLineEdit(chPasswordDlg)
        self.oldPwdLineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.oldPwdLineEdit.setObjectName("oldPwdLineEdit")
        self.horizontalLayout_3.addWidget(self.oldPwdLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(chPasswordDlg)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(37, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pwdLineEdit = QtWidgets.QLineEdit(chPasswordDlg)
        self.pwdLineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.pwdLineEdit.setObjectName("pwdLineEdit")
        self.horizontalLayout.addWidget(self.pwdLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(chPasswordDlg)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.confirmLineEdit = QtWidgets.QLineEdit(chPasswordDlg)
        self.confirmLineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.confirmLineEdit.setObjectName("confirmLineEdit")
        self.horizontalLayout_2.addWidget(self.confirmLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.okCancelButton = QtWidgets.QDialogButtonBox(chPasswordDlg)
        self.okCancelButton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okCancelButton.setObjectName("okCancelButton")
        self.gridLayout.addWidget(self.okCancelButton, 1, 0, 1, 1)

        self.retranslateUi(chPasswordDlg)
        QtCore.QMetaObject.connectSlotsByName(chPasswordDlg)

    def retranslateUi(self, chPasswordDlg):
        _translate = QtCore.QCoreApplication.translate
        chPasswordDlg.setWindowTitle(_translate("chPasswordDlg", "Quick Find Record"))
        self.label_3.setText(_translate("chPasswordDlg", "Current Password: "))
        self.label.setText(_translate("chPasswordDlg", "New Password: "))
        self.label_2.setText(_translate("chPasswordDlg", "Confirm New Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    chPasswordDlg = QtWidgets.QDialog()
    ui = Ui_chPasswordDlg()
    ui.setupUi(chPasswordDlg)
    chPasswordDlg.show()
    sys.exit(app.exec_())

