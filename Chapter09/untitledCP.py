# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitledCP.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(466, 313)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 131, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 190, 161, 23))
        self.pushButton.setObjectName("pushButton")
        self.message = QtWidgets.QLabel(Dialog)
        self.message.setGeometry(QtCore.QRect(20, 240, 411, 16))
        self.message.setText("")
        self.message.setObjectName("message")
        self.email = QtWidgets.QLineEdit(Dialog)
        self.email.setGeometry(QtCore.QRect(160, 20, 251, 20))
        self.email.setObjectName("email")
        self.oldpasswd = QtWidgets.QLineEdit(Dialog)
        self.oldpasswd.setGeometry(QtCore.QRect(160, 70, 251, 20))
        self.oldpasswd.setObjectName("oldpasswd")
        self.newpassword = QtWidgets.QLineEdit(Dialog)
        self.newpassword.setGeometry(QtCore.QRect(160, 110, 251, 20))
        self.newpassword.setObjectName("newpassword")
        self.renewpasswd = QtWidgets.QLineEdit(Dialog)
        self.renewpasswd.setGeometry(QtCore.QRect(160, 150, 251, 20))
        self.renewpasswd.setObjectName("renewpasswd")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "email"))
        self.label_2.setText(_translate("Dialog", "old password"))
        self.label_3.setText(_translate("Dialog", "new password"))
        self.label_4.setText(_translate("Dialog", "re-enter new password"))
        self.pushButton.setText(_translate("Dialog", "change password"))

