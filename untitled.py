# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(730, 283)
        Dialog.setStyleSheet("background-color: rgb(59, 59, 89);")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 711, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.game_frame = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.game_frame.setContentsMargins(3, 3, 3, 3)
        self.game_frame.setObjectName("game_frame")
        self.Game_Name = QtWidgets.QLabel(self.layoutWidget)
        self.Game_Name.setMouseTracking(True)
        self.Game_Name.setStyleSheet("QWidget {\n"
"    background-color: rgb(255, 255, 255,20);\n"
"    font: 15pt \"微软雅黑\";\n"
"    color: rgb(255, 255, 255);\n"
"     }\n"
"")
        self.Game_Name.setText("")
        self.Game_Name.setObjectName("Game_Name")
        self.game_frame.addWidget(self.Game_Name)
        self.Game_I = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.Game_I.setStyleSheet("background-color: rgb(255, 255, 255,20);\n"
"font: 10pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.Game_I.setLineWidth(-1)
        self.Game_I.setPlainText("")
        self.Game_I.setObjectName("Game_I")
        self.game_frame.addWidget(self.Game_I)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: rgb(229, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50); \n"
"     }")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    color: rgb(229, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50); \n"
"     }")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    color: rgb(229, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50); \n"
"     }")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet("font: 9pt \"黑体\";\n"
"color:rgb(255, 255, 255);\n"
"")
        self.label_6.setText("")
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("QPushButton {\n"
"         background-color: rgb(92, 138, 0);\n"
"    color: rgb(255, 255, 255);\n"
"     }")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.game_frame.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "添加至购物车"))
