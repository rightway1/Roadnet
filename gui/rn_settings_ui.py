# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_settings_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName("settingsDialog")
        settingsDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        settingsDialog.resize(342, 226)
        settingsDialog.setMinimumSize(QtCore.QSize(342, 226))
        settingsDialog.setMaximumSize(QtCore.QSize(342, 226))
        self.widget = QtWidgets.QWidget(settingsDialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 323, 211))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ShapeEditing = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShapeEditing.sizePolicy().hasHeightForWidth())
        self.ShapeEditing.setSizePolicy(sizePolicy)
        self.ShapeEditing.setMinimumSize(QtCore.QSize(319, 101))
        self.ShapeEditing.setMaximumSize(QtCore.QSize(319, 101))
        self.ShapeEditing.setObjectName("ShapeEditing")
        self.rdpolyCheckBox = QtWidgets.QCheckBox(self.ShapeEditing)
        self.rdpolyCheckBox.setGeometry(QtCore.QRect(11, 63, 271, 26))
        self.rdpolyCheckBox.setMaximumSize(QtCore.QSize(271, 26))
        self.rdpolyCheckBox.setChecked(True)
        self.rdpolyCheckBox.setObjectName("rdpolyCheckBox")
        self.esuCheckBox = QtWidgets.QCheckBox(self.ShapeEditing)
        self.esuCheckBox.setGeometry(QtCore.QRect(11, 31, 261, 26))
        self.esuCheckBox.setChecked(True)
        self.esuCheckBox.setObjectName("esuCheckBox")
        self.verticalLayout.addWidget(self.ShapeEditing)
        self.rampGroupBox = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rampGroupBox.sizePolicy().hasHeightForWidth())
        self.rampGroupBox.setSizePolicy(sizePolicy)
        self.rampGroupBox.setMinimumSize(QtCore.QSize(319, 61))
        self.rampGroupBox.setMaximumSize(QtCore.QSize(319, 61))
        self.rampGroupBox.setObjectName("rampGroupBox")
        self.rampCheckBox = QtWidgets.QCheckBox(self.rampGroupBox)
        self.rampCheckBox.setGeometry(QtCore.QRect(20, 30, 201, 22))
        self.rampCheckBox.setObjectName("rampCheckBox")
        self.verticalLayout.addWidget(self.rampGroupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.okButton = QtWidgets.QPushButton(self.widget)
        self.okButton.setObjectName("okButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.okButton)
        self.verticalLayout_2.addLayout(self.formLayout)

        self.retranslateUi(settingsDialog)
        self.okButton.clicked.connect(settingsDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        _translate = QtCore.QCoreApplication.translate
        settingsDialog.setWindowTitle(_translate("settingsDialog", "Settings"))
        self.ShapeEditing.setTitle(_translate("settingsDialog", "Shape editing"))
        self.rdpolyCheckBox.setText(_translate("settingsDialog", "Prevent overlapping polygons"))
        self.esuCheckBox.setText(_translate("settingsDialog", "Automatically split ESU\'s"))
        self.rampGroupBox.setTitle(_translate("settingsDialog", "RAMP settings"))
        self.rampCheckBox.setText(_translate("settingsDialog", "Enable RAMP"))
        self.okButton.setText(_translate("settingsDialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settingsDialog = QtWidgets.QDialog()
    ui = Ui_settingsDialog()
    ui.setupUi(settingsDialog)
    settingsDialog.show()
    sys.exit(app.exec_())

