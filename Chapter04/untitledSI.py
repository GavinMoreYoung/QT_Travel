# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitledSI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 81, 16))
        self.label_4.setObjectName("label_4")
        self.lecode = QtWidgets.QLineEdit(Dialog)
        self.lecode.setGeometry(QtCore.QRect(130, 20, 191, 20))
        self.lecode.setObjectName("lecode")
        self.lename = QtWidgets.QLineEdit(Dialog)
        self.lename.setGeometry(QtCore.QRect(130, 60, 191, 20))
        self.lename.setObjectName("lename")
        self.leem = QtWidgets.QLineEdit(Dialog)
        self.leem.setGeometry(QtCore.QRect(130, 110, 191, 20))
        self.leem.setObjectName("leem")
        self.lemm = QtWidgets.QLineEdit(Dialog)
        self.lemm.setGeometry(QtCore.QRect(120, 160, 201, 20))
        self.lemm.setObjectName("lemm")
        self.message = QtWidgets.QLabel(Dialog)
        self.message.setGeometry(QtCore.QRect(70, 200, 251, 51))
        self.message.setText("")
        self.message.setObjectName("message")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "student code"))
        self.label_2.setText(_translate("Dialog", "student name"))
        self.label_3.setText(_translate("Dialog", "english mark"))
        self.label_4.setText(_translate("Dialog", "math mark"))
        self.pushButton.setText(_translate("Dialog", "click"))

