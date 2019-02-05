# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitledDU.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(405, 229)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 101, 16))
        self.label_2.setObjectName("label_2")
        self.email = QtWidgets.QLineEdit(Dialog)
        self.email.setGeometry(QtCore.QRect(120, 30, 261, 20))
        self.email.setObjectName("email")
        self.passwd = QtWidgets.QLineEdit(Dialog)
        self.passwd.setGeometry(QtCore.QRect(120, 80, 261, 20))
        self.passwd.setObjectName("passwd")
        self.delbutton = QtWidgets.QPushButton(Dialog)
        self.delbutton.setGeometry(QtCore.QRect(150, 120, 111, 31))
        self.delbutton.setObjectName("delbutton")
        self.message = QtWidgets.QLabel(Dialog)
        self.message.setGeometry(QtCore.QRect(0, 200, 401, 21))
        self.message.setText("")
        self.message.setObjectName("message")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 160, 101, 16))
        self.label_4.setObjectName("label_4")
        self.byes = QtWidgets.QPushButton(Dialog)
        self.byes.setGeometry(QtCore.QRect(180, 160, 51, 23))
        self.byes.setObjectName("byes")
        self.bno = QtWidgets.QPushButton(Dialog)
        self.bno.setGeometry(QtCore.QRect(280, 160, 51, 23))
        self.bno.setObjectName("bno")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Email Address"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.delbutton.setText(_translate("Dialog", "delete User"))
        self.label_4.setText(_translate("Dialog", "Are you sure?"))
        self.byes.setText(_translate("Dialog", "yes"))
        self.bno.setText(_translate("Dialog", "no"))

