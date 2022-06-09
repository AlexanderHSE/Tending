import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_main_stacked import Ui_MainWindow
from ui_mainworkspace import Ui_MainWindowBig

from ui_functions import *
from tinkoff.invest import Client, RequestError, PortfolioPosition
from tinkoff.invest.schemas import PortfolioResponse

from tending import get_total_cost_portfolio, cast_yield, get_total_profit, get_set_positions

minus_profit = "#FAA2A2" # hex red color
zero_porfit = "#F9F9FB"  # hex white color
plus_profit = "#47F19F " # hex green color



# # APP STATES
#
# STATE_LOGIN = 0
# STATE_MAIN = 1
#
#
# class CLoginState:
#     def __init__(self):
#         super(CLoginState, self).__init__()
#         self.login = LogWindow()
#
#     def start(self):
#         self.login.show()
#
#
# class CMainState:
#     def __init__(self):
#         super(CMainState, self).__init__()
#         self.work_win = MainWindow()
#
#     def start(self):
#         self.work_win.show()
#

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
        self.position_pie_chart_based_list = QVBoxLayout(self.ui.scrollAreaWidgetContents_4)

        self.ui.instruments_cpa_scrollArea.verticalScrollBar().setStyleSheet('QScrollBar {width:0px;}')

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
    # def btn_to_login(self):
    #     app.procNextState(STATE_LOGIN)

    # Получение данных по токену из строки ввода
    def get_token_btn(self):
        accounts = None
        while True:
            token = self.ui.edit_token.text()
            try:
                with Client(token) as client:
                    accounts = client.users.get_accounts()
                    break
            except RequestError:
                print("Ошибка, введите токен заново!")
                break
        self.clear_layout()
        self.create_new_widget(token, accounts)

    # Создание кнопок-полей счетов
    def create_new_widget(self, token, accounts):
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        for i in range(len(accounts.accounts)):
            btn_text = accounts.accounts[i].name
            btn = QPushButton(btn_text, self.ui.scrollAreaWidgetContents_3)
            btn.setStyleSheet(u"QPushButton {border-radius: 25px;\n"
                              "background-color: rgb(148, 148, 152);\n"
                              "height: 60px;\n }"
                              "QPushButton:hover {\n"
                              "	background-color:rgb(234, 234, 234);}\n")
            btn.setFlat(True)
            btn.setObjectName(btn_text)
            btn.clicked.connect(
                lambda *args, add_new_port=True, tok=token, acc=accounts.accounts[i]: self.add_portfolio_to_list(
                    add_new_port, tok, acc))
            btn.clicked.connect(
                lambda *args, tok=token, acc=accounts.accounts[i]: self.fill_main_portfolio(tok, acc))
            # btn.clicked.connect(self.add_portfolio_to_list(accounts.accounts[i]))
            btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_casebig))
            # btn.clicked.connect(self.fill_main_portfolio(accounts.accounts[i]))
            self.scroll_layout.addWidget(btn)

    # Добавление портфеля в список портфелей
    def add_portfolio_to_list(self, add_new_port=False, token=None, acc=None):
        sender = self.sender()
        print(acc.name)
        self.scroll_layout_list.setAlignment(QtCore.Qt.AlignTop)
        # btn_text_list = sender.text()
        btn_text_list = acc.name
        btn_list = QPushButton(btn_text_list, self.ui.scrollAreaWidgetContents_caseList)
        btn_list.setObjectName(btn_text_list)
        btn_list.setStyleSheet(u"QPushButton {border-radius: 25px;\n"
                               "background-color: rgb(148, 148, 152);\n"
                               "height: 60px;\n }"
                               "QPushButton:hover {\n"
                               "	background-color:rgb(234, 234, 234);}\n")
        btn_list.setFlat(True)
        btn_list.clicked.connect(lambda *args, acc_=acc: self.check_presence(acc_))
        if self.check_presence(acc):
            self.scroll_layout_list.addWidget(btn_list)
        else:
            btn_list.setParent(None)
        # Надо как то убрать двойное выполнение функции
        btn_list.clicked.connect(lambda *args, acc_=acc: self.fill_main_portfolio(token, acc_))
        btn_list.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_casebig))

    # Проверка наличия кнопки с заданным идентификатором в окне со списком счетов
    def check_presence(self, acc=None):
        sender = self.sender()
        elem_inside = False
        for i in range(self.scroll_layout_list.count()):
            item = self.scroll_layout_list.itemAt(i).widget()
            if item.text() == acc.name:
                elem_inside = True
        if elem_inside:
            return False
        return True

    # Очистка перед последующим выводом счетов
    def clear_layout(self):
        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.takeAt(i).widget().setParent(None)

    def fill_total_cost(self, portfolio: PortfolioResponse):
        total_cost = str(get_total_cost_portfolio(portfolio)) + "₽"
        self.ui.cost_number_all.setText(total_cost)
        self.ui.cost_number_all.setStyleSheet(f"font-size : 20px; font-family : Open Sans; color : {zero_porfit}")

    def fill_total_yield(self, portfolio: PortfolioResponse):
        total_yield = portfolio.expected_yield
        total_yield_percentage = cast_yield(total_yield)
        self.ui.yield_number_all.setText(str(total_yield_percentage) + "%")
        if total_yield_percentage < 0:
            self.ui.yield_number_all.setStyleSheet(f"font-size : 20px; font-family : Open Sans; color : {minus_profit}")
        elif total_yield_percentage == 0:
            self.ui.yield_number_all.setStyleSheet(f"font-size : 20px; font-family : Open Sans; color : {zero_porfit}")
        elif total_yield_percentage > 0:
            self.ui.yield_number_all.setStyleSheet(f"font-size : 20px; font-family : Open Sans; color : {plus_profit}")

    def fill_total_profit(self, portfolio: PortfolioResponse):
        total_yield = portfolio.expected_yield
        total_yield_percentage = cast_yield(total_yield)
        total_cost = get_total_cost_portfolio(portfolio)
        total_profit = get_total_profit(total_yield_percentage, total_cost)
        self.ui.profit_number_all.setText(str(total_profit) + "₽")
        if total_yield_percentage < 0:
            self.ui.profit_number_all.setStyleSheet(f"font-size : 20px; font-family : Open Sans; color : {minus_profit}")
        elif total_yield_percentage == 0:
            self.ui.profit_number_all.setStyleSheet(f"font-size : 20px; font-family : Open Sans; color : {zero_porfit}")
        elif total_yield_percentage > 0:
            self.ui.profit_number_all.setStyleSheet(f"font-size : 20px; font-family : Open Sans; color : {plus_profit}")

    def fill_total_stats(self, portfolio):
        self.fill_total_cost(portfolio)
        self.fill_total_yield(portfolio)
        self.fill_total_profit(portfolio)

    def add_pos_in_area_pie_based(self, positions: list):
        self.position_pie_chart_based_list.setAlignment(QtCore.Qt.AlignTop)
        c = 0
        for pos in positions:
            c += 1
            frame_inst = QFrame(self.ui.scrollAreaWidgetContents_4)
            # frame_inst = QFrame(self.scrollAreaWidgetContents_4)
            frame_inst.setObjectName("inst_1" + str(c))
            frame_inst.setGeometry(QRect(0, 0, 401, 41))
            frame_inst.setFrameShape(QFrame.StyledPanel)
            frame_inst.setFrameShadow(QFrame.Raised)
            frame_inst_layout = QHBoxLayout(frame_inst)
            frame_inst.setStyleSheet('''
                background-color: #222226;
                padding-left: 0px;
            ''')

            inst_color = QFrame()
            inst_color.setObjectName("inst_color" + str(c))
            inst_color.setGeometry(QRect(0, 0, 5, 51))
            inst_color.setStyleSheet(f"font-size : 20px; font-family : Open Sans; background-color : {pos['color']};")
            # inst_color.setStyleSheet("font-size : 16px; font-family : Open Sans; background-color : #47F19F")
            inst_color.setFrameShape(QFrame.StyledPanel)
            inst_color.setFrameShadow(QFrame.Raised)
            inst_color.setMaximumSize(QSize(5, 16777215))
            inst_color.setContentsMargins(0, 0, 0, 0)
            frame_inst_layout.addWidget(inst_color)

            inst_name = QLabel()
            if pos['ticker'] != "":
                inst_name.setText(pos['ticker'])
            else:
                inst_name.setText(pos['name'])
            inst_name.setObjectName("inst_name" + str(c))
            inst_name.setGeometry(QRect(10, -10, 51, 61))
            # inst_name.setMaximumSize(QSize(80, 16777215))
            inst_name.adjustSize()
            inst_name.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                    "")
            inst_name.setAlignment(Qt.AlignCenter)
            frame_inst_layout.addWidget(inst_name)

            inst_type = QLabel()
            inst_type.setText(pos['instrument_type'])
            inst_type.setObjectName("inst_type" + str(c))
            inst_type.setGeometry(QRect(80, -10, 21, 61))
            # inst_type.setMaximumSize(QSize(65, 16777215))
            inst_type.adjustSize()
            inst_type.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                    "")
            inst_type.setAlignment(Qt.AlignCenter)
            frame_inst_layout.addWidget(inst_type)

            inst_quan = QLabel()
            inst_quan.setText(str(pos['quantity']))
            inst_quan.setObjectName("inst_quan" + str(c))
            inst_quan.setGeometry(QRect(130, -10, 21, 61))
            # inst_quan.setMaximumSize(QSize(56, 16777215))
            inst_quan.adjustSize()
            inst_quan.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                    "")
            inst_quan.setAlignment(Qt.AlignCenter)
            frame_inst_layout.addWidget(inst_quan)

            inst_cost = QLabel()
            inst_cost.setText(str(round(pos['current_buy_price'], 2)) + "\n" + str(round(pos['average_buy_price'], 2)))
            inst_cost.setObjectName("inst_cost" + str(c))
            inst_cost.setGeometry(QRect(190, -10, 51, 61))
            # inst_cost.setMaximumSize(QSize(56, 16777215))
            inst_cost.adjustSize()
            inst_cost.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                    "")
            inst_cost.setAlignment(Qt.AlignCenter)
            frame_inst_layout.addWidget(inst_cost)

            inst_profit = QLabel()
            if pos['expected_yield'] < 0:
                inst_profit.setStyleSheet(u"color:  # FAA2A2")
                inst_profit.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {minus_profit}")
               # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {minus_profit}")
            elif pos['expected_yield'] == 0:
                inst_profit.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {zero_porfit}")
               # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {zero_porfit}")
            elif pos['expected_yield'] > 0:
                inst_profit.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {plus_profit}")
                #inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {plus_profit}")
            inst_profit.setText(str(round(pos['expected_yield'], 2)) + "₽\n" +
                                str(round(pos['expected_yield_percentage'], 2)) + "%")
            inst_profit.setObjectName("inst_profit" + str(c))
            inst_profit.setGeometry(QRect(270, -20, 56, 61))
            # inst_profit.setMaximumSize(QSize(56, 16777215))
            inst_profit.adjustSize()
            #inst_profit.setStyleSheet(u"font-size : 13px; font-family : Open Sans");
            inst_profit.setAlignment(Qt.AlignCenter)
            frame_inst_layout.addWidget(inst_profit)

            inst_percent = QLabel()
            inst_percent.setText(str(round(pos['portfolio_share'],2)) + "%")
            inst_percent.setObjectName("inst_percent" + str(c))
            inst_percent.setGeometry(QRect(340, -20, 56, 61))
            inst_percent.setMaximumSize(QSize(56, 16777215))
            inst_percent.adjustSize()
            inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {zero_porfit}")
            inst_percent.setAlignment(Qt.AlignCenter)
            inst_percent.setContentsMargins(0, 0, 0, 0)
            frame_inst_layout.addWidget(inst_percent)

            self.position_pie_chart_based_list.addWidget(frame_inst)

    def fill_area_pie_based(self, token, client, portfolio):
        list_pos = get_set_positions(token, client, portfolio)
        self.add_pos_in_area_pie_based(list_pos)

    def fill_main_portfolio(self, token, account):
        print('Данные переданы', account.name)
        sender = self.sender()
        with Client(token) as client:
            portfolio = client.operations.get_portfolio(account_id=account.id)
            self.fill_total_stats(portfolio)
            self.fill_area_pie_based(token, client, portfolio)

        print(token)


