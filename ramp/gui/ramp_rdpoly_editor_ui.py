# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ramp_rdpoly_editor_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RdpolyEditorDialog(object):
    def setupUi(self, RdpolyEditorDialog):
        RdpolyEditorDialog.setObjectName("RdpolyEditorDialog")
        RdpolyEditorDialog.resize(589, 437)
        RdpolyEditorDialog.setMinimumSize(QtCore.QSize(589, 437))
        self.gridLayout_8 = QtWidgets.QGridLayout(RdpolyEditorDialog)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox = QtWidgets.QGroupBox(RdpolyEditorDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.mclLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.mclLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.mclLineEdit.setReadOnly(True)
        self.mclLineEdit.setObjectName("mclLineEdit")
        self.gridLayout_2.addWidget(self.mclLineEdit, 1, 0, 1, 1)
        self.usrnLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.usrnLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.usrnLineEdit.setReadOnly(True)
        self.usrnLineEdit.setObjectName("usrnLineEdit")
        self.gridLayout_2.addWidget(self.usrnLineEdit, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)
        self.lorDescPlainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.lorDescPlainTextEdit.setMinimumSize(QtCore.QSize(335, 0))
        self.lorDescPlainTextEdit.setMaximumSize(QtCore.QSize(366, 16777215))
        self.lorDescPlainTextEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.lorDescPlainTextEdit.setReadOnly(True)
        self.lorDescPlainTextEdit.setObjectName("lorDescPlainTextEdit")
        self.gridLayout_5.addWidget(self.lorDescPlainTextEdit, 2, 0, 2, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 2, 1, 1, 1)
        self.laneNumberLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.laneNumberLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.laneNumberLineEdit.setReadOnly(True)
        self.laneNumberLineEdit.setObjectName("laneNumberLineEdit")
        self.gridLayout_5.addWidget(self.laneNumberLineEdit, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 3, 1, 1, 1)
        self.speedLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.speedLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.speedLineEdit.setReadOnly(True)
        self.speedLineEdit.setObjectName("speedLineEdit")
        self.gridLayout_5.addWidget(self.speedLineEdit, 3, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(RdpolyEditorDialog)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.rdpolyLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.rdpolyLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.rdpolyLineEdit.setReadOnly(True)
        self.rdpolyLineEdit.setObjectName("rdpolyLineEdit")
        self.gridLayout.addWidget(self.rdpolyLineEdit, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.elementComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.elementComboBox.setMinimumSize(QtCore.QSize(176, 0))
        self.elementComboBox.setMinimumContentsLength(0)
        self.elementComboBox.setObjectName("elementComboBox")
        self.gridLayout.addWidget(self.elementComboBox, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.offsetComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.offsetComboBox.setObjectName("offsetComboBox")
        self.gridLayout.addWidget(self.offsetComboBox, 1, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 4, 1, 1)
        self.lengthLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lengthLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.lengthLineEdit.setReadOnly(True)
        self.lengthLineEdit.setObjectName("lengthLineEdit")
        self.gridLayout.addWidget(self.lengthLineEdit, 1, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.hierarchyComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.hierarchyComboBox.setObjectName("hierarchyComboBox")
        self.gridLayout.addWidget(self.hierarchyComboBox, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.numberLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.numberLineEdit.setObjectName("numberLineEdit")
        self.gridLayout.addWidget(self.numberLineEdit, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 5, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.combinedRefLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.combinedRefLineEdit.sizePolicy().hasHeightForWidth())
        self.combinedRefLineEdit.setSizePolicy(sizePolicy)
        self.combinedRefLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.combinedRefLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.combinedRefLineEdit.setReadOnly(True)
        self.combinedRefLineEdit.setObjectName("combinedRefLineEdit")
        self.gridLayout_3.addWidget(self.combinedRefLineEdit, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setBaseSize(QtCore.QSize(0, 50))
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(RdpolyEditorDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_8.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.groupBox.raise_()
        self.mclLineEdit.raise_()
        self.label.raise_()
        self.rdpolyLineEdit.raise_()
        self.label_2.raise_()
        self.usrnLineEdit.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label.raise_()
        self.mclLineEdit.raise_()
        self.rdpolyLineEdit.raise_()
        self.usrnLineEdit.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lorDescPlainTextEdit.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.laneNumberLineEdit.raise_()
        self.label_6.raise_()
        self.speedLineEdit.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.numberLineEdit.raise_()
        self.combinedRefLineEdit.raise_()
        self.elementComboBox.raise_()
        self.hierarchyComboBox.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.groupBox_2.raise_()
        self.buttonBox.raise_()

        self.retranslateUi(RdpolyEditorDialog)
        self.buttonBox.accepted.connect(RdpolyEditorDialog.accept)
        self.buttonBox.rejected.connect(RdpolyEditorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RdpolyEditorDialog)
        RdpolyEditorDialog.setTabOrder(self.elementComboBox, self.hierarchyComboBox)
        RdpolyEditorDialog.setTabOrder(self.hierarchyComboBox, self.offsetComboBox)
        RdpolyEditorDialog.setTabOrder(self.offsetComboBox, self.numberLineEdit)
        RdpolyEditorDialog.setTabOrder(self.numberLineEdit, self.lengthLineEdit)
        RdpolyEditorDialog.setTabOrder(self.lengthLineEdit, self.laneNumberLineEdit)
        RdpolyEditorDialog.setTabOrder(self.laneNumberLineEdit, self.combinedRefLineEdit)
        RdpolyEditorDialog.setTabOrder(self.combinedRefLineEdit, self.rdpolyLineEdit)
        RdpolyEditorDialog.setTabOrder(self.rdpolyLineEdit, self.usrnLineEdit)
        RdpolyEditorDialog.setTabOrder(self.usrnLineEdit, self.buttonBox)
        RdpolyEditorDialog.setTabOrder(self.buttonBox, self.speedLineEdit)
        RdpolyEditorDialog.setTabOrder(self.speedLineEdit, self.lorDescPlainTextEdit)
        RdpolyEditorDialog.setTabOrder(self.lorDescPlainTextEdit, self.mclLineEdit)

    def retranslateUi(self, RdpolyEditorDialog):
        _translate = QtCore.QCoreApplication.translate
        RdpolyEditorDialog.setWindowTitle(_translate("RdpolyEditorDialog", "RAMP - Edit Polygon"))
        self.groupBox.setTitle(_translate("RdpolyEditorDialog", "MCL Attributes"))
        self.label.setText(_translate("RdpolyEditorDialog", "MCL ID:"))
        self.label_3.setText(_translate("RdpolyEditorDialog", "USRN:"))
        self.label_4.setText(_translate("RdpolyEditorDialog", "Description:"))
        self.label_5.setText(_translate("RdpolyEditorDialog", "No. of Lanes:"))
        self.label_6.setText(_translate("RdpolyEditorDialog", "Speed:"))
        self.groupBox_2.setTitle(_translate("RdpolyEditorDialog", "Polygon attributes"))
        self.label_2.setText(_translate("RdpolyEditorDialog", "Polygon ID:"))
        self.label_10.setText(_translate("RdpolyEditorDialog", "Element:"))
        self.label_7.setText(_translate("RdpolyEditorDialog", "desc_2:"))
        self.label_12.setText(_translate("RdpolyEditorDialog", "Length (m):"))
        self.label_11.setText(_translate("RdpolyEditorDialog", "Hierarchy:"))
        self.label_8.setText(_translate("RdpolyEditorDialog", "desc_3:"))
        self.label_9.setText(_translate("RdpolyEditorDialog", "Combined Ref:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RdpolyEditorDialog = QtWidgets.QDialog()
    ui = Ui_RdpolyEditorDialog()
    ui.setupUi(RdpolyEditorDialog)
    RdpolyEditorDialog.show()
    sys.exit(app.exec_())

