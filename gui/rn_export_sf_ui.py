# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rn_export_sf_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectedFeatures(object):
    def setupUi(self, selectedFeatures):
        selectedFeatures.setObjectName("selectedFeatures")
        selectedFeatures.resize(351, 96)
        self.label_2 = QtWidgets.QLabel(selectedFeatures)
        self.label_2.setGeometry(QtCore.QRect(10, 13, 328, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(selectedFeatures)
        self.line.setGeometry(QtCore.QRect(10, 51, 328, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(selectedFeatures)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 328, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.okPushButton.setObjectName("okPushButton")
        self.horizontalLayout.addWidget(self.okPushButton)
        self.noPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.noPushButton.setObjectName("noPushButton")
        self.horizontalLayout.addWidget(self.noPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)

        self.retranslateUi(selectedFeatures)
        QtCore.QMetaObject.connectSlotsByName(selectedFeatures)

    def retranslateUi(self, selectedFeatures):
        _translate = QtCore.QCoreApplication.translate
        selectedFeatures.setWindowTitle(_translate("selectedFeatures", "Selected Features?"))
        self.label_2.setText(_translate("selectedFeatures", "Do you want to export selected features? "))
        self.okPushButton.setText(_translate("selectedFeatures", "Yes"))
        self.noPushButton.setText(_translate("selectedFeatures", "No"))
        self.cancelPushButton.setText(_translate("selectedFeatures", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectedFeatures = QtWidgets.QDialog()
    ui = Ui_selectedFeatures()
    ui.setupUi(selectedFeatures)
    selectedFeatures.show()
    sys.exit(app.exec_())

