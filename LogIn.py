# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogIn.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LRMainWindow(object):
    def setupUi(self, LRMainWindow):
        LRMainWindow.setObjectName("LRMainWindow")
        LRMainWindow.resize(581, 351)
        self.centralwidget = QtWidgets.QWidget(LRMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 581, 351))
        self.frame.setStyleSheet("#frame{\n"
"border-radius:7px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0.293785, y1:0, x2:0, y2:1, stop:0 rgba(209, 171, 200, 255), stop:1 rgba(161, 234, 241, 255));\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_Exit = QtWidgets.QPushButton(self.frame)
        self.pushButton_Exit.setGeometry(QtCore.QRect(551, 10, 20, 20))
        self.pushButton_Exit.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:2px;\n"
"}\n"
"#exitButton:hover{\n"
"    padding-bottom:1px;\n"
"}\n"
"")
        self.pushButton_Exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/u=1232580825,2848435856&fm=253&app=138&size=w931&n=0&f=JPEG&fmt=auto.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Exit.setIcon(icon)
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.mainLogIn = QtWidgets.QFrame(self.frame)
        self.mainLogIn.setGeometry(QtCore.QRect(310, 30, 231, 311))
        self.mainLogIn.setMinimumSize(QtCore.QSize(231, 311))
        self.mainLogIn.setStyleSheet("#mainLogIn{\n"
"background-color: rgb(255, 255, 255,0.4);\n"
"border-radius:15px;\n"
"}")
        self.mainLogIn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainLogIn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainLogIn.setObjectName("mainLogIn")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainLogIn)
        self.verticalLayout.setContentsMargins(1, 8, 1, 8)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.mainLogIn)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget_LR = QtWidgets.QStackedWidget(self.frame_5)
        self.stackedWidget_LR.setStyleSheet("QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    border-bottom: 1px solid white;\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(0，0，0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"}\n"
