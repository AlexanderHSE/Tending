import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, QDir, QUrlQuery)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_main_stacked import Ui_MainWindow
from PySide2.QtWebEngineWidgets import QWebEngineView
from ui_mainworkspace import Ui_MainWindowBig

from ui_functions import *
from tinkoff.invest import Client, RequestError, PortfolioPosition
from tinkoff.invest.schemas import PortfolioResponse

from tending import get_total_cost_portfolio, cast_yield, get_total_profit, get_set_positions

import pandas as pd
import numpy as np

import plotly
import plotly.express as px
from plotly.graph_objs import *

from help_func import write_html, check_dt_is_empty, generate_color_column, add_column_percantages, \
    generate_color_by_sectors_column, check_float

from frame_creating import create_shares_frame_on_analytic_page, create_bonds_frame_on_analytic_page, \
    create_etfs_frame_on_analytic_page, create_currencies_frame_on_analytic_page

from re import search

minus_profit = "#FAA2A2"  # hex red color
zero_porfit = "#F9F9FB"  # hex white color
plus_profit = "#47F19F "  # hex green color


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
        self.position_analytic_pie_chart_based_list = QVBoxLayout(self.ui.scrollAreaWidgetContents_2)
        self.all_instruments_analytic_page_list = QVBoxLayout(self.ui.scrollAreaWidgetAllInstrumentsAPage)
        self.ui.scroll_area_all_instruments_analytic_page.verticalScrollBar().setStyleSheet('QScrollBar {width:0px;}')
        self.ui.instruments_cpa_scrollArea.verticalScrollBar().setStyleSheet('QScrollBar {width:0px;}')
        self.ui.legeng_analytic_pie_chart.verticalScrollBar().setStyleSheet('QScrollBar {width:0px;}')
        self.ui.legeng_analytic_pie_chart.horizontalScrollBar().setStyleSheet('QScrollBar {height:0px;}')
        self.main_pie_chart = QtWebEngineWidgets.QWebEngineView(self.ui.widget)
        self.analytic_pie_chart = QtWebEngineWidgets.QWebEngineView(self.ui.analytics_graps_widget)

        def moveWindow(event):
            # If left click - move window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.title_bar_2.mouseMoveEvent = moveWindow

        self.ui.btn_addToList.clicked.connect(self.get_token_btn)

        self.ui.pushButton.clicked.connect(self.toggle_visibility)

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

    def toggle_visibility(self):
        """
        Функция, выполняющая изменение видимости токена
        """
        if self.ui.edit_token.echoMode() == QLineEdit.Normal:
            self.ui.edit_token.setEchoMode(QLineEdit.Password)
            new_icon = QPixmap('closedEyeChanged.png')
            self.ui.pushButton.setIcon(QIcon(new_icon))
        else:
            self.ui.edit_token.setEchoMode(QLineEdit.Normal)
            new_icon = QPixmap('openedEye.png')
            self.ui.pushButton.setIcon(QIcon(new_icon))

    # Движение окна
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # Получение данных по токену из строки ввода
    def get_token_btn(self):
        accounts = None
        while True:
            token = self.ui.edit_token.text().strip()
            try:
                self.ui.edit_token.setPlaceholderText('Введите токен')
                self.ui.edit_token.setStyleSheet('''
                    border-radius: 20px;
                    color: rgb(180, 180, 189);
                    background-color: rgb(73, 73, 77);
                    padding-left: 12px;
                ''')
                with Client(token) as client:
                    accounts = client.users.get_accounts()
                    break
            except (RequestError, ValueError):
                print("Ошибка, введите токен заново!")
                self.ui.edit_token.setPlaceholderText('Ошибка, введите токен заново!')
                pal = self.ui.edit_token.palette()
                text_color = pal.color(QtGui.QPalette.Text)
                pal.setColor(QtGui.QPalette.PlaceholderText, text_color)
                self.ui.edit_token.setPalette(pal)
                self.ui.edit_token.setText('')
                break
        self.clear_layout()
        self.create_new_widget(token, accounts)

    # Создание кнопок-полей счетов
    def create_new_widget(self, token, accounts):
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        for i in range(len(accounts.accounts)):
            if accounts.accounts[i].access_level != 3:
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
                    lambda *args, tok=token, acc=accounts.accounts[i]: self.fill_portfolio(tok, acc))
                # btn.clicked.connect(self.add_portfolio_to_list(accounts.accounts[i]))
                btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_casebig))
                # btn.clicked.connect(self.fill_portfolio(accounts.accounts[i]))
                self.scroll_layout.addWidget(btn)

    # Добавление портфеля в список портфелей
    def add_portfolio_to_list(self, add_new_port=False, token=None, acc=None):
        sender = self.sender()
        self.scroll_layout_list.setAlignment(QtCore.Qt.AlignTop)
        # btn_text_list = sender.text()
        btn_text_list = acc.name + ' ' + ' id ' + acc.id
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
        btn_list.clicked.connect(lambda *args, acc_=acc: self.fill_portfolio(token, acc_))
        btn_list.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_casebig))

    # Проверка наличия кнопки с заданным идентификатором в окне со списком счетов
    def check_presence(self, acc=None):
        """
        Проверка наличия добавляемого счёта в списке счетов.

        Параметры:
            acc : Добавляемый аккаунт
        """
        sender = self.sender()
        elem_inside = False
        for i in range(self.scroll_layout_list.count()):
            item = self.scroll_layout_list.itemAt(i).widget()
            # Проверка, что аккаунт с таким id уже есть в списке счетов
            if search('id.*?(\d+)', item.text()).group(1) == acc.id:
                elem_inside = True
        if elem_inside:
            return False
        return True

    # Очистка перед последующим выводом счетов
    def clear_layout(self):
        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.takeAt(i).widget().setParent(None)

    def fill_total_cost(self, df, portfolio: PortfolioResponse):
        total_cost = str(get_total_cost_portfolio(df, portfolio)) + "₽"
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

    def fill_total_profit(self, df, portfolio: PortfolioResponse):
        total_yield = portfolio.expected_yield
        total_yield_percentage = cast_yield(total_yield)
        total_cost = get_total_cost_portfolio(df, portfolio)
        total_profit = get_total_profit(total_yield_percentage, total_cost)
        self.ui.profit_number_all.setText(str(total_profit) + "₽")
        if total_yield_percentage < 0:
            self.ui.profit_number_all.setStyleSheet(
                f"font-size : 20px; font-family : Open Sans; color : {minus_profit}")
        elif total_yield_percentage == 0:
            self.ui.profit_number_all.setStyleSheet(f"font-size : 20px; font-family : Open Sans; color : {zero_porfit}")
        elif total_yield_percentage > 0:
            self.ui.profit_number_all.setStyleSheet(f"font-size : 20px; font-family : Open Sans; color : {plus_profit}")

    def fill_total_stats(self, df, portfolio):
        self.fill_total_yield(portfolio)
        self.fill_total_profit(df, portfolio)
        self.fill_total_cost(df, portfolio)

    def add_pos_in_area_pie_based(self, positions):
        self.position_pie_chart_based_list.setAlignment(QtCore.Qt.AlignTop)
        c = 0
        for indexRow in range(len(positions.index)):
            row = positions.iloc[indexRow]
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
            inst_color.setStyleSheet(f"font-size : 20px; font-family : Open Sans; background-color : {row['color']};")
            # inst_color.setStyleSheet("font-size : 16px; font-family : Open Sans; background-color : #47F19F")
            inst_color.setFrameShape(QFrame.StyledPanel)
            inst_color.setFrameShadow(QFrame.Raised)
            inst_color.setMaximumSize(QSize(5, 16777215))
            inst_color.setContentsMargins(0, 0, 0, 0)
            frame_inst_layout.addWidget(inst_color)

            inst_name = QLabel()
            if row['ticker'] != "":
                inst_name.setText(row['ticker'])
            else:
                inst_name.setText(row['name'])
            inst_name.setObjectName("inst_name" + str(c))
            inst_name.setGeometry(QRect(10, -10, 51, 61))
            # inst_name.setMaximumSize(QSize(80, 16777215))
            inst_name.adjustSize()
            inst_name.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                    "")
            inst_name.setAlignment(Qt.AlignCenter)
            frame_inst_layout.addWidget(inst_name)

            inst_type = QLabel()
            inst_type.setText(row['instrument_type'])
            inst_type.setObjectName("inst_type" + str(c))
            inst_type.setGeometry(QRect(80, -10, 21, 61))
            # inst_type.setMaximumSize(QSize(65, 16777215))
            inst_type.adjustSize()
            inst_type.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                    "")
            inst_type.setAlignment(Qt.AlignCenter)
            frame_inst_layout.addWidget(inst_type)

            inst_quan = QLabel()
            if check_float(row['quantity']):
                inst_quan.setText(str(int(row['quantity'])))
            else:
                inst_quan.setText(str(row['quantity']))
            inst_quan.setObjectName("inst_quan" + str(c))
            inst_quan.setGeometry(QRect(130, -10, 21, 61))
            # inst_quan.setMaximumSize(QSize(56, 16777215))
            inst_quan.adjustSize()
            inst_quan.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                    "")
            inst_quan.setAlignment(Qt.AlignCenter)
            frame_inst_layout.addWidget(inst_quan)

            inst_cost = QLabel()
            inst_cost.setText(str(round(row['current_buy_price'], 2)) + "\n" + str(round(row['average_buy_price'], 2)))
            inst_cost.setObjectName("inst_cost" + str(c))
            inst_cost.setGeometry(QRect(190, -10, 51, 61))
            # inst_cost.setMaximumSize(QSize(56, 16777215))
            inst_cost.adjustSize()
            inst_cost.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                    "")
            inst_cost.setAlignment(Qt.AlignCenter)
            frame_inst_layout.addWidget(inst_cost)

            inst_profit = QLabel()
            if row['expected_yield'] < 0:
                inst_profit.setStyleSheet(u"color:  # FAA2A2")
                inst_profit.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {minus_profit}")
            # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {minus_profit}")
            elif row['expected_yield'] == 0:
                inst_profit.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {zero_porfit}")
            # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {zero_porfit}")
            elif row['expected_yield'] > 0:
                inst_profit.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {plus_profit}")
                # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {plus_profit}")
            inst_profit.setText(str(round(row['expected_yield'], 2)) + "₽\n" +
                                str(round(row['expected_yield_percentage'], 2)) + "%")
            inst_profit.setObjectName("inst_profit" + str(c))
            inst_profit.setGeometry(QRect(270, -20, 56, 61))
            # inst_profit.setMaximumSize(QSize(56, 16777215))
            inst_profit.adjustSize()
            # inst_profit.setStyleSheet(u"font-size : 13px; font-family : Open Sans");
            inst_profit.setAlignment(Qt.AlignCenter)
            frame_inst_layout.addWidget(inst_profit)

            inst_percent = QLabel()
            inst_percent.setText(str(round(row['portfolio_share'], 2)) + "%")
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
        self.create_main_portfolio_pie_chart(list_pos, portfolio)
        self.clear_pos_in_area_pie()
        global all_instruments_df
        all_instruments_df = pd.DataFrame()
        if len(list_pos) == 0:
            all_instruments_df['cost'] = pd.Series()
            print("Here")
            '''
            УДАЛЕНИЕ ДЕЛАТЬ ТУТ ! 
            '''
            self.clear_all_instruments_on_analytic_page()
        else:
            all_instruments_df = pd.DataFrame(list_pos)
        all_instruments_df = all_instruments_df.sort_values('cost', ascending=False)
        all_instruments_df = all_instruments_df.set_index(np.arange(0, len(all_instruments_df.index), 1))
        self.add_pos_in_area_pie_based(all_instruments_df)
        self.fill_analyt_page(list_pos)

    def clear_pos_in_area_pie(self):
        for i in reversed(range(self.position_pie_chart_based_list.count())):
            self.position_pie_chart_based_list.takeAt(i).widget().setParent(None)

    def create_main_portfolio_pie_chart(self, list_positions, portfolio):
        df = pd.DataFrame(list_positions)
        if df.empty:
            self.clear_legend_analytics_pie_chart()
            self.ui.analytics_graps_widget.hide()
            global full_df
            global current_df
            global all_instruments_df
            global request_from_currencies
            full_df = pd.DataFrame()
            current_df = pd.DataFrame()
            all_instruments_df = pd.DataFrame()
            request_from_currencies = False
            self.ui.widget.hide()
            self.fill_total_stats(df, portfolio)
        else:
            df = df.sort_values('name')
            self.ui.widget.show()
            self.fill_total_stats(df, portfolio)
            pie_chart = px.pie(data_frame=df, values='portfolio_share', names='name', color='name',
                               color_discrete_sequence=list(df['color']),
                               hole=0.3)
            hovertemp = "%{label} \n"
            hovertemp += "%{value}%\n\n"
            pie_chart.update_traces(hovertemplate=hovertemp)
            pie_chart.update_traces(textposition='inside', showlegend=False)
            pie_chart.update_layout(paper_bgcolor='#2A2A2C', plot_bgcolor='#2A2A2C', uniformtext_minsize=12,
                                    uniformtext_mode='hide')

            # plotly.offline.plot(pie_chart, filename="MainPieChart.html")
            write_html(pie_chart, "MainPortfolioPieChart.html")
            self.show_graph()

    def show_graph(self):
        with open("MainPortfolioPieChart.html", 'r') as pie_char_html:
            self.main_pie_chart.setHtml(pie_char_html.read())
            self.main_pie_chart.setMinimumSize(390, 400)

    def fill_main_page(self, portfolio, token, client):
        self.fill_area_pie_based(token, client, portfolio)

    def link_analytic_buttons(self, list_positions):
        self.ui.btn_all_instruments.clicked.connect(lambda: self.give_all_instruments_to_charts())
        self.ui.btn_shares.clicked.connect(lambda: self.give_all_shares_to_charts())
        self.ui.btn_bonds.clicked.connect(lambda: self.give_all_bonds_to_charts())
        self.ui.btn_etfs.clicked.connect(lambda: self.give_all_etf_to_charts())
        self.ui.btn_currencies_all.clicked.connect(lambda: self.give_all_currencies_to_charts())

        self.ui.btn_currencies.clicked.connect(lambda: self.grouping_by_currencies_pie_chart_analytical_page())
        self.ui.btn_sectors.clicked.connect(lambda: self.grouping_by_sectors_pie_chart_analytical_page())
        self.ui.btn_countries.clicked.connect(lambda: self.grouping_by_countries_pie_chart_analytical_page())
        self.ui.btn_instruments_type.clicked.connect(
            lambda: self.grouping_by_instruments_type_pie_chart_analytical_page())

    # Нажимаем на кнопку "Все инструменты" и передаем все инструменты для графиков.
    def give_all_instruments_to_charts(self):
        global current_df
        if not current_df.empty:
            current_df = full_df
            self.ui.btn_countries.show()
            self.ui.btn_instruments_type.show()
            self.ui.btn_sectors.show()
            global request_from_currencies
            request_from_currencies = False
            self.grouping_by_currencies_pie_chart_analytical_page()

    # Нажимаем на кнопку "Акции" и передаем только все акции для графиков.
    def give_all_shares_to_charts(self):
        global current_df
        if not current_df.empty:
            current_df = full_df[full_df['instrument_type'] == 'Акция']
            self.ui.btn_countries.show()
            self.ui.btn_instruments_type.hide()
            self.ui.btn_sectors.show()
            global request_from_currencies
            request_from_currencies = False
            self.grouping_by_currencies_pie_chart_analytical_page()

    # Нажимаем на кнопку "Облигации" и передаем только все облигации для графиков.
    def give_all_bonds_to_charts(self):
        global current_df
        if not current_df.empty:
            current_df = full_df[full_df['instrument_type'] == 'Облигация']
            self.ui.btn_countries.show()
            self.ui.btn_instruments_type.hide()
            self.ui.btn_sectors.hide()
            global request_from_currencies
            request_from_currencies = False
            self.grouping_by_currencies_pie_chart_analytical_page()

    # Нажимаем на кнопку "Фонды" и передаем только все фонды для графиков.
    def give_all_etf_to_charts(self):
        global current_df
        if not current_df.empty:
            current_df = full_df[full_df['instrument_type'] == 'Фонд']
            self.ui.btn_countries.show()
            self.ui.btn_instruments_type.hide()
            self.ui.btn_sectors.hide()
            global request_from_currencies
            request_from_currencies = False
            self.grouping_by_currencies_pie_chart_analytical_page()

    # Нажимаем на кнопку "Валюты" и передаем только все валюты для графиков.
    def give_all_currencies_to_charts(self):
        global current_df
        if not current_df.empty:
            current_df = full_df[full_df['instrument_type'] == 'Валюта']
            self.ui.btn_countries.hide()
            self.ui.btn_instruments_type.hide()
            self.ui.btn_sectors.hide()
            global request_from_currencies
            request_from_currencies = True
            self.grouping_by_currencies_pie_chart_analytical_page()

    # Нажимаем на кнопку "Валюта" и строим график валют на основе переданных данных.
    def grouping_by_currencies_pie_chart_analytical_page(self):
        global request_from_currencies
        if not current_df.empty:
            if request_from_currencies:
                data = current_df.groupby('name').agg('sum')
            else:
                data = current_df.groupby('original_currency').agg('sum')
            if not check_dt_is_empty(data):
                self.ui.analytics_graps_widget.show()
                self.disactivate_text_on_analytic_pie_chart()
                currencies = list(data.index)
                data = data.set_index(np.arange(0, len(data.index), 1))
                data['currencies'] = pd.Series(currencies)
                add_column_percantages(data)
                generate_color_column(data)
                data = data.sort_values('total_cost_percentage', ascending=False)
                pie_chart = px.pie(data_frame=data, values='total_cost_percentage', names='currencies',
                                   color='currencies',
                                   color_discrete_sequence=list(data['color']),
                                   hole=0.3)
                hovertemp = "%{label} "
                hovertemp += "%{value}%            "
                pie_chart.update_traces(hovertemplate=hovertemp)
                pie_chart.update_traces(textposition='inside', showlegend=False)
                pie_chart.update_layout(paper_bgcolor='#2A2A2C', plot_bgcolor='#2A2A2C', uniformtext_minsize=12,
                                        uniformtext_mode='hide', )
                name_graph = "AnalyticByCurrenciesPieChart.html"
                write_html(pie_chart, name_graph)
                self.show_analytic_pie_chart(name_graph, data, 'currencies')
            else:
                self.ui.analytics_graps_widget.hide()
                self.activate_text_on_analytic_pie_chart()

    # Нажимаем на кнопку "Сектора" и строим график секторов на основе переданных данных.
    def grouping_by_sectors_pie_chart_analytical_page(self):
        if not current_df.empty:
            data = current_df.groupby('sector').agg('sum')
            if not check_dt_is_empty(data):
                self.ui.analytics_graps_widget.show()
                self.disactivate_text_on_analytic_pie_chart()
                sectors = list(data.index)
                data = data.set_index(np.arange(0, len(data.index), 1))
                data['sector'] = pd.Series(sectors)
                add_column_percantages(data)
                generate_color_by_sectors_column(data)
                data = data.sort_values('total_cost_percentage', ascending=False)
                pie_chart = px.pie(data_frame=data, values='total_cost_percentage', names='sector', color='sector',
                                   color_discrete_sequence=list(data['color']),
                                   hole=0.3)
                hovertemp = "%{label} "
                hovertemp += "%{value}%      "
                pie_chart.update_traces(hovertemplate=hovertemp)
                pie_chart.update_traces(textposition='inside', showlegend=False)
                pie_chart.update_layout(paper_bgcolor='#2A2A2C', plot_bgcolor='#2A2A2C', uniformtext_minsize=12,
                                        uniformtext_mode='hide', )
                name_graph = "AnalyticBySectorsPieChart.html"
                write_html(pie_chart, name_graph)
                self.show_analytic_pie_chart(name_graph, data, 'sector')
            else:
                self.ui.analytics_graps_widget.hide()
                self.activate_text_on_analytic_pie_chart()

    # Нажимаем на кнопку "Страны" и строим график стран на основе переданных данных.
    def grouping_by_countries_pie_chart_analytical_page(self):
        if not current_df.empty:
            data = current_df.groupby('short_country_name').agg('sum')
            if not check_dt_is_empty(data):
                self.ui.analytics_graps_widget.show()
                self.disactivate_text_on_analytic_pie_chart()
                countries = list(data.index)
                data = data.set_index(np.arange(0, len(data.index), 1))
                data['short_country_name'] = pd.Series(countries)
                add_column_percantages(data)
                generate_color_column(data)
                data = data.sort_values('total_cost_percentage', ascending=False)
                pie_chart = px.pie(data_frame=data, values='total_cost_percentage', names='short_country_name',
                                   color='short_country_name', color_discrete_sequence=list(data['color']),
                                   hole=0.3)
                hovertemp = "%{label} \n"
                hovertemp += "%{value}%               "
                pie_chart.update_traces(hovertemplate=hovertemp)
                pie_chart.update_traces(textposition='inside', showlegend=False)
                pie_chart.update_layout(paper_bgcolor='#2A2A2C', plot_bgcolor='#2A2A2C', uniformtext_minsize=12,
                                        uniformtext_mode='hide', )
                name_graph = "AnalyticByCountriesPieChart.html"
                write_html(pie_chart, name_graph)
                self.show_analytic_pie_chart(name_graph, data, 'short_country_name')
            else:
                self.ui.analytics_graps_widget.hide()
                self.activate_text_on_analytic_pie_chart()

    # Нажимаем на кнопку "Классы" и строим график классов на основе переданных данных.
    def grouping_by_instruments_type_pie_chart_analytical_page(self):
        if not current_df.empty:
            data = current_df.groupby('instrument_type').agg('sum')
            if not check_dt_is_empty(data):
                self.ui.analytics_graps_widget.show()
                self.disactivate_text_on_analytic_pie_chart()
                sectors = list(data.index)
                data = data.set_index(np.arange(0, len(data.index), 1))
                data['instrument_type'] = pd.Series(sectors)
                add_column_percantages(data)
                generate_color_column(data)
                data = data.sort_values('total_cost_percentage', ascending=False)
                pie_chart = px.pie(data_frame=data, values='total_cost_percentage', names='instrument_type',
                                   color='instrument_type', color_discrete_sequence=list(data['color']), hole=0.3)
                hovertemp = "%{label} "
                hovertemp += "%{value}            %"
                pie_chart.update_traces(hovertemplate=hovertemp)
                pie_chart.update_traces(textposition='inside', showlegend=False)
                pie_chart.update_layout(paper_bgcolor='#2A2A2C', plot_bgcolor='#2A2A2C', uniformtext_minsize=12,
                                        uniformtext_mode='hide', )
                name_graph = "AnalyticByInstrumentTypePieChart.html"
                write_html(pie_chart, name_graph)
                self.show_analytic_pie_chart(name_graph, data, 'instrument_type')
            else:
                self.ui.analytics_graps_widget.hide()
                self.activate_text_on_analytic_pie_chart()

    # Строим график на основе данных.
    def show_analytic_pie_chart(self, name_graph, dt, condition):
        with open(name_graph, 'r') as pie_char_html:
            self.analytic_pie_chart.setHtml(pie_char_html.read())
            self.analytic_pie_chart.setMinimumSize(335, 310)
            self.clear_legend_analytics_pie_chart()
            self.add_legend_analytic_pie_chart(dt, condition)

    def add_legend_analytic_pie_chart(self, df, condition):
        self.position_analytic_pie_chart_based_list.setAlignment(QtCore.Qt.AlignTop)
        colors = df['color'].tolist()
        costs = df['cost'].tolist()
        total_cost_pecentage = df['total_cost_percentage'].tolist()
        condition = df[condition].tolist()
        for i in range(len(colors)):
            frame_inst_1 = QFrame(self.ui.scrollAreaWidgetContents_2)
            # frame_inst = QFrame(self.scrollAreaWidgetContents_4)
            frame_inst_1.setObjectName("_inst_1" + str(i))
            frame_inst_1.setGeometry(QRect(5, 10, 100, 21))
            frame_inst_1.setFrameShape(QFrame.StyledPanel)
            frame_inst_1.setFrameShadow(QFrame.Raised)
            frame_inst_layout_1 = QHBoxLayout(frame_inst_1)
            frame_inst_1.setStyleSheet('''
                   background-color: #222226;
                   padding-left: 0px;
               ''')

            inst_color_1 = QFrame()
            inst_color_1.setObjectName("inst_color" + str(i))
            inst_color_1.setGeometry(QRect(10, 0, 16, 21))
            inst_color_1.setStyleSheet(f"font-size : 20px; font-family : Open Sans; background-color : {colors[i]};")
            # inst_color.setStyleSheet("font-size : 16px; font-family : Open Sans; background-color : #47F19F")
            inst_color_1.setFrameShape(QFrame.StyledPanel)
            inst_color_1.setFrameShadow(QFrame.Raised)
            inst_color_1.setMaximumSize(QSize(5, 16777215))
            inst_color_1.setContentsMargins(0, 0, 0, 0)
            frame_inst_layout_1.addWidget(inst_color_1)

            inst_name_1 = QLabel()
            inst_name_1.setText(
                condition[i] + "\n" + str(total_cost_pecentage[i]) + "%" + " " + str(round(costs[i], 2)) + "₽")
            inst_name_1.setObjectName("inst_name" + str(i))
            inst_name_1.setGeometry(QRect(30, 0, 141, 21))
            # inst_name.setMaximumSize(QSize(80, 16777215))
            inst_name_1.adjustSize()
            inst_name_1.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                      "")
            inst_name_1.setAlignment(Qt.AlignCenter)
            frame_inst_layout_1.addWidget(inst_name_1)
            self.position_analytic_pie_chart_based_list.addWidget(frame_inst_1)

    # Удаление фреймов из легенды
    def clear_legend_analytics_pie_chart(self):
        for i in reversed(range(self.position_analytic_pie_chart_based_list.count())):
            self.position_analytic_pie_chart_based_list.takeAt(i).widget().setParent(None)

    def disactivate_text_on_analytic_pie_chart(self):
        self.ui.analytic_graph_text_if_have_no_instr.setStyleSheet('color: #2A2A2C')

    def activate_text_on_analytic_pie_chart(self):
        self.ui.analytic_graph_text_if_have_no_instr.setStyleSheet('color: #F9F9FB')

    full_df = pd.DataFrame()
    current_df = pd.DataFrame()
    all_instruments_df = pd.DataFrame()
    request_from_currencies = False

    def fill_analyt_page(self, list_positions):
        if len(list_positions) == 0:
            return
        # Графики на странице аналитики.
        global full_df
        full_df = pd.DataFrame(list_positions)
        global current_df
        current_df = pd.DataFrame(list_positions)
        self.link_analytic_buttons(current_df)
        global request_from_currencies
        request_from_currencies = False
        self.grouping_by_currencies_pie_chart_analytical_page()
        # Рекомендации.

        # Все инструменты.
        self.fill_all_instruments_on_analytic_page()

    def fill_all_instruments_on_analytic_page(self):
        global full_df
        full_df = full_df.sort_values('cost', ascending=False)
        if not full_df.empty:
            self.all_instruments_analytic_page_list.setAlignment(QtCore.Qt.AlignTop)
            shares_df =full_df[full_df['instrument_type'] == 'Акция']
            if not shares_df.empty:
                shares_df = shares_df.set_index(np.arange(0, len(shares_df.index), 1))
                frame_shares = create_shares_frame_on_analytic_page(shares_df)
                self.all_instruments_analytic_page_list.addWidget(frame_shares)
            else:
                pass

            bonds_df = full_df[full_df['instrument_type'] == 'Облигация']
            if not bonds_df.empty:
                bonds_df = bonds_df.set_index(np.arange(0, len(bonds_df.index), 1))
                frame_bonds = create_bonds_frame_on_analytic_page(bonds_df)
                self.all_instruments_analytic_page_list.addWidget(frame_bonds)
            else:
                pass
            etf_df = full_df[full_df['instrument_type'] == 'Фонд']
            if not etf_df.empty:
                etf_df = etf_df.set_index(np.arange(0, len(etf_df.index), 1))
                frame_shares = create_etfs_frame_on_analytic_page(etf_df)
                self.all_instruments_analytic_page_list.addWidget(frame_shares)
            else:
                pass
            currencies_df = full_df[full_df['instrument_type'] == 'Валюта']
            if not etf_df.empty:
                currencies_df = currencies_df.set_index(np.arange(0, len(currencies_df.index), 1))
                frame_shares = create_currencies_frame_on_analytic_page(currencies_df)
                self.all_instruments_analytic_page_list.addWidget(frame_shares)
            else:
                pass

    def clear_all_instruments_on_analytic_page(self):
        for i in reversed(range(self.all_instruments_analytic_page_list.count())):
            self.all_instruments_analytic_page_list.takeAt(i).widget().setParent(None)

    def fill_portfolio(self, token, account):
        sender = self.sender()
        with Client(token) as client:
            portfolio = client.operations.get_portfolio(account_id=account.id)
            self.fill_main_page(portfolio, token, client)


if __name__ == "__main__":
    # sys.argv.append("--disable-web-security")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
