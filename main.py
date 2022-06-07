import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_main_stacked import Ui_MainWindow
from ui_mainworkspace import Ui_MainWindowBig

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
        QFontDatabase.addApplicationFont('Ubuntu-Regular.ttf')
        QMainWindow.__init__(self)
        self.dragPos = None
        self.ui = Ui_MainWindowBig()
        self.ui.setupUi(self)
        # ScrollArea страницы добавления
        self.scroll_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents_3)
        # ScrollArea страницы со списком портфелей
        self.scroll_layout_list = QVBoxLayout(self.ui.scrollAreaWidgetContents_caseList)

        # self.ui.to_login_2.clicked.connect(self.btn_to_login)
        # self.ui.to_login_2.clicked.connect(self.close)

        def moveWindow(event):
            if UIFuncs.returnStatus(self) == 1:
                UIFuncs.maximize_restore(self)
            # If left click - move window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.title_bar_2.mouseMoveEvent = moveWindow

        self.ui.btn_addToList.clicked.connect(self.get_token_btn)

        UIFuncs.uiDefinitions(self)

        # Смена окон в MainWindow Login

        # Adding list
        self.ui.btn_addCase.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_add_case))

        # List of portfolios
        self.ui.btn_case.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_caseList))

        # Analytics page
        self.ui.btn_analtics.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_analytics))

        # Portfolio page
        self.ui.btn_casemain.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_casebig))

    # Движение окна
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # Переход из окна Портфель (пока что) на окно входа
    def btn_to_login(self):
        app.procNextState(STATE_LOGIN)

    # Получение данных по токену из строки ввода
    def get_token_btn(self):
        count = int(self.ui.edit_token.text())
        print('inside get token func')
        self.clear_layout()
        self.create_new_widget(count)

    # Создание кнопок-полей счетов
    def create_new_widget(self, count):
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        for i in range(count):
            btn_text = 'btn' + str(i)
            btn = QPushButton(btn_text, self.ui.scrollAreaWidgetContents_3)
            btn.setStyleSheet(u"QPushButton {border-radius: 25px;\n"
                                "background-color: rgb(148, 148, 152);\n"
                                "height: 60px;\n }"
                                "QPushButton:hover {\n"
                                "	background-color:rgb(234, 234, 234);}\n")
            btn.setFlat(True)
            btn.setObjectName(btn_text)
            btn.clicked.connect(self.add_portfolio_to_list)
            btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_casebig))
            self.scroll_layout.addWidget(btn)

    # Добавление портфеля в список портфелей
    def add_portfolio_to_list(self):
        sender = self.sender()
        self.scroll_layout_list.setAlignment(QtCore.Qt.AlignTop)
        btn_text_list = sender.text() + '_' + 'list'
        btn_list = QPushButton(btn_text_list, self.ui.scrollAreaWidgetContents_caseList)
        btn_list.setObjectName(btn_text_list)
        btn_list.setStyleSheet(u"QPushButton {border-radius: 25px;\n"
                                "background-color: rgb(148, 148, 152);\n"
                                "height: 60px;\n }"
                                "QPushButton:hover {\n"
                                "	background-color:rgb(234, 234, 234);}\n")
        btn_list.setFlat(True)
        btn_list.clicked.connect(self.check_presence)
        if self.check_presence():
            self.scroll_layout_list.addWidget(btn_list)
        else:
            btn_list.setParent(None)
        btn_list.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_casebig))

    # Проверка наличия кнопки с заданным идентификатором в окне со списком счетов
    def check_presence(self):
        sender = self.sender()
        elem_inside = False
        for i in range(self.scroll_layout_list.count()):
            item = self.scroll_layout_list.itemAt(i).widget()
            if item.text() == sender.text() + '_' + 'list':
                elem_inside = True
        if elem_inside:
            return False
        return True

    # Очистка перед последующим выводом счетов
    def clear_layout(self):
        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.takeAt(i).widget().setParent(None)


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
