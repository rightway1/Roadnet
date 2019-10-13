# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_admin_street_reports_alert_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_strtAdminAlert(object):
    def setupUi(self, strtAdminAlert):
        strtAdminAlert.setObjectName("strtAdminAlert")
        strtAdminAlert.resize(258, 81)
        self.gridLayout = QtWidgets.QGridLayout(strtAdminAlert)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(strtAdminAlert)
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
        self.cancelPushButton = QtWidgets.QPushButton(strtAdminAlert)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(strtAdminAlert)
        QtCore.QMetaObject.connectSlotsByName(strtAdminAlert)

    def retranslateUi(self, strtAdminAlert):
        _translate = QtCore.QCoreApplication.translate
        strtAdminAlert.setWindowTitle(_translate("strtAdminAlert", "Dialog"))
        self.label_2.setText(_translate("strtAdminAlert", "Please Select an Additional Table Code"))
        self.cancelPushButton.setText(_translate("strtAdminAlert", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    strtAdminAlert = QtWidgets.QDialog()
    ui = Ui_strtAdminAlert()
    ui.setupUi(strtAdminAlert)
    strtAdminAlert.show()
    sys.exit(app.exec_())
