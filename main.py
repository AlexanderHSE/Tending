import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_main_stacked import Ui_MainWindow
from ui_main import Ui_MainWindowBase

from ui_functions import *

# APP STATES

STATE_LOGIN = 0
STATE_MAIN = 1


class CLoginState:
    def __init__(self):
        super(CLoginState, self).__init__()
        self.login = LogWindow()

    def start(self):
        self.login.show()


class CMainState:
    def __init__(self):
        super(CMainState, self).__init__()
        self.work_win = MainWindow()

    def start(self):
        self.work_win.show()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.uiMain = Ui_MainWindowBase()
        self.uiMain.setupUi(self)

        self.uiMain.to_login.clicked.connect(self.btn_to_login)

    def btn_to_login(self):
        app.procNextState(STATE_LOGIN)


class LogWindow(QMainWindow):
    def __init__(self):
        QFontDatabase.addApplicationFont('Ubuntu-Regular.ttf')
        QMainWindow.__init__(self)
        self.dragPos = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_show_password_2.clicked.connect(self.toggleVisibility)

        # Move Window
        def moveWindow(event):
            # If left click - move window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # Set title bar
        self.ui.title_bar_2.mouseMoveEvent = moveWindow

        UIFunctions.uiDefinitions(self)

        # Смена окон в MainWindow Login

        # Login Window
        self.ui.btn_signin_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_reg))

        # Registration Window
        self.ui.btn_signin_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_login))

        # Переход к окну программы с метриками
        self.ui.btn_signin_3.clicked.connect(self.btn_to_main_clicked)
        self.ui.btn_signin_5.clicked.connect(self.btn_to_main_clicked)

        # Закрытие окна
        self.ui.btn_signin_3.clicked.connect(self.close)
        self.ui.btn_signin_5.clicked.connect(self.close)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # Изменение видимости пароля
    def toggleVisibility(self):
        if self.ui.edit_password_2.echoMode() == QLineEdit.Normal:
            self.ui.edit_password_2.setEchoMode(QLineEdit.Password)
            new_icon = QPixmap('closedEyeChanged.png')
            self.ui.btn_show_password_2.setIcon(QIcon(new_icon))
        else:
            self.ui.edit_password_2.setEchoMode(QLineEdit.Normal)
            new_icon = QPixmap('openedEye.png')
            self.ui.btn_show_password_2.setIcon(QIcon(new_icon))

    def btn_to_main_clicked(self):
        app.procNextState(STATE_MAIN)


class CMainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.s = None

    def __CreateState(self, state):
        if state == STATE_LOGIN:
            self.s = CLoginState()
        if state == STATE_MAIN:
            self.s = CMainState()
        return self.s

    def procNextState(self, state):
        s = self.__CreateState(state)
        s.start()

    def run(self):
        self.procNextState(STATE_LOGIN)
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    app = CMainApp()
    app.run()
