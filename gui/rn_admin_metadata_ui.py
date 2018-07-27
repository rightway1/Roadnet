# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_admin_metadata_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_metadataDialog(object):
    def setupUi(self, metadataDialog):
        metadataDialog.setObjectName("metadataDialog")
        metadataDialog.resize(342, 483)
        metadataDialog.setSizeGripEnabled(False)
        metadataDialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(metadataDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(metadataDialog)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.mailLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.mailLineEdit.setObjectName("mailLineEdit")
        self.gridLayout_8.addWidget(self.mailLineEdit, 4, 1, 1, 2)
        self.classLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.classLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.classLineEdit.setReadOnly(True)
        self.classLineEdit.setObjectName("classLineEdit")
        self.gridLayout_8.addWidget(self.classLineEdit, 8, 1, 1, 2)
        self.custLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.custLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.custLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.custLineEdit.setText("")
        self.custLineEdit.setReadOnly(True)
        self.custLineEdit.setObjectName("custLineEdit")
        self.gridLayout_8.addWidget(self.custLineEdit, 12, 1, 1, 1)
        self.stateLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.stateLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.stateLineEdit.setReadOnly(True)
        self.stateLineEdit.setObjectName("stateLineEdit")
        self.gridLayout_8.addWidget(self.stateLineEdit, 9, 1, 1, 2)
        self.custLbl = QtWidgets.QLabel(self.groupBox_2)
        self.custLbl.setObjectName("custLbl")
        self.gridLayout_8.addWidget(self.custLbl, 12, 0, 1, 1)
        self.gazLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.gazLineEdit.setObjectName("gazLineEdit")
        self.gridLayout_8.addWidget(self.gazLineEdit, 3, 1, 1, 2)
        self.scopeLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.scopeLineEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.scopeLineEdit.setObjectName("scopeLineEdit")
        self.gridLayout_8.addWidget(self.scopeLineEdit, 1, 1, 1, 2)
        self.terrLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.terrLineEdit.setObjectName("terrLineEdit")
        self.gridLayout_8.addWidget(self.terrLineEdit, 2, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem, 0, 2, 1, 1)
        self.stateLbl = QtWidgets.QLabel(self.groupBox_2)
        self.stateLbl.setObjectName("stateLbl")
        self.gridLayout_8.addWidget(self.stateLbl, 9, 0, 1, 1)
        self.classLbl = QtWidgets.QLabel(self.groupBox_2)
        self.classLbl.setObjectName("classLbl")
        self.gridLayout_8.addWidget(self.classLbl, 8, 0, 1, 1)
        self.charLbl = QtWidgets.QLabel(self.groupBox_2)
        self.charLbl.setObjectName("charLbl")
        self.gridLayout_8.addWidget(self.charLbl, 11, 0, 1, 1)
        self.langLbl = QtWidgets.QLabel(self.groupBox_2)
        self.langLbl.setObjectName("langLbl")
        self.gridLayout_8.addWidget(self.langLbl, 10, 0, 1, 1)
        self.charCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.charCheckBox.setObjectName("charCheckBox")
        self.gridLayout_8.addWidget(self.charCheckBox, 11, 1, 1, 1)
        self.langCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.langCheckBox.setObjectName("langCheckBox")
        self.gridLayout_8.addWidget(self.langCheckBox, 10, 1, 1, 1)
        self.metaLbl = QtWidgets.QLabel(self.groupBox_2)
        self.metaLbl.setObjectName("metaLbl")
        self.gridLayout_8.addWidget(self.metaLbl, 7, 0, 1, 1)
        self.unitsLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.unitsLineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.unitsLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.unitsLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.unitsLineEdit.setText("")
        self.unitsLineEdit.setReadOnly(True)
        self.unitsLineEdit.setObjectName("unitsLineEdit")
        self.gridLayout_8.addWidget(self.unitsLineEdit, 6, 1, 1, 1)
        self.metaLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.metaLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.metaLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.metaLineEdit.setText("")
        self.metaLineEdit.setReadOnly(True)
        self.metaLineEdit.setObjectName("metaLineEdit")
        self.gridLayout_8.addWidget(self.metaLineEdit, 7, 1, 1, 1)
        self.nameLbl = QtWidgets.QLabel(self.groupBox_2)
        self.nameLbl.setObjectName("nameLbl")
        self.gridLayout_8.addWidget(self.nameLbl, 0, 0, 1, 1)
        self.nameLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.nameLineEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.nameLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.nameLineEdit.setReadOnly(True)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridLayout_8.addWidget(self.nameLineEdit, 0, 1, 1, 1)
        self.scopeLbl = QtWidgets.QLabel(self.groupBox_2)
        self.scopeLbl.setObjectName("scopeLbl")
        self.gridLayout_8.addWidget(self.scopeLbl, 1, 0, 1, 1)
        self.emailLbl = QtWidgets.QLabel(self.groupBox_2)
        self.emailLbl.setObjectName("emailLbl")
        self.gridLayout_8.addWidget(self.emailLbl, 4, 0, 1, 1)
        self.gazLbl = QtWidgets.QLabel(self.groupBox_2)
        self.gazLbl.setObjectName("gazLbl")
        self.gridLayout_8.addWidget(self.gazLbl, 3, 0, 1, 1)
        self.coordLbl = QtWidgets.QLabel(self.groupBox_2)
        self.coordLbl.setObjectName("coordLbl")
        self.gridLayout_8.addWidget(self.coordLbl, 5, 0, 1, 1)
        self.terrLbl = QtWidgets.QLabel(self.groupBox_2)
        self.terrLbl.setObjectName("terrLbl")
        self.gridLayout_8.addWidget(self.terrLbl, 2, 0, 1, 1)
        self.unitsLbl = QtWidgets.QLabel(self.groupBox_2)
        self.unitsLbl.setObjectName("unitsLbl")
        self.gridLayout_8.addWidget(self.unitsLbl, 6, 0, 1, 1)
        self.coordLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.coordLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.coordLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.coordLineEdit.setReadOnly(True)
        self.coordLineEdit.setObjectName("coordLineEdit")
        self.gridLayout_8.addWidget(self.coordLineEdit, 5, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(metadataDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.lsgLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lsgLineEdit.setMinimumSize(QtCore.QSize(80, 20))
        self.lsgLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lsgLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.lsgLineEdit.setReadOnly(True)
        self.lsgLineEdit.setObjectName("lsgLineEdit")
        self.horizontalLayout_3.addWidget(self.lsgLineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_3.addWidget(self.label_18)
        self.asdLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.asdLineEdit.setMinimumSize(QtCore.QSize(80, 20))
        self.asdLineEdit.setMaximumSize(QtCore.QSize(80, 20))
        self.asdLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.asdLineEdit.setReadOnly(True)
        self.asdLineEdit.setObjectName("asdLineEdit")
        self.horizontalLayout_3.addWidget(self.asdLineEdit)
        self.gridLayout_9.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(metadataDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(metadataDialog)
        QtCore.QMetaObject.connectSlotsByName(metadataDialog)

    def retranslateUi(self, metadataDialog):
        _translate = QtCore.QCoreApplication.translate
        metadataDialog.setWindowTitle(_translate("metadataDialog", "Metadata"))
        self.custLbl.setText(_translate("metadataDialog", "Custodian Code:"))
        self.stateLbl.setText(_translate("metadataDialog", "State Coding Scheme:"))
        self.classLbl.setText(_translate("metadataDialog", "Classification Scheme:"))
        self.charLbl.setText(_translate("metadataDialog", "Character Set: "))
        self.langLbl.setText(_translate("metadataDialog", "Language:"))
        self.charCheckBox.setText(_translate("metadataDialog", "Contains Gaelic Character?"))
        self.langCheckBox.setText(_translate("metadataDialog", "Contains Gaelic?"))
        self.metaLbl.setText(_translate("metadataDialog", "Metadata Date:"))
        self.nameLbl.setText(_translate("metadataDialog", "Name:"))
        self.scopeLbl.setText(_translate("metadataDialog", "Scope:"))
        self.emailLbl.setText(_translate("metadataDialog", "Custodian Email:"))
        self.gazLbl.setText(_translate("metadataDialog", "Gazetter Owner:"))
        self.coordLbl.setText(_translate("metadataDialog", "Cordinate System:"))
        self.terrLbl.setText(_translate("metadataDialog", "Territory of use:"))
        self.unitsLbl.setText(_translate("metadataDialog", "Units:"))
        self.groupBox.setTitle(_translate("metadataDialog", "Latest Changes"))
        self.label_17.setText(_translate("metadataDialog", "LSG: "))
        self.label_18.setText(_translate("metadataDialog", "ASD:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    metadataDialog = QtWidgets.QDialog()
    ui = Ui_metadataDialog()
    ui.setupUi(metadataDialog)
    metadataDialog.show()
    sys.exit(app.exec_())

