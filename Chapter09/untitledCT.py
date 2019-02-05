# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitledCT.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(479, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(43, 100, 111, 20))
        self.label_2.setObjectName("label_2")
        self.databasenm = QtWidgets.QLineEdit(Dialog)
        self.databasenm.setGeometry(QtCore.QRect(170, 40, 211, 20))
        self.databasenm.setObjectName("databasenm")
        self.tablenm = QtWidgets.QLineEdit(Dialog)
        self.tablenm.setGeometry(QtCore.QRect(170, 100, 211, 20))
        self.tablenm.setObjectName("tablenm")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(210, 150, 61, 20))
        self.label_4.setObjectName("label_4")
        self.columnmn = QtWidgets.QLineEdit(Dialog)
        self.columnmn.setGeometry(QtCore.QRect(20, 180, 141, 20))
        self.columnmn.setObjectName("columnmn")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(190, 180, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(380, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 230, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.message = QtWidgets.QLabel(Dialog)
        self.message.setGeometry(QtCore.QRect(80, 270, 321, 21))
        self.message.setText("")
        self.message.setObjectName("message")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "enter database name"))
        self.label_2.setText(_translate("Dialog", "enter table name"))
        self.label_3.setText(_translate("Dialog", "column name"))
        self.label_4.setText(_translate("Dialog", "data type"))
        self.comboBox.setItemText(0, _translate("Dialog", "int"))
        self.comboBox.setItemText(1, _translate("Dialog", "text"))
        self.pushButton.setText(_translate("Dialog", "Add column"))
        self.pushButton_2.setText(_translate("Dialog", "create Table"))

