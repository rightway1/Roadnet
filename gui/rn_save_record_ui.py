# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_save_record_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddRecordDialog(object):
    def setupUi(self, AddRecordDialog):
        AddRecordDialog.setObjectName("AddRecordDialog")
        AddRecordDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AddRecordDialog.resize(257, 114)
        AddRecordDialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AddRecordDialog)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(AddRecordDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.savePushButton = QtWidgets.QPushButton(AddRecordDialog)
        self.savePushButton.setObjectName("savePushButton")
        self.horizontalLayout.addWidget(self.savePushButton)
        self.revertPushButton = QtWidgets.QPushButton(AddRecordDialog)
        self.revertPushButton.setObjectName("revertPushButton")
        self.horizontalLayout.addWidget(self.revertPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(AddRecordDialog)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(AddRecordDialog)
        QtCore.QMetaObject.connectSlotsByName(AddRecordDialog)

    def retranslateUi(self, AddRecordDialog):
        _translate = QtCore.QCoreApplication.translate
        AddRecordDialog.setWindowTitle(_translate("AddRecordDialog", "Save changes"))
        self.label.setText(_translate("AddRecordDialog", "Save changes to record?"))
        self.savePushButton.setText(_translate("AddRecordDialog", "Yes"))
        self.revertPushButton.setText(_translate("AddRecordDialog", "No"))
        self.cancelPushButton.setText(_translate("AddRecordDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddRecordDialog = QtWidgets.QDialog()
    ui = Ui_AddRecordDialog()
    ui.setupUi(AddRecordDialog)
    AddRecordDialog.show()
    sys.exit(app.exec_())

