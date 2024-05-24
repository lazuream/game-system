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
        cursor.execute("SELECT id, introduction FROM manufacturer")

        # 获取所有制造商的id和简介
        all_manufacturers = cursor.fetchall()

        # 关闭数据库连接
        db.close()

        x = 0  # 初始化x坐标
        y = 0  # 初始化y坐标

        for i in range(0, manufacturers_count):
            self.add_page(x, y, i, all_manufacturers[i][0], all_manufacturers[i][1])
            y += 150  # 增加x坐标，以便放置下一个页面
            # if x >= screen.width():  # 如果x坐标超出屏幕宽度，重置x坐标并增加y坐标
            #     x = 0
            #     y += 150

    # 添加到页面上
    def add_page(self, x, y, i, id, introduction):
        frame = QFrame(parent=self.ui.scrollAreaWidgetContents)  # 显式指定父对象为scroll
        frame.move(x, y)
        frame.setMinimumSize(615, 150)
        frame.setMaximumSize(615, 150)
        frame.setStyleSheet("background-color: rgb(85, 255, 255);")
        frame.setObjectName("frame")
        # 添加一个QLabel到QFrame
        game_button = QPushButton(frame)
        game_button.setText(f"{introduction}")# 显示厂商简介（test)
        game_button.setStyleSheet("color: white; font-size: 24px")
        game_button.setGeometry(0, 0, 615, 150)
        game_button.clicked.connect(lambda: self.game_but_clicked(i))


if __name__ == '__main__':
    # 解决自适应缩放
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    TheWin = TestWindow()
    TheWin.show()
    sys.exit(app.exec_())