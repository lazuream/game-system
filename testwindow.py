# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_testwindow(object):
    def setupUi(self, testwindow):
        testwindow.setObjectName("testwindow")
        testwindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(testwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.background.setMinimumSize(QtCore.QSize(801, 571))
        self.background.setStyleSheet("#background{\n"
"border-radius:7px;\n"
"background-color: rgb(38, 38, 38);\n"
"}")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.background)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu = QtWidgets.QFrame(self.background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.verticalLayout.addWidget(self.menu)
        self.main = QtWidgets.QFrame(self.background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setStyleSheet("background-color: rgb(59, 59, 89);")
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget_Window = QtWidgets.QStackedWidget(self.main)
        self.stackedWidget_Window.setObjectName("stackedWidget_Window")
        self.page_MainWindow = QtWidgets.QWidget()
        self.page_MainWindow.setObjectName("page_MainWindow")
        self.scrollArea = QtWidgets.QScrollArea(self.page_MainWindow)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1022, 640))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(781, 454))
        self.scrollArea.setStyleSheet("QProgressBar{\n"
"background-color: white; \n"
"border: 1px solid black;\n"
"}")
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1007, 1000))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(766, 0))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1011, 171))
        self.frame_3.setMinimumSize(QtCore.QSize(771, 120))
        self.frame_3.setStyleSheet("background-color: rgb(101, 222, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setGeometry(QtCore.QRect(290, 10, 661, 41))
        self.frame.setStyleSheet("#frame{\n"
"background-color: rgb(59, 59, 89,0.2);\n"
"border-radius:15px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_SearchGame = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_SearchGame.setGeometry(QtCore.QRect(470, 10, 160, 20))
        self.lineEdit_SearchGame.setStyleSheet("background-color: rgba(255, 255, 255, 0.2);\n"
"    border: none;")
        self.lineEdit_SearchGame.setObjectName("lineEdit_SearchGame")
        self.pushButton_SearchGame = QtWidgets.QPushButton(self.frame)
        self.pushButton_SearchGame.setGeometry(QtCore.QRect(590, 10, 40, 20))
        self.pushButton_SearchGame.setStyleSheet("background-color: rgb(255, 255, 255，0);\n"
"border:none")
        self.pushButton_SearchGame.setText("")
        self.pushButton_SearchGame.setObjectName("pushButton_SearchGame")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget_Window.addWidget(self.page_MainWindow)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_4)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 0, 1022, 640))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(781, 454))
        self.scrollArea_2.setStyleSheet("QProgressBar{\n"
"background-color: white; \n"
"border: 1px solid black;\n"
"}")
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1007, 1000))
        self.scrollAreaWidgetContents_3.setMinimumSize(QtCore.QSize(766, 0))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1011, 171))
        self.frame_4.setMinimumSize(QtCore.QSize(771, 120))
        self.frame_4.setStyleSheet("background-color: rgb(101, 222, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setGeometry(QtCore.QRect(290, 10, 661, 41))
        self.frame_2.setStyleSheet("#frame{\n"
"background-color: rgb(59, 59, 89,0.2);\n"
"border-radius:15px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit_SearchGame_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_SearchGame_2.setGeometry(QtCore.QRect(470, 10, 160, 20))
        self.lineEdit_SearchGame_2.setStyleSheet("background-color: rgba(255, 255, 255, 0.2);\n"
"    border: none;")
        self.lineEdit_SearchGame_2.setObjectName("lineEdit_SearchGame_2")
        self.pushButton_SearchGame_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_SearchGame_2.setGeometry(QtCore.QRect(590, 10, 40, 20))
        self.pushButton_SearchGame_2.setStyleSheet("background-color: rgb(255, 255, 255，0);\n"
"border:none")
        self.pushButton_SearchGame_2.setText("")
        self.pushButton_SearchGame_2.setObjectName("pushButton_SearchGame_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.stackedWidget_Window.addWidget(self.page_4)
        self.horizontalLayout.addWidget(self.stackedWidget_Window)
        self.verticalLayout.addWidget(self.main)
        self.menu_2 = QtWidgets.QFrame(self.background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.menu_2.sizePolicy().hasHeightForWidth())
        self.menu_2.setSizePolicy(sizePolicy)
        self.menu_2.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.menu_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_2.setObjectName("menu_2")
        self.verticalLayout.addWidget(self.menu_2)
        testwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(testwindow)
        self.statusbar.setObjectName("statusbar")
        testwindow.setStatusBar(self.statusbar)

        self.retranslateUi(testwindow)
        self.stackedWidget_Window.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(testwindow)

    def retranslateUi(self, testwindow):
        _translate = QtCore.QCoreApplication.translate
        testwindow.setWindowTitle(_translate("testwindow", "MainWindow"))
        self.lineEdit_SearchGame.setPlaceholderText(_translate("testwindow", "搜索"))
        self.lineEdit_SearchGame_2.setPlaceholderText(_translate("testwindow", "搜索"))
import resgame_system_rc
