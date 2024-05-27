from LogIn import Ui_LRMainWindow
from testwindow import Ui_testwindow  # 假设testshowmenu.py中定义了Ui_MainWindow类
from PyQt5 import QtCore, QtWidgets
from  PyQt5.QtWidgets import QFrame, QApplication, QMainWindow, QDesktopWidget,  QPushButton
import sys
import pymysql

class LogInWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LRMainWindow()
        self.ui.setupUi(self)

        # 设置窗口无边框及透明背景
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 窗口居中显示
        self.center()

        # 按钮绑定函数
        self.ui.pushButton_LogIn.clicked.connect(lambda: self.ui.stackedWidget_LR.setCurrentIndex(0))
        self.ui.pushButton_userRegister.clicked.connect(lambda: self.ui.stackedWidget_LR.setCurrentIndex(1))
        self.ui.pushButton_manufacturerRegister.clicked.connect(lambda: self.ui.stackedWidget_LR.setCurrentIndex(2))

        # 异常栏初始化
        self.ui.success_error_Type.setCurrentIndex(0)

        # 显示登录界面
        self.show()

        # 登录按钮点击事件
        self.ui.pushButton_L_Sure.clicked.connect(self.log_in)

        #用户注册按钮点击事件
        self.ui.pushButton_User_R_Sure.clicked.connect(self.register_user)

    #居中显示
    def center(self):
        # 窗口居中
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #用户(厂商)登录
    def log_in(self):
        self.ui.success_error_Type.setCurrentIndex(0)
        account_number = self.ui.lineEdit_L_AccountNumber.text()
        password = self.ui.lineEdit_L_Password.text()

        if len(account_number) <= 10:
            try:
                db = pymysql.connect(host="localhost", user="root", password='123456', port=3306, db='game_system')
                cursor = db.cursor()

                cursor.execute("SELECT * FROM user WHERE ACCOUNT_NUMBER = %s", (account_number,))
                flag = cursor.fetchall()

                if not flag:
                    self.ui.success_error_Type.setCurrentIndex(3)  # 没有找到账户
                else:
                    # 确保查询有结果才尝试访问
                    if len(flag) > 0 and password == flag[0][2]:  # 假设密码在查询结果的第3个位置
                        self.ui.success_error_Type.setCurrentIndex(1)
                        self.win = MainUserWindow()
                        self.win.show()
                        self.close()
                    else:
                        self.ui.success_error_Type.setCurrentIndex(3)  # 密码错误
            except pymysql.MySQLError as e:
                print(f"Database Error: {e}")
                self.ui.success_error_Type.setCurrentIndex(3)  # 数据库错误或其他未知错误
            finally:
                db.close()
        else:
            self.ui.success_error_Type.setCurrentIndex(3)  # 账户名长度超过限制

    def register_user(self):
        self.ui.success_error_Type.setCurrentIndex(0)

        new_account_number = self.ui.lineEdit_User_R_AccountNumber.text()
        new_password = self.ui.lineEdit_User_R_Password.text()
        new_check_password = self.ui.lineEdit_User_R_CheckPassword.text()

        # 检查用户名和密码长度
        if len(new_account_number) > 10 or len(new_password) > 20 or len(new_account_number) == 0 or len(
                new_password) == 0:
            self.ui.success_error_Type.setCurrentIndex(4)
            return
        elif new_password != new_check_password:
            self.ui.success_error_Type.setCurrentIndex(6)
            return

        try:
            db = pymysql.connect(host="localhost", user="root", password='123456', port=3306, db='game_system')
            cursor = db.cursor()

            # 防止SQL注入，使用参数化查询
            cursor.execute("SELECT * FROM user WHERE ACCOUNT_NUMBER = %s", (new_account_number,))
            flag = cursor.fetchall()

            if not flag:
                cursor.execute("SELECT COUNT(*) FROM user")
                user_count = int(cursor.fetchone()[0])
                new_user_id = 'U' + str(user_count + 1).zfill(8)
                # 使用参数化查询插入数据
                cursor.execute("INSERT INTO user (ID, ACCOUNT_NUMBER, PASSWORD) VALUES (%s, %s, %s)",
                               (new_user_id, new_account_number, new_password))
                db.commit()  # 提交事务，确保数据被保存
            else:
                self.ui.success_error_Type.setCurrentIndex(5)
        except pymysql.MySQLError as e:
            print(f"Database Error: {e}")
            self.ui.success_error_Type.setCurrentIndex(3)  # 数据库错误或其他未知错误
        finally:
            db.close()


class MainUserWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_testwindow()  # 注意这里是实例化对象
        self.ui.setupUi(self)

        # 设置窗口无边框及透明背景
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 窗口居中
        self.center()

        # 连接数据库
        db = pymysql.connect(host="localhost", user="root", password='123456', port=3306, db='game_system')
        cursor = db.cursor()

        # 查询游戏数量
        cursor.execute("SELECT COUNT(*) FROM game")  # 添加表名'manufacturer'
        game_count = int(cursor.fetchone()[0])

        # 查询所有游戏具体信息
        cursor.execute("SELECT id, introduction, price FROM game")

        # 获取所有游戏具体信息
        all_game = cursor.fetchall()

        # 关闭数据库连接
        db.close()

        x = 207  # 初始化x坐标
        y = 180  # 初始化y坐标

        for i in range(0, game_count):
            self.add_page(x, y, all_game[i][0], all_game[i][1], all_game[i][2])
            y += 160  # 增加x坐标，以便放置下一个页面(150高度，10空隙)
            # if x >= screen.width():  # 如果x坐标超出屏幕宽度，重置x坐标并增加y坐标
            #     x = 0
            #     y += 150

        self.show()

    #居中显示
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

     # 添加到页面上
    #
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
    # 启用高DPI缩放
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    win = LogInWindow()
    sys.exit(app.exec_())