"QpushButton:pressed{\n"
"    paddling-top 2px;\n"
"}\n"
"#lineEdit_Empty{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"}\n"
"#lineEdit_Empty_2{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"}")
        self.stackedWidget_LR.setObjectName("stackedWidget_LR")
        self.page_UserLogin = QtWidgets.QWidget()
        self.page_UserLogin.setObjectName("page_UserLogin")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_UserLogin)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_UserState = QtWidgets.QLabel(self.page_UserLogin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.label_UserState.sizePolicy().hasHeightForWidth())
        self.label_UserState.setSizePolicy(sizePolicy)
        self.label_UserState.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"楷体\";")
        self.label_UserState.setObjectName("label_UserState")
        self.verticalLayout_6.addWidget(self.label_UserState)
        self.lineEdit_L_AccountNumber = QtWidgets.QLineEdit(self.page_UserLogin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_L_AccountNumber.sizePolicy().hasHeightForWidth())
        self.lineEdit_L_AccountNumber.setSizePolicy(sizePolicy)
        self.lineEdit_L_AccountNumber.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_L_AccountNumber.setObjectName("lineEdit_L_AccountNumber")
        self.verticalLayout_6.addWidget(self.lineEdit_L_AccountNumber)
        self.lineEdit_L_Password = QtWidgets.QLineEdit(self.page_UserLogin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_L_Password.sizePolicy().hasHeightForWidth())
        self.lineEdit_L_Password.setSizePolicy(sizePolicy)
        self.lineEdit_L_Password.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_L_Password.setText("")
        self.lineEdit_L_Password.setObjectName("lineEdit_L_Password")
        self.verticalLayout_6.addWidget(self.lineEdit_L_Password)
        self.pushButton_L_Sure = QtWidgets.QPushButton(self.page_UserLogin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_L_Sure.sizePolicy().hasHeightForWidth())
        self.pushButton_L_Sure.setSizePolicy(sizePolicy)
        self.pushButton_L_Sure.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_L_Sure.setStyleSheet("QPushButton{\n"
"    font: 14pt \"Eras Bold ITC\";\n"
"    background-colour:rgb(255, 255, 255);\n"
"    colour:rgb(0, 0, 0);\n"
"    border-radius:7px;\n"
"}\n"
"QpushButton:pressed{\n"
"    paddling-top 2px;\n"
"}")
        self.pushButton_L_Sure.setObjectName("pushButton_L_Sure")
        self.verticalLayout_6.addWidget(self.pushButton_L_Sure)
        self.stackedWidget_LR.addWidget(self.page_UserLogin)
        self.page_manufacturerLogin = QtWidgets.QWidget()
        self.page_manufacturerLogin.setObjectName("page_manufacturerLogin")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_manufacturerLogin)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_manufacturerState = QtWidgets.QLabel(self.page_manufacturerLogin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.label_manufacturerState.sizePolicy().hasHeightForWidth())
        self.label_manufacturerState.setSizePolicy(sizePolicy)
        self.label_manufacturerState.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"楷体\";")
        self.label_manufacturerState.setObjectName("label_manufacturerState")
        self.verticalLayout_13.addWidget(self.label_manufacturerState)
        self.lineEdit_L_AccountNumber_manufacture = QtWidgets.QLineEdit(self.page_manufacturerLogin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_L_AccountNumber_manufacture.sizePolicy().hasHeightForWidth())
        self.lineEdit_L_AccountNumber_manufacture.setSizePolicy(sizePolicy)
        self.lineEdit_L_AccountNumber_manufacture.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_L_AccountNumber_manufacture.setObjectName("lineEdit_L_AccountNumber_manufacture")
        self.verticalLayout_13.addWidget(self.lineEdit_L_AccountNumber_manufacture)
        self.lineEdit_L_Password_manufacturer = QtWidgets.QLineEdit(self.page_manufacturerLogin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_L_Password_manufacturer.sizePolicy().hasHeightForWidth())
        self.lineEdit_L_Password_manufacturer.setSizePolicy(sizePolicy)
        self.lineEdit_L_Password_manufacturer.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_L_Password_manufacturer.setText("")
        self.lineEdit_L_Password_manufacturer.setObjectName("lineEdit_L_Password_manufacturer")
        self.verticalLayout_13.addWidget(self.lineEdit_L_Password_manufacturer)
        self.pushButton_L_Sure_manufacturer = QtWidgets.QPushButton(self.page_manufacturerLogin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_L_Sure_manufacturer.sizePolicy().hasHeightForWidth())
        self.pushButton_L_Sure_manufacturer.setSizePolicy(sizePolicy)
        self.pushButton_L_Sure_manufacturer.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_L_Sure_manufacturer.setStyleSheet("QPushButton{\n"
"    font: 14pt \"Eras Bold ITC\";\n"
"    background-colour:rgb(255, 255, 255);\n"
"    colour:rgb(0, 0, 0);\n"
"    border-radius:7px;\n"
"}\n"
"QpushButton:pressed{\n"
"    paddling-top 2px;\n"
"}")
        self.pushButton_L_Sure_manufacturer.setObjectName("pushButton_L_Sure_manufacturer")
        self.verticalLayout_13.addWidget(self.pushButton_L_Sure_manufacturer)
        self.stackedWidget_LR.addWidget(self.page_manufacturerLogin)
        self.page_userRegister = QtWidgets.QWidget()
        self.page_userRegister.setObjectName("page_userRegister")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_userRegister)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_UserState_2 = QtWidgets.QLabel(self.page_userRegister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.label_UserState_2.sizePolicy().hasHeightForWidth())
        self.label_UserState_2.setSizePolicy(sizePolicy)
        self.label_UserState_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"楷体\";")
        self.label_UserState_2.setObjectName("label_UserState_2")
        self.verticalLayout_8.addWidget(self.label_UserState_2)
        self.lineEdit_User_R_AccountNumber = QtWidgets.QLineEdit(self.page_userRegister)
        self.lineEdit_User_R_AccountNumber.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_User_R_AccountNumber.setText("")
        self.lineEdit_User_R_AccountNumber.setObjectName("lineEdit_User_R_AccountNumber")
        self.verticalLayout_8.addWidget(self.lineEdit_User_R_AccountNumber)
        self.lineEdit_User_R_Password = QtWidgets.QLineEdit(self.page_userRegister)
        self.lineEdit_User_R_Password.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_User_R_Password.setText("")
        self.lineEdit_User_R_Password.setObjectName("lineEdit_User_R_Password")
        self.verticalLayout_8.addWidget(self.lineEdit_User_R_Password)
        self.lineEdit_User_R_CheckPassword = QtWidgets.QLineEdit(self.page_userRegister)
        self.lineEdit_User_R_CheckPassword.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_User_R_CheckPassword.setObjectName("lineEdit_User_R_CheckPassword")
        self.verticalLayout_8.addWidget(self.lineEdit_User_R_CheckPassword)
        self.pushButton_User_R_Sure = QtWidgets.QPushButton(self.page_userRegister)
        self.pushButton_User_R_Sure.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_User_R_Sure.setStyleSheet("QPushButton{\n"
"    font: 14pt \"Eras Bold ITC\";\n"
"    background-colour:rgb(0, 0, 0);\n"
"    colour:rgb(25,255,255);\n"
"    border-radius:7px;\n"
"}\n"
"QpushButton:pressed{\n"
"    paddling-top 2px;\n"
"}")
        self.pushButton_User_R_Sure.setObjectName("pushButton_User_R_Sure")
        self.verticalLayout_8.addWidget(self.pushButton_User_R_Sure)
        self.stackedWidget_LR.addWidget(self.page_userRegister)
        self.page_manufacturerRregister = QtWidgets.QWidget()
        self.page_manufacturerRregister.setObjectName("page_manufacturerRregister")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_manufacturerRregister)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_UserState_4 = QtWidgets.QLabel(self.page_manufacturerRregister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.label_UserState_4.sizePolicy().hasHeightForWidth())
        self.label_UserState_4.setSizePolicy(sizePolicy)
        self.label_UserState_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"楷体\";")
        self.label_UserState_4.setObjectName("label_UserState_4")
        self.verticalLayout_12.addWidget(self.label_UserState_4)
        self.lineEdit_Manufacturer_R_AccountNumber = QtWidgets.QLineEdit(self.page_manufacturerRregister)
        self.lineEdit_Manufacturer_R_AccountNumber.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_Manufacturer_R_AccountNumber.setText("")
        self.lineEdit_Manufacturer_R_AccountNumber.setObjectName("lineEdit_Manufacturer_R_AccountNumber")
        self.verticalLayout_12.addWidget(self.lineEdit_Manufacturer_R_AccountNumber)
        self.lineEdit_Manufacturer_R_Password = QtWidgets.QLineEdit(self.page_manufacturerRregister)
        self.lineEdit_Manufacturer_R_Password.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_Manufacturer_R_Password.setText("")
        self.lineEdit_Manufacturer_R_Password.setObjectName("lineEdit_Manufacturer_R_Password")
        self.verticalLayout_12.addWidget(self.lineEdit_Manufacturer_R_Password)
        self.lineEdit_Manufacturer_R_CheckPassword = QtWidgets.QLineEdit(self.page_manufacturerRregister)
        self.lineEdit_Manufacturer_R_CheckPassword.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_Manufacturer_R_CheckPassword.setObjectName("lineEdit_Manufacturer_R_CheckPassword")
        self.verticalLayout_12.addWidget(self.lineEdit_Manufacturer_R_CheckPassword)
        self.pushButton_Manufacturer_R_Sure = QtWidgets.QPushButton(self.page_manufacturerRregister)
        self.pushButton_Manufacturer_R_Sure.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_Manufacturer_R_Sure.setStyleSheet("QPushButton{\n"
"    font: 14pt \"Eras Bold ITC\";\n"
"    background-colour:rgb(0, 0, 0);\n"
"    colour:rgb(25,255,255);\n"
"    border-radius:7px;\n"
"}\n"
"QpushButton:pressed{\n"
"    paddling-top 2px;\n"
"}")
        self.pushButton_Manufacturer_R_Sure.setObjectName("pushButton_Manufacturer_R_Sure")
        self.verticalLayout_12.addWidget(self.pushButton_Manufacturer_R_Sure)
        self.stackedWidget_LR.addWidget(self.page_manufacturerRregister)
        self.verticalLayout_5.addWidget(self.stackedWidget_LR)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_LogIn = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_LogIn.sizePolicy().hasHeightForWidth())
        self.pushButton_LogIn.setSizePolicy(sizePolicy)
        self.pushButton_LogIn.setMinimumSize(QtCore.QSize(105, 0))
        self.pushButton_LogIn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:2px;\n"
