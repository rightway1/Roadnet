# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_db_path_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newDbPathDialog(object):
    def setupUi(self, newDbPathDialog):
        newDbPathDialog.setObjectName("newDbPathDialog")
        newDbPathDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        newDbPathDialog.resize(700, 120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(newDbPathDialog.sizePolicy().hasHeightForWidth())
        newDbPathDialog.setSizePolicy(sizePolicy)
        newDbPathDialog.setMinimumSize(QtCore.QSize(700, 120))
        newDbPathDialog.setMaximumSize(QtCore.QSize(900, 120))
        newDbPathDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(newDbPathDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.applyButton = QtWidgets.QPushButton(newDbPathDialog)
        self.applyButton.setObjectName("applyButton")
        self.horizontalLayout_2.addWidget(self.applyButton)
        self.cancelButton = QtWidgets.QPushButton(newDbPathDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.newLabel = QtWidgets.QLabel(newDbPathDialog)
        self.newLabel.setObjectName("newLabel")
        self.horizontalLayout_3.addWidget(self.newLabel)
        spacerItem1 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.newPathLineEdit = QtWidgets.QLineEdit(newDbPathDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newPathLineEdit.sizePolicy().hasHeightForWidth())
        self.newPathLineEdit.setSizePolicy(sizePolicy)
        self.newPathLineEdit.setMinimumSize(QtCore.QSize(389, 0))
        self.newPathLineEdit.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.newPathLineEdit.setStyleSheet("")
        self.newPathLineEdit.setReadOnly(False)
        self.newPathLineEdit.setObjectName("newPathLineEdit")
        self.horizontalLayout_3.addWidget(self.newPathLineEdit)
        self.openButton = QtWidgets.QPushButton(newDbPathDialog)
        self.openButton.setText("")
        self.openButton.setObjectName("openButton")
        self.horizontalLayout_3.addWidget(self.openButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.currLabel = QtWidgets.QLabel(newDbPathDialog)
        self.currLabel.setObjectName("currLabel")
        self.horizontalLayout_5.addWidget(self.currLabel)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.currPathLineEdit = QtWidgets.QLineEdit(newDbPathDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currPathLineEdit.sizePolicy().hasHeightForWidth())
        self.currPathLineEdit.setSizePolicy(sizePolicy)
        self.currPathLineEdit.setMinimumSize(QtCore.QSize(380, 0))
        self.currPathLineEdit.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.currPathLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.currPathLineEdit.setReadOnly(True)
        self.currPathLineEdit.setObjectName("currPathLineEdit")
        self.horizontalLayout_5.addWidget(self.currPathLineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(45, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.retranslateUi(newDbPathDialog)
        QtCore.QMetaObject.connectSlotsByName(newDbPathDialog)

    def retranslateUi(self, newDbPathDialog):
        _translate = QtCore.QCoreApplication.translate
        newDbPathDialog.setWindowTitle(_translate("newDbPathDialog", "Change Database Location"))
        self.applyButton.setText(_translate("newDbPathDialog", "Apply"))
        self.cancelButton.setText(_translate("newDbPathDialog", "Cancel"))
        self.newLabel.setText(_translate("newDbPathDialog", "New Database Path: "))
        self.currLabel.setText(_translate("newDbPathDialog", "Current Database Path:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newDbPathDialog = QtWidgets.QDialog()
    ui = Ui_newDbPathDialog()
    ui.setupUi(newDbPathDialog)
    newDbPathDialog.show()
    sys.exit(app.exec_())

