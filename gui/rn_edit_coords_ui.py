# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_edit_coords_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editCoordsDialog(object):
    def setupUi(self, editCoordsDialog):
        editCoordsDialog.setObjectName("editCoordsDialog")
        editCoordsDialog.setWindowModality(QtCore.Qt.WindowModal)
        editCoordsDialog.resize(277, 165)
        editCoordsDialog.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(editCoordsDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okPushButton = QtWidgets.QPushButton(editCoordsDialog)
        self.okPushButton.setObjectName("okPushButton")
        self.horizontalLayout.addWidget(self.okPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(editCoordsDialog)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.startPushButton = QtWidgets.QPushButton(editCoordsDialog)
        self.startPushButton.setCheckable(True)
        self.startPushButton.setObjectName("startPushButton")
        self.gridLayout.addWidget(self.startPushButton, 1, 0, 1, 1)
        self.startXLineEdit = QtWidgets.QLineEdit(editCoordsDialog)
        self.startXLineEdit.setMaxLength(10)
        self.startXLineEdit.setObjectName("startXLineEdit")
        self.gridLayout.addWidget(self.startXLineEdit, 1, 1, 1, 1)
        self.endPushButton = QtWidgets.QPushButton(editCoordsDialog)
        self.endPushButton.setCheckable(True)
        self.endPushButton.setObjectName("endPushButton")
        self.gridLayout.addWidget(self.endPushButton, 2, 0, 1, 1)
        self.endXLineEdit = QtWidgets.QLineEdit(editCoordsDialog)
        self.endXLineEdit.setMaxLength(10)
        self.endXLineEdit.setObjectName("endXLineEdit")
        self.gridLayout.addWidget(self.endXLineEdit, 2, 1, 1, 1)
        self.startYLineEdit = QtWidgets.QLineEdit(editCoordsDialog)
        self.startYLineEdit.setMaxLength(10)
        self.startYLineEdit.setObjectName("startYLineEdit")
        self.gridLayout.addWidget(self.startYLineEdit, 1, 2, 1, 1)
        self.endYLineEdit = QtWidgets.QLineEdit(editCoordsDialog)
        self.endYLineEdit.setMaxLength(10)
        self.endYLineEdit.setObjectName("endYLineEdit")
        self.gridLayout.addWidget(self.endYLineEdit, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(editCoordsDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(editCoordsDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.usrnLabel = QtWidgets.QLabel(editCoordsDialog)
        self.usrnLabel.setObjectName("usrnLabel")
        self.gridLayout_2.addWidget(self.usrnLabel, 0, 1, 1, 1)

        self.retranslateUi(editCoordsDialog)
        QtCore.QMetaObject.connectSlotsByName(editCoordsDialog)

    def retranslateUi(self, editCoordsDialog):
        _translate = QtCore.QCoreApplication.translate
        editCoordsDialog.setWindowTitle(_translate("editCoordsDialog", "Edit start/end coordinates"))
        self.okPushButton.setText(_translate("editCoordsDialog", "OK"))
        self.cancelPushButton.setText(_translate("editCoordsDialog", "Cancel"))
        self.startPushButton.setText(_translate("editCoordsDialog", "Start"))
        self.endPushButton.setText(_translate("editCoordsDialog", "End"))
        self.label_2.setText(_translate("editCoordsDialog", "X"))
        self.label_3.setText(_translate("editCoordsDialog", "Y"))
        self.usrnLabel.setText(_translate("editCoordsDialog", "USRN:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editCoordsDialog = QtWidgets.QDialog()
    ui = Ui_editCoordsDialog()
    ui.setupUi(editCoordsDialog)
    editCoordsDialog.show()
    sys.exit(app.exec_())