"}")
        self.pushButton_LogIn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/u=157358869,2307745509&fm=217&app=126&size=f242,150&n=0&f=PNG.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_LogIn.setIcon(icon1)
        self.pushButton_LogIn.setObjectName("pushButton_LogIn")
        self.horizontalLayout.addWidget(self.pushButton_LogIn)
        self.pushButton_Register = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Register.sizePolicy().hasHeightForWidth())
        self.pushButton_Register.setSizePolicy(sizePolicy)
        self.pushButton_Register.setMinimumSize(QtCore.QSize(105, 0))
        self.pushButton_Register.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:2px;\n"
"}")
        self.pushButton_Register.setText("")
        self.pushButton_Register.setIcon(icon1)
        self.pushButton_Register.setObjectName("pushButton_Register")
        self.horizontalLayout.addWidget(self.pushButton_Register)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.success_error_Type = QtWidgets.QStackedWidget(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.success_error_Type.sizePolicy().hasHeightForWidth())
        self.success_error_Type.setSizePolicy(sizePolicy)
        self.success_error_Type.setStyleSheet("#successLogIn{\n"
"}\n"
"#successRegister{\n"
"}\n"
"#sizeWrong{\n"
"    color: rgb(190, 0, 0);\n"
"}\n"
"#userNameWrong{\n"
"    color: rgb(190, 0, 0);\n"
"}\n"
"#passwordWrong{\n"
"    color: rgb(190, 0, 0);\n"
"}\n"
"#logInWrong{\n"
"    color: rgb(190, 0, 0);\n"
"}")
        self.success_error_Type.setObjectName("success_error_Type")
        self.emptyPage = QtWidgets.QWidget()
        self.emptyPage.setObjectName("emptyPage")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.emptyPage)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.success_error_Type.addWidget(self.emptyPage)
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.gridLayout = QtWidgets.QGridLayout(self.page1)
        self.gridLayout.setObjectName("gridLayout")
        self.successLogIn = QtWidgets.QLabel(self.page1)
        self.successLogIn.setStyleSheet("#userNameWrong_1{\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.successLogIn.setObjectName("successLogIn")
        self.gridLayout.addWidget(self.successLogIn, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.success_error_Type.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.successRegister = QtWidgets.QLabel(self.page2)
        self.successRegister.setStyleSheet("#userNameWrong_1{\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.successRegister.setObjectName("successRegister")
        self.horizontalLayout_3.addWidget(self.successRegister, 0, QtCore.Qt.AlignHCenter)
        self.success_error_Type.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.logInWrong = QtWidgets.QLabel(self.page3)
        self.logInWrong.setStyleSheet("#userNameWrong_1{\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.logInWrong.setObjectName("logInWrong")
        self.verticalLayout_7.addWidget(self.logInWrong, 0, QtCore.Qt.AlignHCenter)
        self.success_error_Type.addWidget(self.page3)
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.sizeWrong = QtWidgets.QLabel(self.page4)
        self.sizeWrong.setStyleSheet("#userNameWrong_1{\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.sizeWrong.setObjectName("sizeWrong")
        self.verticalLayout_9.addWidget(self.sizeWrong, 0, QtCore.Qt.AlignHCenter)
        self.success_error_Type.addWidget(self.page4)
        self.page5 = QtWidgets.QWidget()
        self.page5.setObjectName("page5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.userNameWrong = QtWidgets.QLabel(self.page5)
        self.userNameWrong.setStyleSheet("#userNameWrong_1{\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.userNameWrong.setObjectName("userNameWrong")
        self.verticalLayout_10.addWidget(self.userNameWrong, 0, QtCore.Qt.AlignHCenter)
        self.success_error_Type.addWidget(self.page5)
        self.page6 = QtWidgets.QWidget()
        self.page6.setObjectName("page6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.passwordWrong = QtWidgets.QLabel(self.page6)
        self.passwordWrong.setStyleSheet("#userNameWrong_1{\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.passwordWrong.setObjectName("passwordWrong")
        self.verticalLayout_11.addWidget(self.passwordWrong, 0, QtCore.Qt.AlignHCenter)
        self.success_error_Type.addWidget(self.page6)
        self.verticalLayout_3.addWidget(self.success_error_Type)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        self.pushButton_switch = QtWidgets.QPushButton(self.frame)
        self.pushButton_switch.setGeometry(QtCore.QRect(20, 20, 30, 30))
        self.pushButton_switch.setStyleSheet("border-radius: 15px;")
        self.pushButton_switch.setText("")
        self.pushButton_switch.setIcon(icon1)
        self.pushButton_switch.setIconSize(QtCore.QSize(30, 330))
        self.pushButton_switch.setObjectName("pushButton_switch")
        LRMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LRMainWindow)
        self.stackedWidget_LR.setCurrentIndex(0)
        self.success_error_Type.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LRMainWindow)

    def retranslateUi(self, LRMainWindow):
        _translate = QtCore.QCoreApplication.translate
        LRMainWindow.setWindowTitle(_translate("LRMainWindow", "MainWindow"))
        self.label_UserState.setText(_translate("LRMainWindow", "用户登录"))
        self.lineEdit_L_AccountNumber.setPlaceholderText(_translate("LRMainWindow", "账号："))
        self.lineEdit_L_Password.setPlaceholderText(_translate("LRMainWindow", "密码："))
        self.pushButton_L_Sure.setText(_translate("LRMainWindow", "Log   In"))
        self.label_manufacturerState.setText(_translate("LRMainWindow", "厂商登录"))
        self.lineEdit_L_AccountNumber_manufacture.setPlaceholderText(_translate("LRMainWindow", "账号："))
        self.lineEdit_L_Password_manufacturer.setPlaceholderText(_translate("LRMainWindow", "密码："))
        self.pushButton_L_Sure_manufacturer.setText(_translate("LRMainWindow", "Log   In"))
        self.label_UserState_2.setText(_translate("LRMainWindow", "用户注册"))
        self.lineEdit_User_R_AccountNumber.setPlaceholderText(_translate("LRMainWindow", "账号（长度小于16)："))
        self.lineEdit_User_R_Password.setPlaceholderText(_translate("LRMainWindow", "密码："))
        self.lineEdit_User_R_CheckPassword.setPlaceholderText(_translate("LRMainWindow", "确认密码："))
        self.pushButton_User_R_Sure.setText(_translate("LRMainWindow", "Register"))
        self.label_UserState_4.setText(_translate("LRMainWindow", "厂商注册"))
        self.lineEdit_Manufacturer_R_AccountNumber.setPlaceholderText(_translate("LRMainWindow", "账号（长度大于16）："))
        self.lineEdit_Manufacturer_R_Password.setPlaceholderText(_translate("LRMainWindow", "密码："))
        self.lineEdit_Manufacturer_R_CheckPassword.setPlaceholderText(_translate("LRMainWindow", "确认密码："))
        self.pushButton_Manufacturer_R_Sure.setText(_translate("LRMainWindow", "Register"))
        self.successLogIn.setText(_translate("LRMainWindow", " 登陆成功"))
        self.successRegister.setText(_translate("LRMainWindow", " 注册成功"))
        self.logInWrong.setText(_translate("LRMainWindow", "用户名或密码错误"))
        self.sizeWrong.setText(_translate("LRMainWindow", "用户名或密码长度不符合要求"))
        self.userNameWrong.setText(_translate("LRMainWindow", "该用户名已存在"))
        self.passwordWrong.setText(_translate("LRMainWindow", "两次输入密码不一致"))
import resgame_system_rc
