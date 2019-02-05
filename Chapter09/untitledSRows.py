# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitledSRows.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(442, 290)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 151, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 151, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 250, 151, 16))
        self.label_4.setObjectName("label_4")
        self.databasenm = QtWidgets.QLineEdit(Dialog)
        self.databasenm.setGeometry(QtCore.QRect(180, 30, 221, 20))
        self.databasenm.setObjectName("databasenm")
        self.tablenm = QtWidgets.QLineEdit(Dialog)
        self.tablenm.setGeometry(QtCore.QRect(180, 90, 221, 20))
        self.tablenm.setObjectName("tablenm")
        self.email = QtWidgets.QLineEdit(Dialog)
        self.email.setGeometry(QtCore.QRect(180, 150, 221, 20))
        self.email.setObjectName("email")
        self.passwd = QtWidgets.QLineEdit(Dialog)
        self.passwd.setGeometry(QtCore.QRect(170, 250, 221, 20))
        self.passwd.setObjectName("passwd")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 190, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.message = QtWidgets.QLabel(Dialog)
        self.message.setGeometry(QtCore.QRect(20, 220, 391, 16))
        self.message.setText("")
        self.message.setObjectName("message")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "enter database name"))
        self.label_2.setText(_translate("Dialog", "enter table name"))
        self.label_3.setText(_translate("Dialog", "email address"))
        self.label_4.setText(_translate("Dialog", "password"))
        self.pushButton.setText(_translate("Dialog", "search"))

