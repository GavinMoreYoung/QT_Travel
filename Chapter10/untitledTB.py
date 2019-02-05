# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitledTB.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 338)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actioncircle = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Graphics/circleIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncircle.setIcon(icon)
        self.actioncircle.setObjectName("actioncircle")
        self.actionrectangle = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Graphics/rectangleIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionrectangle.setIcon(icon1)
        self.actionrectangle.setObjectName("actionrectangle")
        self.actionline = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Graphics/lineIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionline.setIcon(icon2)
        self.actionline.setObjectName("actionline")
        self.toolBar.addAction(self.actioncircle)
        self.toolBar.addAction(self.actionrectangle)
        self.toolBar.addAction(self.actionline)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actioncircle.setText(_translate("MainWindow", "circle"))
        self.actioncircle.setToolTip(_translate("MainWindow", "draw circle"))
        self.actioncircle.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionrectangle.setText(_translate("MainWindow", "rectangle"))
        self.actionline.setText(_translate("MainWindow", "line"))

import iconresource_rc
