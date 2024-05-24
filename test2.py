from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
import sys
import pymysql

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(600, 800)
        self.setWindowTitle('动态添加游戏区')

        self.n_labels = 7

        for i in range(0, self.n_labels):
            self.add_game(0, 0 + 150 * i, i)

    def add_game(self, x, y, i):
        frame = QFrame(parent=self)  # 显式指定父对象为self
        frame.move(x, y)
        frame.setMinimumSize(600, 150)
        frame.setMaximumSize(600, 150)
        frame.setStyleSheet("background-color: rgb(85, 255, 255);")
        frame.setObjectName("frame")

        # 添加一个QLabel到QFrame
        game_button = QPushButton(frame)
        game_button.setText(f"Game {i+1}")
        game_button.setStyleSheet("color: white; font-size: 24px")
        game_button.setGeometry(0, 0, 600, 150)
        game_button.clicked.connect(lambda :self.game_but_clicked(i))

    def game_but_clicked(self, i):
        print(f"game{i + 1}");

if __name__ == '__main__':
    app = QApplication(sys.argv)
    TheWin = Example()
    TheWin.show()
    sys.exit(app.exec_())