# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_symbology_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_symbologyDialog(object):
    def setupUi(self, symbologyDialog):
        symbologyDialog.setObjectName("symbologyDialog")
        symbologyDialog.setWindowModality(QtCore.Qt.NonModal)
        symbologyDialog.resize(418, 141)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(symbologyDialog.sizePolicy().hasHeightForWidth())
        symbologyDialog.setSizePolicy(sizePolicy)
        symbologyDialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(symbologyDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtWidgets.QProgressBar(symbologyDialog)
        self.progressBar.setEnabled(True)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.runPushButton = QtWidgets.QPushButton(symbologyDialog)
        self.runPushButton.setObjectName("runPushButton")
        self.horizontalLayout.addWidget(self.runPushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.updatedFeaturesLabel = QtWidgets.QLabel(symbologyDialog)
        self.updatedFeaturesLabel.setObjectName("updatedFeaturesLabel")
        self.verticalLayout_2.addWidget(self.updatedFeaturesLabel)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(symbologyDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.esuCheckBox = QtWidgets.QCheckBox(symbologyDialog)
        self.esuCheckBox.setObjectName("esuCheckBox")
        self.verticalLayout.addWidget(self.esuCheckBox)
        self.rdPolyCheckBox = QtWidgets.QCheckBox(symbologyDialog)
        self.rdPolyCheckBox.setObjectName("rdPolyCheckBox")
        self.verticalLayout.addWidget(self.rdPolyCheckBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(symbologyDialog)
        QtCore.QMetaObject.connectSlotsByName(symbologyDialog)

    def retranslateUi(self, symbologyDialog):
        _translate = QtCore.QCoreApplication.translate
        symbologyDialog.setWindowTitle(_translate("symbologyDialog", "Update Symbology"))
        self.runPushButton.setText(_translate("symbologyDialog", "Run"))
        self.updatedFeaturesLabel.setText(_translate("symbologyDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Updated Features</span></p><p>ESU Graphic:</p><p>Road Polygon:</p></body></html>"))
        self.label.setText(_translate("symbologyDialog", "Select layers to update:"))
        self.esuCheckBox.setText(_translate("symbologyDialog", "ESU Graphic"))
        self.rdPolyCheckBox.setText(_translate("symbologyDialog", "Road Polygon"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    symbologyDialog = QtWidgets.QDialog()
    ui = Ui_symbologyDialog()
    ui.setupUi(symbologyDialog)
    symbologyDialog.show()
    sys.exit(app.exec_())

