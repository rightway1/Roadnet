# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        loginDialog.setObjectName("loginDialog")
        loginDialog.resize(285, 138)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginDialog.sizePolicy().hasHeightForWidth())
        loginDialog.setSizePolicy(sizePolicy)
        loginDialog.setMinimumSize(QtCore.QSize(285, 130))
        loginDialog.setMaximumSize(QtCore.QSize(500, 300))
        font = QtGui.QFont()
        font.setPointSize(9)
        loginDialog.setFont(font)
        self.gridLayout_2 = QtWidgets.QGridLayout(loginDialog)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(loginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(65, 0))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.usrLineEdit = QtWidgets.QLineEdit(loginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usrLineEdit.sizePolicy().hasHeightForWidth())
        self.usrLineEdit.setSizePolicy(sizePolicy)
        self.usrLineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.usrLineEdit.setMaximumSize(QtCore.QSize(400, 21))
        self.usrLineEdit.setText("")
        self.usrLineEdit.setObjectName("usrLineEdit")
        self.gridLayout.addWidget(self.usrLineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(loginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(65, 0))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pwdLineEdit = QtWidgets.QLineEdit(loginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwdLineEdit.sizePolicy().hasHeightForWidth())
        self.pwdLineEdit.setSizePolicy(sizePolicy)
        self.pwdLineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.pwdLineEdit.setMaximumSize(QtCore.QSize(400, 20))
        self.pwdLineEdit.setText("")
        self.pwdLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwdLineEdit.setObjectName("pwdLineEdit")
        self.gridLayout.addWidget(self.pwdLineEdit, 1, 1, 1, 1)
        self.okCancelButton = QtWidgets.QDialogButtonBox(loginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okCancelButton.sizePolicy().hasHeightForWidth())
        self.okCancelButton.setSizePolicy(sizePolicy)
        self.okCancelButton.setMinimumSize(QtCore.QSize(150, 40))
        self.okCancelButton.setMaximumSize(QtCore.QSize(195, 16777215))
        self.okCancelButton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okCancelButton.setObjectName("okCancelButton")
        self.gridLayout.addWidget(self.okCancelButton, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(loginDialog)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)

    def retranslateUi(self, loginDialog):
        _translate = QtCore.QCoreApplication.translate
        loginDialog.setWindowTitle(_translate("loginDialog", "Login"))
        self.label.setText(_translate("loginDialog", "Username:"))
        self.label_2.setText(_translate("loginDialog", "Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginDialog = QtWidgets.QDialog()
    ui = Ui_loginDialog()
    ui.setupUi(loginDialog)
    loginDialog.show()
    sys.exit(app.exec_())

