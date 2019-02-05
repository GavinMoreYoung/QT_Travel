# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitledMLI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(268, 333)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 71, 16))
        self.label_4.setObjectName("label_4")
        self.lesc = QtWidgets.QLineEdit(Dialog)
        self.lesc.setGeometry(QtCore.QRect(120, 30, 113, 20))
        self.lesc.setObjectName("lesc")
        self.lesn = QtWidgets.QLineEdit(Dialog)
        self.lesn.setGeometry(QtCore.QRect(120, 70, 113, 20))
        self.lesn.setObjectName("lesn")
        self.leem = QtWidgets.QLineEdit(Dialog)
        self.leem.setGeometry(QtCore.QRect(120, 110, 113, 20))
        self.leem.setObjectName("leem")
        self.lemm = QtWidgets.QLineEdit(Dialog)
        self.lemm.setGeometry(QtCore.QRect(120, 150, 113, 20))
        self.lemm.setObjectName("lemm")
        self.total = QtWidgets.QLineEdit(Dialog)
        self.total.setEnabled(False)
        self.total.setGeometry(QtCore.QRect(120, 200, 113, 20))
        self.total.setObjectName("total")
        self.percentage = QtWidgets.QLineEdit(Dialog)
        self.percentage.setEnabled(False)
        self.percentage.setGeometry(QtCore.QRect(120, 250, 113, 20))
        self.percentage.setObjectName("percentage")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 250, 71, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 290, 75, 23))
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
        self.label_5.setText(_translate("Dialog", "tatal"))
        self.label_6.setText(_translate("Dialog", "percentage"))
        self.pushButton.setText(_translate("Dialog", "click"))

