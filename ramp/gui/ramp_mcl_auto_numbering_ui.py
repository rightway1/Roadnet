# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ramp_mcl_auto_numbering_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mclAutoNumberingDialog(object):
    def setupUi(self, mclAutoNumberingDialog):
        mclAutoNumberingDialog.setObjectName("mclAutoNumberingDialog")
        mclAutoNumberingDialog.setWindowModality(QtCore.Qt.WindowModal)
        mclAutoNumberingDialog.resize(332, 330)
        mclAutoNumberingDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(mclAutoNumberingDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(mclAutoNumberingDialog)
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.linkedPolysLabel = QtWidgets.QLabel(mclAutoNumberingDialog)
        self.linkedPolysLabel.setObjectName("linkedPolysLabel")
        self.verticalLayout.addWidget(self.linkedPolysLabel)
        self.mclListWidget = QtWidgets.QListWidget(mclAutoNumberingDialog)
        self.mclListWidget.setObjectName("mclListWidget")
        self.verticalLayout.addWidget(self.mclListWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 2, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.startValueSpinBox = QtWidgets.QSpinBox(mclAutoNumberingDialog)
        self.startValueSpinBox.setObjectName("startValueSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.startValueSpinBox)
        self.label_3 = QtWidgets.QLabel(mclAutoNumberingDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.incrementSpinBox = QtWidgets.QSpinBox(mclAutoNumberingDialog)
        self.incrementSpinBox.setObjectName("incrementSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.incrementSpinBox)
        self.label_2 = QtWidgets.QLabel(mclAutoNumberingDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(mclAutoNumberingDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.retranslateUi(mclAutoNumberingDialog)
        QtCore.QMetaObject.connectSlotsByName(mclAutoNumberingDialog)
        mclAutoNumberingDialog.setTabOrder(self.startValueSpinBox, self.incrementSpinBox)
        mclAutoNumberingDialog.setTabOrder(self.incrementSpinBox, self.buttonBox)

    def retranslateUi(self, mclAutoNumberingDialog):
        _translate = QtCore.QCoreApplication.translate
        mclAutoNumberingDialog.setWindowTitle(_translate("mclAutoNumberingDialog", "MCL Auto-numbering Tool"))
        self.label.setText(_translate("mclAutoNumberingDialog", "Use <ctrl-click> to modify the selection on the map canvas.  Add/remove MCL sections one at a time."))
        self.linkedPolysLabel.setText(_translate("mclAutoNumberingDialog", "MCL sections:"))
        self.label_3.setText(_translate("mclAutoNumberingDialog", "Increment:"))
        self.label_2.setText(_translate("mclAutoNumberingDialog", "Start value:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mclAutoNumberingDialog = QtWidgets.QDialog()
    ui = Ui_mclAutoNumberingDialog()
    ui.setupUi(mclAutoNumberingDialog)
    mclAutoNumberingDialog.show()
    sys.exit(app.exec_())

