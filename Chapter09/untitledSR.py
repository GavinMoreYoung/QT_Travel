# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitledSR.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(449, 250)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.label_2.setObjectName("label_2")
        self.eamil = QtWidgets.QLineEdit(Dialog)
        self.eamil.setGeometry(QtCore.QRect(160, 40, 271, 20))
        self.eamil.setObjectName("eamil")
        self.passwd = QtWidgets.QLineEdit(Dialog)
        self.passwd.setGeometry(QtCore.QRect(160, 100, 271, 20))
        self.passwd.setObjectName("passwd")
        self.first = QtWidgets.QPushButton(Dialog)
        self.first.setGeometry(QtCore.QRect(20, 150, 91, 31))
        self.first.setObjectName("first")
        self.previous = QtWidgets.QPushButton(Dialog)
        self.previous.setGeometry(QtCore.QRect(130, 150, 91, 31))
        self.previous.setObjectName("previous")
        self.next = QtWidgets.QPushButton(Dialog)
        self.next.setGeometry(QtCore.QRect(230, 150, 91, 31))
        self.next.setObjectName("next")
        self.last = QtWidgets.QPushButton(Dialog)
        self.last.setGeometry(QtCore.QRect(340, 150, 91, 31))
        self.last.setObjectName("last")
        self.message = QtWidgets.QLabel(Dialog)
        self.message.setGeometry(QtCore.QRect(20, 205, 411, 31))
        self.message.setText("")
        self.message.setObjectName("message")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "email"))
        self.label_2.setText(_translate("Dialog", "password"))
        self.first.setText(_translate("Dialog", "first row"))
        self.previous.setText(_translate("Dialog", "previous"))
        self.next.setText(_translate("Dialog", "next"))
        self.last.setText(_translate("Dialog", "last row"))

