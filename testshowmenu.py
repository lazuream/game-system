from test03 import *
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
import sys
import pymysql

class showWindow(QMainWindow):
    def __init__(self):
        def __init__(self):
            super().__init__()
            self.ui = Ui_MainWindow

            # 设置窗口无边框和透明背景
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

            # 窗口居中
            screen = QDesktopWidget().screenGeometry()  # 获取屏幕大小
            self.top = int((screen.width() - self.width()) / 2)  # 左上角x坐标
            self.left = int((screen.height() - self.height()) / 2)  # 左上角y坐标
            self.setGeometry(self.top, self.left, self.width(), self.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    TheWin = showWindow()
    TheWin.show()
    sys.exit(app.exec_())