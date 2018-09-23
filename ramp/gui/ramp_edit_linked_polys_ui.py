# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ramp_edit_linked_polys_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editLinkedPolysDialog(object):
    def setupUi(self, editLinkedPolysDialog):
        editLinkedPolysDialog.setObjectName("editLinkedPolysDialog")
        editLinkedPolysDialog.setWindowModality(QtCore.Qt.WindowModal)
        editLinkedPolysDialog.resize(250, 267)
        editLinkedPolysDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(editLinkedPolysDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.linkedPolysLabel = QtWidgets.QLabel(editLinkedPolysDialog)
        self.linkedPolysLabel.setObjectName("linkedPolysLabel")
        self.gridLayout.addWidget(self.linkedPolysLabel, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(editLinkedPolysDialog)
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)
        self.linkedPolysListWidget = QtWidgets.QListWidget(editLinkedPolysDialog)
        self.linkedPolysListWidget.setObjectName("linkedPolysListWidget")
        self.gridLayout.addWidget(self.linkedPolysListWidget, 1, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(editLinkedPolysDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.retranslateUi(editLinkedPolysDialog)
        QtCore.QMetaObject.connectSlotsByName(editLinkedPolysDialog)

    def retranslateUi(self, editLinkedPolysDialog):
        _translate = QtCore.QCoreApplication.translate
        editLinkedPolysDialog.setWindowTitle(_translate("editLinkedPolysDialog", "Edit linked polygons"))
        self.linkedPolysLabel.setText(_translate("editLinkedPolysDialog", "Linked polygons:"))
        self.label.setText(_translate("editLinkedPolysDialog", "Modify the selection on the map canvas to link/unlink polygons."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editLinkedPolysDialog = QtWidgets.QDialog()
    ui = Ui_editLinkedPolysDialog()
    ui.setupUi(editLinkedPolysDialog)
    editLinkedPolysDialog.show()
    sys.exit(app.exec_())

