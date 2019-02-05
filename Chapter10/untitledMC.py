# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitledMC.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(568, 191)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 531, 16))
        self.label.setObjectName("label")
        self.press = QtWidgets.QLabel(Dialog)
        self.press.setGeometry(QtCore.QRect(20, 60, 531, 16))
        self.press.setText("")
        self.press.setObjectName("press")
        self.release = QtWidgets.QLabel(Dialog)
        self.release.setGeometry(QtCore.QRect(20, 100, 531, 16))
        self.release.setText("")
        self.release.setObjectName("release")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "displays the x,y co-ordinates where mouse button is pressed and release"))