#
# class LogWindow(QMainWindow):
#     def __init__(self):
#         QFontDatabase.addApplicationFont('Ubuntu-Regular.ttf')
#         QMainWindow.__init__(self)
#         self.dragPos = None
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.ui.btn_show_password_2.clicked.connect(self.toggleVisibility)
#
#         # Move Window
#         def moveWindow(event):
#             # If left click - move window
#             if event.buttons() == Qt.LeftButton:
#                 self.move(self.pos() + event.globalPos() - self.dragPos)
#                 self.dragPos = event.globalPos()
#                 event.accept()
#
#         # Set title bar
#         self.ui.title_bar_2.mouseMoveEvent = moveWindow
#
#         UIFunctions.uiDefinitions(self)
#
#         # Смена окон в MainWindow Login
#
#         # Login Window
#         self.ui.btn_signin_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_reg))
#
#         # Registration Window
#         self.ui.btn_signin_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_login))
#
#         # Переход к окну программы с метриками
#         self.ui.btn_signin_3.clicked.connect(self.btn_to_main_clicked)
#         self.ui.btn_signin_5.clicked.connect(self.btn_to_main_clicked)
#
#         # Закрытие окна
#         self.ui.btn_signin_3.clicked.connect(self.close)
#         self.ui.btn_signin_5.clicked.connect(self.close)
#
#     def mousePressEvent(self, event):
#         self.dragPos = event.globalPos()
#
#     # Изменение видимости пароля
#     def toggleVisibility(self):
#         if self.ui.edit_password_2.echoMode() == QLineEdit.Normal:
#             self.ui.edit_password_2.setEchoMode(QLineEdit.Password)
#             new_icon = QPixmap('closedEyeChanged.png')
#             self.ui.btn_show_password_2.setIcon(QIcon(new_icon))
#         else:
#             self.ui.edit_password_2.setEchoMode(QLineEdit.Normal)
#             new_icon = QPixmap('openedEye.png')
#             self.ui.btn_show_password_2.setIcon(QIcon(new_icon))
#
#     def btn_to_main_clicked(self):
#         app.procNextState(STATE_MAIN)
#
#
# class CMainApp:
#     def __init__(self):
#         self.app = QApplication(sys.argv)
#         self.s = None
#
#     def __CreateState(self, state):
#         if state == STATE_LOGIN:
#             self.s = CLoginState()
#         if state == STATE_MAIN:
#             self.s = CMainState()
#         return self.s
#
#     def procNextState(self, state):
#         s = self.__CreateState(state)
#         s.start()
#
#     def run(self):
#         self.procNextState(STATE_LOGIN)
#         sys.exit(self.app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
