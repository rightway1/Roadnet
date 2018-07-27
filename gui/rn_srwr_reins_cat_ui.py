# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_srwr_reins_cat_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_srwrReinsCatDialog(object):
    def setupUi(self, srwrReinsCatDialog):
        srwrReinsCatDialog.setObjectName("srwrReinsCatDialog")
        srwrReinsCatDialog.setWindowModality(QtCore.Qt.NonModal)
        srwrReinsCatDialog.resize(372, 438)
        self.gridLayout = QtWidgets.QGridLayout(srwrReinsCatDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(srwrReinsCatDialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.locationLabel = QtWidgets.QLabel(self.groupBox)
        self.locationLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.locationLabel.setObjectName("locationLabel")
        self.gridLayout_9.addWidget(self.locationLabel, 1, 0, 1, 1)
        self.maintIdLabel = QtWidgets.QLabel(self.groupBox)
        self.maintIdLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.maintIdLabel.setObjectName("maintIdLabel")
        self.gridLayout_9.addWidget(self.maintIdLabel, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.locationTextEdit = QtWidgets.QTextEdit(self.groupBox)
        self.locationTextEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.locationTextEdit.setReadOnly(True)
        self.locationTextEdit.setObjectName("locationTextEdit")
        self.horizontalLayout.addWidget(self.locationTextEdit)
        self.gridLayout_9.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.notesLabel = QtWidgets.QLabel(self.groupBox)
        self.notesLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.notesLabel.setObjectName("notesLabel")
        self.gridLayout_9.addWidget(self.notesLabel, 5, 0, 1, 1)
        self.wholeRoadCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.wholeRoadCheckBox.setObjectName("wholeRoadCheckBox")
        self.gridLayout_9.addWidget(self.wholeRoadCheckBox, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.entryDateLineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entryDateLineEdit.sizePolicy().hasHeightForWidth())
        self.entryDateLineEdit.setSizePolicy(sizePolicy)
        self.entryDateLineEdit.setMinimumSize(QtCore.QSize(40, 0))
        self.entryDateLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.entryDateLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.entryDateLineEdit.setReadOnly(True)
        self.entryDateLineEdit.setObjectName("entryDateLineEdit")
        self.horizontalLayout_3.addWidget(self.entryDateLineEdit)
        self.byLabel = QtWidgets.QLabel(self.groupBox)
        self.byLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.byLabel.setObjectName("byLabel")
        self.horizontalLayout_3.addWidget(self.byLabel)
        self.byLineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.byLineEdit.sizePolicy().hasHeightForWidth())
        self.byLineEdit.setSizePolicy(sizePolicy)
        self.byLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.byLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.byLineEdit.setReadOnly(True)
        self.byLineEdit.setObjectName("byLineEdit")
        self.horizontalLayout_3.addWidget(self.byLineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout_9.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.versionLineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionLineEdit.sizePolicy().hasHeightForWidth())
        self.versionLineEdit.setSizePolicy(sizePolicy)
        self.versionLineEdit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.versionLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.versionLineEdit.setText("")
        self.versionLineEdit.setReadOnly(True)
        self.versionLineEdit.setObjectName("versionLineEdit")
        self.gridLayout_2.addWidget(self.versionLineEdit, 0, 1, 1, 1)
        self.reinsCatIdLineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reinsCatIdLineEdit.sizePolicy().hasHeightForWidth())
        self.reinsCatIdLineEdit.setSizePolicy(sizePolicy)
        self.reinsCatIdLineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.reinsCatIdLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.reinsCatIdLineEdit.setReadOnly(True)
        self.reinsCatIdLineEdit.setObjectName("reinsCatIdLineEdit")
        self.gridLayout_2.addWidget(self.reinsCatIdLineEdit, 0, 0, 1, 1)
        self.refLabel = QtWidgets.QLabel(self.groupBox)
        self.refLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.refLabel.setObjectName("refLabel")
        self.gridLayout_2.addWidget(self.refLabel, 0, 2, 1, 1)
        self.refLineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refLineEdit.sizePolicy().hasHeightForWidth())
        self.refLineEdit.setSizePolicy(sizePolicy)
        self.refLineEdit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.refLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.refLineEdit.setReadOnly(True)
        self.refLineEdit.setObjectName("refLineEdit")
        self.gridLayout_2.addWidget(self.refLineEdit, 0, 3, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.swaLabel = QtWidgets.QLabel(self.groupBox)
        self.swaLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.swaLabel.setObjectName("swaLabel")
        self.gridLayout_9.addWidget(self.swaLabel, 3, 0, 1, 1)
        self.entryDateLabel = QtWidgets.QLabel(self.groupBox)
        self.entryDateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entryDateLabel.setObjectName("entryDateLabel")
        self.gridLayout_9.addWidget(self.entryDateLabel, 4, 0, 1, 1)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.groupBox)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_9)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.categoryLineEdit = QtWidgets.QLineEdit(self.page_9)
        self.categoryLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.categoryLineEdit.setReadOnly(True)
        self.categoryLineEdit.setObjectName("categoryLineEdit")
        self.gridLayout_7.addWidget(self.categoryLineEdit, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page_10)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.categoryComboBox = QtWidgets.QComboBox(self.page_10)
        self.categoryComboBox.setObjectName("categoryComboBox")
        self.gridLayout_10.addWidget(self.categoryComboBox, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_10)
        self.gridLayout_9.addWidget(self.stackedWidget_2, 3, 1, 1, 1)
        self.notesTextEdit = QtWidgets.QTextEdit(self.groupBox)
        self.notesTextEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.notesTextEdit.setReadOnly(True)
        self.notesTextEdit.setObjectName("notesTextEdit")
        self.gridLayout_9.addWidget(self.notesTextEdit, 5, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.coordinatesGroupBox = QtWidgets.QGroupBox(srwrReinsCatDialog)
        self.coordinatesGroupBox.setObjectName("coordinatesGroupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.coordinatesGroupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_15.setVerticalSpacing(6)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.endXLineEdit = QtWidgets.QLineEdit(self.coordinatesGroupBox)
        self.endXLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.endXLineEdit.setReadOnly(True)
        self.endXLineEdit.setObjectName("endXLineEdit")
        self.gridLayout_15.addWidget(self.endXLineEdit, 1, 1, 1, 1)
        self.startYLabel = QtWidgets.QLabel(self.coordinatesGroupBox)
        self.startYLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startYLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.startYLabel.setObjectName("startYLabel")
        self.gridLayout_15.addWidget(self.startYLabel, 0, 2, 1, 1)
        self.endXLabel = QtWidgets.QLabel(self.coordinatesGroupBox)
        self.endXLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.endXLabel.setObjectName("endXLabel")
        self.gridLayout_15.addWidget(self.endXLabel, 1, 0, 1, 1)
        self.startYLineEdit = QtWidgets.QLineEdit(self.coordinatesGroupBox)
        self.startYLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.startYLineEdit.setReadOnly(True)
        self.startYLineEdit.setObjectName("startYLineEdit")
        self.gridLayout_15.addWidget(self.startYLineEdit, 0, 3, 1, 1)
        self.startXLabel = QtWidgets.QLabel(self.coordinatesGroupBox)
        self.startXLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.startXLabel.setObjectName("startXLabel")
        self.gridLayout_15.addWidget(self.startXLabel, 0, 0, 1, 1)
        self.startXLineEdit = QtWidgets.QLineEdit(self.coordinatesGroupBox)
        self.startXLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.startXLineEdit.setReadOnly(True)
        self.startXLineEdit.setObjectName("startXLineEdit")
        self.gridLayout_15.addWidget(self.startXLineEdit, 0, 1, 1, 1)
        self.endYLabel = QtWidgets.QLabel(self.coordinatesGroupBox)
        self.endYLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.endYLabel.setAutoFillBackground(False)
        self.endYLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.endYLabel.setObjectName("endYLabel")
        self.gridLayout_15.addWidget(self.endYLabel, 1, 2, 1, 1)
        self.endYLineEdit = QtWidgets.QLineEdit(self.coordinatesGroupBox)
        self.endYLineEdit.setStyleSheet("border-width:0.5px;\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-color:  rgb(100,100,100);\n"
"background-color: rgb(213, 234, 234);")
        self.endYLineEdit.setReadOnly(True)
        self.endYLineEdit.setObjectName("endYLineEdit")
        self.gridLayout_15.addWidget(self.endYLineEdit, 1, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_15, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.editLinkPushButton = QtWidgets.QPushButton(self.coordinatesGroupBox)
        self.editLinkPushButton.setEnabled(False)
        self.editLinkPushButton.setFlat(False)
        self.editLinkPushButton.setObjectName("editLinkPushButton")
        self.horizontalLayout_4.addWidget(self.editLinkPushButton)
        self.editCoordsPushButton = QtWidgets.QPushButton(self.coordinatesGroupBox)
        self.editCoordsPushButton.setEnabled(False)
        self.editCoordsPushButton.setObjectName("editCoordsPushButton")
        self.horizontalLayout_4.addWidget(self.editCoordsPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.mapPushButton = QtWidgets.QPushButton(self.coordinatesGroupBox)
        self.mapPushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.mapPushButton.setObjectName("mapPushButton")
        self.horizontalLayout_4.addWidget(self.mapPushButton)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.coordinatesGroupBox, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.closePushButton = QtWidgets.QPushButton(srwrReinsCatDialog)
        self.closePushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.closePushButton.setObjectName("closePushButton")
        self.horizontalLayout_5.addWidget(self.closePushButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.retranslateUi(srwrReinsCatDialog)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(srwrReinsCatDialog)

    def retranslateUi(self, srwrReinsCatDialog):
        _translate = QtCore.QCoreApplication.translate
        srwrReinsCatDialog.setWindowTitle(_translate("srwrReinsCatDialog", "Reinstatement Category Record"))
        self.locationLabel.setText(_translate("srwrReinsCatDialog", "Location"))
        self.maintIdLabel.setText(_translate("srwrReinsCatDialog", "Reins ID"))
        self.notesLabel.setText(_translate("srwrReinsCatDialog", "Notes"))
        self.wholeRoadCheckBox.setText(_translate("srwrReinsCatDialog", "Whole road"))
        self.byLabel.setText(_translate("srwrReinsCatDialog", "By"))
        self.refLabel.setText(_translate("srwrReinsCatDialog", "Ref"))
        self.swaLabel.setText(_translate("srwrReinsCatDialog", "Category"))
        self.entryDateLabel.setText(_translate("srwrReinsCatDialog", "Entry Date"))
        self.coordinatesGroupBox.setTitle(_translate("srwrReinsCatDialog", "Coordinates"))
        self.startYLabel.setText(_translate("srwrReinsCatDialog", "Start Y"))
        self.endXLabel.setText(_translate("srwrReinsCatDialog", "End X"))
        self.startXLabel.setText(_translate("srwrReinsCatDialog", "Start X"))
        self.endYLabel.setText(_translate("srwrReinsCatDialog", "End Y"))
        self.editLinkPushButton.setText(_translate("srwrReinsCatDialog", "Edit Polygon/Maint Link"))
        self.editCoordsPushButton.setText(_translate("srwrReinsCatDialog", "Edit Start/End Coordinates"))
        self.mapPushButton.setText(_translate("srwrReinsCatDialog", "Map"))
        self.closePushButton.setText(_translate("srwrReinsCatDialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    srwrReinsCatDialog = QtWidgets.QDialog()
    ui = Ui_srwrReinsCatDialog()
    ui.setupUi(srwrReinsCatDialog)
    srwrReinsCatDialog.show()
    sys.exit(app.exec_())

