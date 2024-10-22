from test03 import *
import webbrowser
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QWidget, QLabel, QPushButton
import sys
import pymysql


class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 初始化UI布局

        # 设置窗口无边框和透明背景
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 窗口居中
        screen = QDesktopWidget().screenGeometry()  # 获取屏幕大小
        self.top = int((screen.width() - self.width()) / 2)  # 左上角x坐标
        self.left = int((screen.height() - self.height()) / 2)  # 左上角y坐标
        self.setGeometry(self.top, self.left, self.width(), self.height())
        # 连接数据库
        db = pymysql.connect(host="localhost", user="root", password='123456', port=3306, db='game_system')
        cursor = db.cursor()

        # 查询厂商数量
        cursor.execute("SELECT COUNT(*) FROM manufacturer")  # 添加表名'manufacturer'
        manufacturers_count = int(cursor.fetchone()[0])

        # 查询所有制造商
        cursor.execute("SELECT id, introduction, price FROM game")

        # 获取所有制造商的id和简介
        all_manufacturers = cursor.fetchall()

        # 关闭数据库连接
        db.close()

        x = 0  # 初始化x坐标
        y = 0  # 初始化y坐标

        for i in range(0, manufacturers_count):
            self.add_page(x, y , all_manufacturers[i][0], all_manufacturers[i][1], all_manufacturers[i][2])
            y += 150  # 增加x坐标，以便放置下一个页面
            # if x >= screen.width():  # 如果x坐标超出屏幕宽度，重置x坐标并增加y坐标
            #     x = 0
            #     y += 150

    # 添加到页面上
    def add_page(self, x, y,  id, introduction, cost):
        frame = QFrame(parent=self.ui.scrollAreaWidgetContents)  # 显式指定父对象为scroll
        frame.move(x, y)
        frame.setMinimumSize(615, 150)
        frame.setMaximumSize(615, 150)
        frame.setStyleSheet("background-color: rgb(59, 59, 89);")
        frame.setObjectName("Frame")

        layoutWidget = QtWidgets.QWidget(frame)
        layoutWidget.setGeometry(QtCore.QRect(0, 0, 615, 150))
        layoutWidget.setObjectName("layoutWidget")

        game_frame = QtWidgets.QVBoxLayout(layoutWidget)
        game_frame.setContentsMargins(3, 3, 3, 3)
        game_frame.setObjectName("Frame_Game")

        #游戏名称栏
        Game_Name = QtWidgets.QLabel(layoutWidget)
        Game_Name.setMouseTracking(True)
        Game_Name.setStyleSheet("QWidget {\n"
                                     "    background-color: rgb(255, 255, 255,20);\n"
                                     "    font: 15pt \"微软雅黑\";\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "     }\n"
                                     "")
        Game_Name.setText(f"{id}")
        Game_Name.setObjectName("Game_Name")
        game_frame.addWidget(Game_Name)

        #游戏简介栏
        Game_Introduction = QtWidgets.QPlainTextEdit(layoutWidget)
        Game_Introduction.setStyleSheet("background-color: rgb(255, 255, 255,20);\n"
                                  "font: 10pt \"微软雅黑\";\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "border:none;")
        Game_Introduction.setLineWidth(-1)
        Game_Introduction.setPlainText(f"{introduction}")
        Game_Introduction.setObjectName("Game_I")
        game_frame.addWidget(Game_Introduction)

        #功能栏
        horizontalLayout_2 = QtWidgets.QHBoxLayout()
        horizontalLayout_2.setObjectName("horizontalLayout_2")

        pushButton_2 = QtWidgets.QPushButton(layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pushButton_2.sizePolicy().hasHeightForWidth())
        pushButton_2.setSizePolicy(sizePolicy)
        pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(229, 255, 255);\n"
                                        "background-color: rgba(255, 255, 255, 50); \n"
                                        "     }")
        pushButton_2.setText("")
        pushButton_2.setObjectName("pushButton_2")
        horizontalLayout_2.addWidget(pushButton_2)

        pushButton_3 = QtWidgets.QPushButton(layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pushButton_3.sizePolicy().hasHeightForWidth())
        pushButton_3.setSizePolicy(sizePolicy)
        pushButton_3.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(229, 255, 255);\n"
                                        "background-color: rgba(255, 255, 255, 50); \n"
                                        "     }")
        pushButton_3.setText("")
        pushButton_3.setObjectName("pushButton_3")
        horizontalLayout_2.addWidget(pushButton_3)

        pushButton_4 = QtWidgets.QPushButton(layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pushButton_4.sizePolicy().hasHeightForWidth())
        pushButton_4.setSizePolicy(sizePolicy)
        pushButton_4.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(229, 255, 255);\n"
                                        "background-color: rgba(255, 255, 255, 50); \n"
                                        "     }")
        pushButton_4.setText("")
        pushButton_4.setObjectName("pushButton_4")
        horizontalLayout_2.addWidget(pushButton_4)

        label_6 = QtWidgets.QLabel(layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label_6.sizePolicy().hasHeightForWidth())
        label_6.setSizePolicy(sizePolicy)
        label_6.setStyleSheet("font: 9pt \"黑体\";\n"
                                   "color:rgb(255, 255, 255);\n"
                                   "")
        label_6.setText(f"{cost}")
        label_6.setWordWrap(False)
        label_6.setObjectName("label_6")
        horizontalLayout_2.addWidget(label_6)

        pushButton = QtWidgets.QPushButton(layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pushButton.sizePolicy().hasHeightForWidth())
        pushButton.setSizePolicy(sizePolicy)
        pushButton.setStyleSheet("QPushButton {\n"
                                      "         background-color: rgb(92, 138, 0);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "     }")
        pushButton.setText("加入购物车")
        pushButton.setObjectName("pushButton")
        horizontalLayout_2.addWidget(pushButton)

        game_frame.addLayout(horizontalLayout_2)


if __name__ == '__main__':
    # 解决自适应缩放
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    TheWin = TestWindow()
    TheWin.show()
    sys.exit(app.exec_())