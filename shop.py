# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shop.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 50)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 600, 50))
        self.frame.setStyleSheet("background-color: rgb(196, 129, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_GameName = QtWidgets.QLabel(self.frame)
        self.label_GameName.setGeometry(QtCore.QRect(20, 10, 341, 30))
        self.label_GameName.setText("")
        self.label_GameName.setObjectName("label_GameName")
        self.pushButton_Remove = QtWidgets.QPushButton(self.frame)
        self.pushButton_Remove.setGeometry(QtCore.QRect(450, 15, 120, 20))
        self.pushButton_Remove.setStyleSheet("\n"
"QPushButton {\n"
"         background-color: rgb(92, 138, 0);\n"
"    color: rgb(255, 255, 255);\n"
"     }")
        self.pushButton_Remove.setObjectName("pushButton_Remove")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Remove.setText(_translate("MainWindow", "移除"))