# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_edit_esu_link_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editEsuLinkDialog(object):
    def setupUi(self, editEsuLinkDialog):
        editEsuLinkDialog.setObjectName("editEsuLinkDialog")
        editEsuLinkDialog.setWindowModality(QtCore.Qt.WindowModal)
        editEsuLinkDialog.resize(213, 267)
        editEsuLinkDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(editEsuLinkDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.usrnLabel = QtWidgets.QLabel(editEsuLinkDialog)
        self.usrnLabel.setObjectName("usrnLabel")
        self.gridLayout.addWidget(self.usrnLabel, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(editEsuLinkDialog)
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okPushButton = QtWidgets.QPushButton(editEsuLinkDialog)
        self.okPushButton.setObjectName("okPushButton")
        self.horizontalLayout.addWidget(self.okPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(editEsuLinkDialog)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.esuLinkListWidget = QtWidgets.QListWidget(editEsuLinkDialog)
        self.esuLinkListWidget.setObjectName("esuLinkListWidget")
        self.gridLayout.addWidget(self.esuLinkListWidget, 1, 0, 1, 2)

        self.retranslateUi(editEsuLinkDialog)
        QtCore.QMetaObject.connectSlotsByName(editEsuLinkDialog)

    def retranslateUi(self, editEsuLinkDialog):
        _translate = QtCore.QCoreApplication.translate
        editEsuLinkDialog.setWindowTitle(_translate("editEsuLinkDialog", "Edit ESU/Street Links"))
        self.usrnLabel.setText(_translate("editEsuLinkDialog", "USRN:"))
        self.label.setText(_translate("editEsuLinkDialog", "Modify the selection on the map canvas to add/remove ESU\'s."))
        self.okPushButton.setText(_translate("editEsuLinkDialog", "OK"))
        self.cancelPushButton.setText(_translate("editEsuLinkDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editEsuLinkDialog = QtWidgets.QDialog()
    ui = Ui_editEsuLinkDialog()
    ui.setupUi(editEsuLinkDialog)
    editEsuLinkDialog.show()
    sys.exit(app.exec_())

