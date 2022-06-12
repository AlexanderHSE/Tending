from PySide2 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, QDir, QUrlQuery)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from help_func import check_float

minus_profit = "#FAA2A2"  # hex red color
zero_porfit = "#F9F9FB"  # hex white color
plus_profit = "#47F19F "  # hex green color

def create_shares_frame_on_analytic_page(df):
    frame_instruments = QFrame()
    frame_instruments.setObjectName("frame_instruments")
    frame_instruments.setFrameShape(QFrame.StyledPanel)
    frame_instruments.setFrameShadow(QFrame.Raised)
    frame_instruments.setStyleSheet('''
            background-color: #222226;
            padding-left: 0px;
        ''')
    frame_instruments_layout = QVBoxLayout(frame_instruments)

    frame_instruments_title = QLabel()
    frame_instruments_title.setText("Акции")
    frame_instruments_title.setObjectName("frame_title_shares")
    frame_instruments_title.setGeometry(QRect(0, 0, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_title.adjustSize()
    frame_instruments_title.setStyleSheet(u"font-size : 16px; font-family : Open Sans; color : #F9F9FB\n"
                                     "")
    frame_instruments_title.setAlignment(Qt.AlignCenter)
    frame_instruments_layout.addWidget(frame_instruments_title)

    frame_instruments_columns_titles = QFrame()
    frame_instruments_columns_titles.setObjectName("frame_instruments_columns_titles")
    frame_instruments_columns_titles.setFrameShape(QFrame.StyledPanel)
    frame_instruments_columns_titles.setFrameShadow(QFrame.Raised)
    frame_instruments_columns_titles.setStyleSheet('''
                   background-color: #2A2A2C;
                   padding-left: 0px;
               ''')
    frame_instruments_name_columns_layout = QHBoxLayout(frame_instruments_columns_titles)

    frame_instruments_columns_titles_name = QLabel()
    frame_instruments_columns_titles_name.setText("Название")
    frame_instruments_columns_titles_name.setObjectName("frame_instruments_columns_titles_name")
    frame_instruments_columns_titles_name.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_name.adjustSize()
    frame_instruments_columns_titles_name.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                                   "")
    frame_instruments_columns_titles_name.setAlignment(Qt.AlignLeft)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_name)

    frame_instruments_columns_titles_ticker = QLabel()
    frame_instruments_columns_titles_ticker.setText("Тикер")
    frame_instruments_columns_titles_ticker.setObjectName("frame_instruments_columns_titles_name")
    frame_instruments_columns_titles_ticker.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_ticker.adjustSize()
    frame_instruments_columns_titles_ticker.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                                     "")
    frame_instruments_columns_titles_ticker.setAlignment(Qt.AlignLeft)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_ticker)

    frame_instruments_columns_titles_country = QLabel()
    frame_instruments_columns_titles_country.setText("Страна")
    frame_instruments_columns_titles_country.setObjectName("frame_shares_columns_titles_country")
    frame_instruments_columns_titles_country.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_country.adjustSize()
    frame_instruments_columns_titles_country.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                                      "")
    frame_instruments_columns_titles_country.setAlignment(Qt.AlignLeft)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_country)
    
    frame_instruments_columns_titles_sectors = QLabel()
    frame_instruments_columns_titles_sectors.setText("Сектор")
    frame_instruments_columns_titles_sectors.setObjectName("frame_shares_columns_titles_country")
    frame_instruments_columns_titles_sectors.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_sectors.adjustSize()
    frame_instruments_columns_titles_sectors.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_sectors.setAlignment(Qt.AlignLeft)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_sectors)
    
    frame_instruments_columns_titles_quantity = QLabel()
    frame_instruments_columns_titles_quantity.setText("Количество")
    frame_instruments_columns_titles_quantity.setObjectName("frame_shares_columns_titles_quantity")
    frame_instruments_columns_titles_quantity.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_quantity.adjustSize()
    frame_instruments_columns_titles_quantity.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_quantity.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_quantity)
    
    frame_instruments_columns_titles_current_cost = QLabel()
    frame_instruments_columns_titles_current_cost.setText("Тек. цена")
    frame_instruments_columns_titles_current_cost.setObjectName("frame_shares_columns_titles_current_cost")
    frame_instruments_columns_titles_current_cost.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_current_cost.adjustSize()
    frame_instruments_columns_titles_current_cost.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_current_cost.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_current_cost)
    
    frame_instruments_columns_titles_average_cost = QLabel()
    frame_instruments_columns_titles_average_cost.setText("Сред. цена")
    frame_instruments_columns_titles_average_cost.setObjectName("frame_shares_columns_titles_average_cost")
    frame_instruments_columns_titles_average_cost.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_average_cost.adjustSize()
    frame_instruments_columns_titles_average_cost.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_average_cost.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_average_cost)
    
    frame_instruments_columns_titles_total_cost = QLabel()
    frame_instruments_columns_titles_total_cost.setText("Стоимость")
    frame_instruments_columns_titles_total_cost.setObjectName("frame_instruments_columns_titles_total_cost")
    frame_instruments_columns_titles_total_cost.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_total_cost.adjustSize()
    frame_instruments_columns_titles_total_cost.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_total_cost.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_total_cost)
    
    frame_instruments_columns_titles_profit = QLabel()
    frame_instruments_columns_titles_profit.setText("Прибыль")
    frame_instruments_columns_titles_profit.setObjectName("frame_shares_columns_titles_profit")
    frame_instruments_columns_titles_profit.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_profit.adjustSize()
    frame_instruments_columns_titles_profit.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_profit.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_profit)
    
    frame_instruments_columns_titles_profit_percentage = QLabel()
    frame_instruments_columns_titles_profit_percentage.setText("Доходность")
    frame_instruments_columns_titles_profit_percentage.setObjectName("frame_shares_columns_titles_profit_percentage")
    frame_instruments_columns_titles_profit_percentage.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_profit_percentage.adjustSize()
    frame_instruments_columns_titles_profit_percentage.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_profit_percentage.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_profit_percentage)
    
    frame_instruments_columns_titles_share_percentage = QLabel()
    frame_instruments_columns_titles_share_percentage.setText("Доля в портфеле")
    frame_instruments_columns_titles_share_percentage.setObjectName("frame_shares_columns_titles_share_percentage")
    frame_instruments_columns_titles_share_percentage.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_share_percentage.adjustSize()
    frame_instruments_columns_titles_share_percentage.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_share_percentage.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_share_percentage)

    frame_instruments_layout.addWidget(frame_instruments_columns_titles)

    c = 0
    for indexRow in range(len(df.index)):
        row = df.iloc[indexRow]
        c += 1
        frame_instrument = QFrame()
        # frame_inst = QFrame(self.scrollAreaWidgetContents_4)
        frame_instrument.setObjectName("instr_share" + str(c))
        frame_instrument.setGeometry(QRect(0, 0, 401, 41))
        frame_instrument.setFrameShape(QFrame.StyledPanel)
        frame_instrument.setFrameShadow(QFrame.Raised)
        frame_inst_layout = QHBoxLayout(frame_instrument)
        frame_instrument.setStyleSheet('''
            background-color: #2A2A2C;
            padding-left: 0px;
        ''')

        inst_name = QLabel()
        inst_name.setText(row['name'])
        inst_name.setObjectName("inst_name" + str(c))
        inst_name.setGeometry(QRect(10, -10, 51, 61))
        # inst_name.setMaximumSize(QSize(80, 16777215))
        inst_name.adjustSize()
        inst_name.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                "")
        inst_name.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_name)

        inst_ticker = QLabel()
        inst_ticker.setText(row['ticker'])
        inst_ticker.setObjectName("inst_ticker" + str(c))
        inst_ticker.setGeometry(QRect(10, -10, 20, 61))
        # inst_name.setMaximumSize(QSize(80, 16777215))
        inst_ticker.adjustSize()
        inst_ticker.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                  "")
        inst_ticker.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_ticker)

        inst_country = QLabel()
        inst_country.setText(row['short_country_name'])
        inst_country.setObjectName("inst_short_country_name" + str(c))
        inst_country.setGeometry(QRect(80, -10, 21, 61))
        # inst_type.setMaximumSize(QSize(65, 16777215))
        inst_country.adjustSize()
        inst_country.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                   "")
        inst_country.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_country)

        inst_sector = QLabel()
        inst_sector.setText(row['sector'])
        inst_sector.setObjectName("inst_sector" + str(c))
        inst_sector.setGeometry(QRect(80, -10, 21, 61))
        # inst_type.setMaximumSize(QSize(65, 16777215))
        inst_sector.adjustSize()
        inst_sector.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                  "")
        inst_sector.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_sector)

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
        inst_quan.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_quan)

        inst_current_buy_price = QLabel()
        inst_current_buy_price.setText(str(round(row['current_buy_price'], 2)) + "₽")
        inst_current_buy_price.setObjectName("inst_current_buy_price" + str(c))
        inst_current_buy_price.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_current_buy_price.adjustSize()
        inst_current_buy_price.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                             "")
        inst_current_buy_price.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_current_buy_price)

        inst_average_buy_price = QLabel()
        inst_average_buy_price.setText(str(round(row['average_buy_price'], 2)) + "₽")
        inst_average_buy_price.setObjectName("inst_inst_average_buy_price" + str(c))
        inst_average_buy_price.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_average_buy_price.adjustSize()
        inst_average_buy_price.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                             "")
        inst_average_buy_price.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_average_buy_price)

        inst_cost = QLabel()
        inst_cost.setText(str(round(row['cost'], 2)) + "₽")
        inst_cost.setObjectName("inst_cost" + str(c))
        inst_cost.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_cost.adjustSize()
        inst_cost.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                "")
        inst_cost.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_cost)

        inst_expected_yield = QLabel()
        inst_expected_yield_percentage = QLabel()
        if row['expected_yield'] < 0:
            inst_expected_yield.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {minus_profit}")
            inst_expected_yield_percentage.setStyleSheet(
                f"font-size : 13px; font-family : Open Sans; color : {minus_profit}")
            # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {minus_profit}")
        elif row['expected_yield'] == 0:
            inst_expected_yield.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {zero_porfit}")
            inst_expected_yield_percentage.setStyleSheet(
                f"font-size : 13px; font-family : Open Sans; color : {zero_porfit}")
            # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {zero_porfit}")
        elif row['expected_yield'] > 0:
            inst_expected_yield.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {plus_profit}")
            inst_expected_yield_percentage.setStyleSheet(
                f"font-size : 13px; font-family : Open Sans; color : {plus_profit}")
            # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {plus_profit}")
        inst_expected_yield.setText(str(round(row['expected_yield'], 2)) + "₽")
        inst_expected_yield.setObjectName("inst_expected_yield" + str(c))
        inst_expected_yield.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_expected_yield.adjustSize()
        inst_expected_yield.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_expected_yield)

        inst_expected_yield_percentage.setText(str(round(row['expected_yield_percentage'], 2)) + "%")
        inst_expected_yield_percentage.setObjectName("inst_expected_yield" + str(c))
        inst_expected_yield_percentage.setGeometry(QRect(190, -10, 48, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_expected_yield_percentage.adjustSize()
        inst_expected_yield_percentage.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_expected_yield_percentage)

        inst_percent = QLabel()
        inst_percent.setText(str(round(row['portfolio_share'], 2)) + "%")
        inst_percent.setObjectName("inst_percent" + str(c))
        inst_percent.setGeometry(QRect(340, -20, 48, 61))
        inst_percent.setMaximumSize(QSize(56, 16777215))
        inst_percent.adjustSize()
        inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {zero_porfit}")
        inst_percent.setAlignment(Qt.AlignRight)
        inst_percent.setContentsMargins(0, 0, 0, 0)
        frame_inst_layout.addWidget(inst_percent)

        frame_instruments_layout.addWidget(frame_instrument)
    return frame_instruments

def create_bonds_frame_on_analytic_page(df):
    frame_instruments = QFrame()
    frame_instruments.setObjectName("frame_instruments")
    frame_instruments.setFrameShape(QFrame.StyledPanel)
    frame_instruments.setFrameShadow(QFrame.Raised)
    frame_instruments.setStyleSheet('''
                background-color: #222226;
                padding-left: 0px;
            ''')
    frame_instruments_layout = QVBoxLayout(frame_instruments)

    frame_instruments_title = QLabel()
    frame_instruments_title.setText("Облигации")
    frame_instruments_title.setObjectName("frame_title_shares")
    frame_instruments_title.setGeometry(QRect(0, 0, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_title.adjustSize()
    frame_instruments_title.setStyleSheet(u"font-size : 16px; font-family : Open Sans; color : #F9F9FB\n"
                                          "")
    frame_instruments_title.setAlignment(Qt.AlignCenter)
    frame_instruments_layout.addWidget(frame_instruments_title)

    frame_instruments_columns_titles = QFrame()
    frame_instruments_columns_titles.setObjectName("frame_instruments_columns_titles")
    frame_instruments_columns_titles.setFrameShape(QFrame.StyledPanel)
    frame_instruments_columns_titles.setFrameShadow(QFrame.Raised)
    frame_instruments_columns_titles.setStyleSheet('''
                       background-color: #2A2A2C;
                       padding-left: 0px;
                   ''')
    frame_instruments_name_columns_layout = QHBoxLayout(frame_instruments_columns_titles)

    frame_instruments_columns_titles_name = QLabel()
    frame_instruments_columns_titles_name.setText("Название")
    frame_instruments_columns_titles_name.setObjectName("frame_instruments_columns_titles_name")
    frame_instruments_columns_titles_name.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_name.adjustSize()
    frame_instruments_columns_titles_name.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                                        "")
    frame_instruments_columns_titles_name.setAlignment(Qt.AlignLeft)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_name)


    frame_instruments_columns_titles_country = QLabel()
    frame_instruments_columns_titles_country.setText("Страна")
    frame_instruments_columns_titles_country.setObjectName("frame_shares_columns_titles_country")
    frame_instruments_columns_titles_country.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_country.adjustSize()
    frame_instruments_columns_titles_country.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_country.setAlignment(Qt.AlignLeft)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_country)

    frame_instruments_columns_titles_quantity = QLabel()
    frame_instruments_columns_titles_quantity.setText("Количество")
    frame_instruments_columns_titles_quantity.setObjectName("frame_shares_columns_titles_quantity")
    frame_instruments_columns_titles_quantity.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_quantity.adjustSize()
    frame_instruments_columns_titles_quantity.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_quantity.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_quantity)

    frame_instruments_columns_titles_current_cost = QLabel()
    frame_instruments_columns_titles_current_cost.setText("Тек. цена")
    frame_instruments_columns_titles_current_cost.setObjectName("frame_shares_columns_titles_current_cost")
    frame_instruments_columns_titles_current_cost.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_current_cost.adjustSize()
    frame_instruments_columns_titles_current_cost.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_current_cost.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_current_cost)

    frame_instruments_columns_titles_average_cost = QLabel()
    frame_instruments_columns_titles_average_cost.setText("Сред. цена")
    frame_instruments_columns_titles_average_cost.setObjectName("frame_shares_columns_titles_average_cost")
    frame_instruments_columns_titles_average_cost.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_average_cost.adjustSize()
    frame_instruments_columns_titles_average_cost.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_average_cost.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_average_cost)

    frame_instruments_columns_titles_nkd = QLabel()
    frame_instruments_columns_titles_nkd.setText("НКД")
    frame_instruments_columns_titles_nkd.setObjectName("frame_instruments_columns_titles_name")
    frame_instruments_columns_titles_nkd.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_nkd.adjustSize()
    frame_instruments_columns_titles_nkd.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_nkd.setAlignment(Qt.AlignCenter)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_nkd)

    frame_instruments_columns_titles_total_cost = QLabel()
    frame_instruments_columns_titles_total_cost.setText("Стоимость")
    frame_instruments_columns_titles_total_cost.setObjectName("frame_instruments_columns_titles_total_cost")
    frame_instruments_columns_titles_total_cost.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_total_cost.adjustSize()
    frame_instruments_columns_titles_total_cost.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_total_cost.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_total_cost)

    frame_instruments_columns_titles_profit = QLabel()
    frame_instruments_columns_titles_profit.setText("Прибыль")
    frame_instruments_columns_titles_profit.setObjectName("frame_shares_columns_titles_profit")
    frame_instruments_columns_titles_profit.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_profit.adjustSize()
    frame_instruments_columns_titles_profit.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_profit.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_profit)

    frame_instruments_columns_titles_profit_percentage = QLabel()
    frame_instruments_columns_titles_profit_percentage.setText("Доходность")
    frame_instruments_columns_titles_profit_percentage.setObjectName("frame_shares_columns_titles_profit_percentage")
    frame_instruments_columns_titles_profit_percentage.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_profit_percentage.adjustSize()
    frame_instruments_columns_titles_profit_percentage.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_profit_percentage.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_profit_percentage)

    frame_instruments_columns_titles_share_percentage = QLabel()
    frame_instruments_columns_titles_share_percentage.setText("Доля в портфеле")
    frame_instruments_columns_titles_share_percentage.setObjectName("frame_shares_columns_titles_share_percentage")
    frame_instruments_columns_titles_share_percentage.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_share_percentage.adjustSize()
    frame_instruments_columns_titles_share_percentage.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_share_percentage.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_share_percentage)

    frame_instruments_layout.addWidget(frame_instruments_columns_titles)

    c = 0
    for indexRow in range(len(df.index)):
        row = df.iloc[indexRow]
        c += 1
        frame_instrument = QFrame()
        # frame_inst = QFrame(self.scrollAreaWidgetContents_4)
        frame_instrument.setObjectName("instr_share" + str(c))
        frame_instrument.setGeometry(QRect(0, 0, 401, 41))
        frame_instrument.setFrameShape(QFrame.StyledPanel)
        frame_instrument.setFrameShadow(QFrame.Raised)
        frame_inst_layout = QHBoxLayout(frame_instrument)
        frame_instrument.setStyleSheet('''
                background-color: #2A2A2C;
                padding-left: 0px;
            ''')

        inst_name = QLabel()
        inst_name.setText(row['name'])
        inst_name.setObjectName("inst_name" + str(c))
        inst_name.setGeometry(QRect(10, -10, 51, 61))
        # inst_name.setMaximumSize(QSize(80, 16777215))
        inst_name.adjustSize()
        inst_name.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                "")
        inst_name.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_name)

        inst_country = QLabel()
        inst_country.setText(row['short_country_name'])
        inst_country.setObjectName("inst_short_country_name" + str(c))
        inst_country.setGeometry(QRect(80, -10, 21, 61))
        # inst_type.setMaximumSize(QSize(65, 16777215))
        inst_country.adjustSize()
        inst_country.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                   "")
        inst_country.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_country)

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
        inst_quan.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_quan)

        inst_current_buy_price = QLabel()
        inst_current_buy_price.setText(str(round(row['current_buy_price'], 2)) + "₽")
        inst_current_buy_price.setObjectName("inst_current_buy_price" + str(c))
        inst_current_buy_price.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_current_buy_price.adjustSize()
        inst_current_buy_price.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                             "")
        inst_current_buy_price.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_current_buy_price)

        inst_average_buy_price = QLabel()
        inst_average_buy_price.setText(str(round(row['average_buy_price'], 2)) + "₽")
        inst_average_buy_price.setObjectName("inst_inst_average_buy_price" + str(c))
        inst_average_buy_price.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_average_buy_price.adjustSize()
        inst_average_buy_price.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                             "")
        inst_average_buy_price.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_average_buy_price)

        inst_nkd_price = QLabel()
        inst_nkd_price.setText(str(round(row['nkd'], 2)) + "₽")
        inst_nkd_price.setObjectName("inst_nkd" + str(c))
        inst_nkd_price.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_nkd_price.adjustSize()
        inst_nkd_price.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                             "")
        inst_nkd_price.setAlignment(Qt.AlignCenter)
        frame_inst_layout.addWidget(inst_nkd_price)

        inst_cost = QLabel()
        inst_cost.setText(str(round(row['cost'], 2)) + "₽")
        inst_cost.setObjectName("inst_cost" + str(c))
        inst_cost.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_cost.adjustSize()
        inst_cost.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                "")
        inst_cost.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_cost)

        inst_expected_yield = QLabel()
        inst_expected_yield_percentage = QLabel()
        if row['expected_yield'] < 0:
            inst_expected_yield.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {minus_profit}")
            inst_expected_yield_percentage.setStyleSheet(
                f"font-size : 13px; font-family : Open Sans; color : {minus_profit}")
            # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {minus_profit}")
        elif row['expected_yield'] == 0:
            inst_expected_yield.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {zero_porfit}")
            inst_expected_yield_percentage.setStyleSheet(
                f"font-size : 13px; font-family : Open Sans; color : {zero_porfit}")
            # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {zero_porfit}")
        elif row['expected_yield'] > 0:
            inst_expected_yield.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {plus_profit}")
            inst_expected_yield_percentage.setStyleSheet(
                f"font-size : 13px; font-family : Open Sans; color : {plus_profit}")
            # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {plus_profit}")
        inst_expected_yield.setText(str(round(row['expected_yield'], 2)) + "₽")
        inst_expected_yield.setObjectName("inst_expected_yield" + str(c))
        inst_expected_yield.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_expected_yield.adjustSize()
        inst_expected_yield.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_expected_yield)

        inst_expected_yield_percentage.setText(str(round(row['expected_yield_percentage'], 2)) + "%")
        inst_expected_yield_percentage.setObjectName("inst_expected_yield" + str(c))
        inst_expected_yield_percentage.setGeometry(QRect(190, -10, 48, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_expected_yield_percentage.adjustSize()
        inst_expected_yield_percentage.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_expected_yield_percentage)

        inst_percent = QLabel()
        inst_percent.setText(str(round(row['portfolio_share'], 2)) + "%")
        inst_percent.setObjectName("inst_percent" + str(c))
        inst_percent.setGeometry(QRect(340, -20, 48, 61))
        inst_percent.setMaximumSize(QSize(56, 16777215))
        inst_percent.adjustSize()
        inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {zero_porfit}")
        inst_percent.setAlignment(Qt.AlignRight)
        inst_percent.setContentsMargins(0, 0, 0, 0)
        frame_inst_layout.addWidget(inst_percent)

        frame_instruments_layout.addWidget(frame_instrument)
    return frame_instruments

def create_etfs_frame_on_analytic_page(df):
    frame_instruments = QFrame()
    frame_instruments.setObjectName("frame_instruments")
    frame_instruments.setFrameShape(QFrame.StyledPanel)
    frame_instruments.setFrameShadow(QFrame.Raised)
    frame_instruments.setStyleSheet('''
                background-color: #222226;
                padding-left: 0px;
            ''')
    frame_instruments_layout = QVBoxLayout(frame_instruments)

    frame_instruments_title = QLabel()
    frame_instruments_title.setText("Фонды")
    frame_instruments_title.setObjectName("frame_title_shares")
    frame_instruments_title.setGeometry(QRect(0, 0, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_title.adjustSize()
    frame_instruments_title.setStyleSheet(u"font-size : 16px; font-family : Open Sans; color : #F9F9FB\n"
                                          "")
    frame_instruments_title.setAlignment(Qt.AlignCenter)
    frame_instruments_layout.addWidget(frame_instruments_title)

    frame_instruments_columns_titles = QFrame()
    frame_instruments_columns_titles.setObjectName("frame_instruments_columns_titles")
    frame_instruments_columns_titles.setFrameShape(QFrame.StyledPanel)
    frame_instruments_columns_titles.setFrameShadow(QFrame.Raised)
    frame_instruments_columns_titles.setStyleSheet('''
                       background-color: #2A2A2C;
                       padding-left: 0px;
                   ''')
    frame_instruments_name_columns_layout = QHBoxLayout(frame_instruments_columns_titles)

    frame_instruments_columns_titles_name = QLabel()
    frame_instruments_columns_titles_name.setText("Название")
    frame_instruments_columns_titles_name.setObjectName("frame_instruments_columns_titles_name")
    frame_instruments_columns_titles_name.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_name.adjustSize()
    frame_instruments_columns_titles_name.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                                        "")
    frame_instruments_columns_titles_name.setAlignment(Qt.AlignLeft)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_name)

    frame_instruments_columns_titles_ticker = QLabel()
    frame_instruments_columns_titles_ticker.setText("Тикер")
    frame_instruments_columns_titles_ticker.setObjectName("frame_instruments_columns_titles_name")
    frame_instruments_columns_titles_ticker.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_ticker.adjustSize()
    frame_instruments_columns_titles_ticker.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_ticker.setAlignment(Qt.AlignLeft)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_ticker)

    frame_instruments_columns_titles_country = QLabel()
    frame_instruments_columns_titles_country.setText("Страна")
    frame_instruments_columns_titles_country.setObjectName("frame_shares_columns_titles_country")
    frame_instruments_columns_titles_country.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_country.adjustSize()
    frame_instruments_columns_titles_country.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_country.setAlignment(Qt.AlignLeft)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_country)


    frame_instruments_columns_titles_quantity = QLabel()
    frame_instruments_columns_titles_quantity.setText("Количество")
    frame_instruments_columns_titles_quantity.setObjectName("frame_shares_columns_titles_quantity")
    frame_instruments_columns_titles_quantity.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_quantity.adjustSize()
    frame_instruments_columns_titles_quantity.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_quantity.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_quantity)

    frame_instruments_columns_titles_current_cost = QLabel()
    frame_instruments_columns_titles_current_cost.setText("Тек. цена")
    frame_instruments_columns_titles_current_cost.setObjectName("frame_shares_columns_titles_current_cost")
    frame_instruments_columns_titles_current_cost.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_current_cost.adjustSize()
    frame_instruments_columns_titles_current_cost.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_current_cost.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_current_cost)

    frame_instruments_columns_titles_average_cost = QLabel()
    frame_instruments_columns_titles_average_cost.setText("Сред. цена")
    frame_instruments_columns_titles_average_cost.setObjectName("frame_shares_columns_titles_average_cost")
    frame_instruments_columns_titles_average_cost.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_average_cost.adjustSize()
    frame_instruments_columns_titles_average_cost.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_average_cost.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_average_cost)

    frame_instruments_columns_titles_total_cost = QLabel()
    frame_instruments_columns_titles_total_cost.setText("Стоимость")
    frame_instruments_columns_titles_total_cost.setObjectName("frame_instruments_columns_titles_total_cost")
    frame_instruments_columns_titles_total_cost.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_total_cost.adjustSize()
    frame_instruments_columns_titles_total_cost.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_total_cost.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_total_cost)

    frame_instruments_columns_titles_profit = QLabel()
    frame_instruments_columns_titles_profit.setText("Прибыль")
    frame_instruments_columns_titles_profit.setObjectName("frame_shares_columns_titles_profit")
    frame_instruments_columns_titles_profit.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_profit.adjustSize()
    frame_instruments_columns_titles_profit.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_profit.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_profit)

    frame_instruments_columns_titles_profit_percentage = QLabel()
    frame_instruments_columns_titles_profit_percentage.setText("Доходность")
    frame_instruments_columns_titles_profit_percentage.setObjectName("frame_shares_columns_titles_profit_percentage")
    frame_instruments_columns_titles_profit_percentage.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_profit_percentage.adjustSize()
    frame_instruments_columns_titles_profit_percentage.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_profit_percentage.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_profit_percentage)

    frame_instruments_columns_titles_share_percentage = QLabel()
    frame_instruments_columns_titles_share_percentage.setText("Доля в портфеле")
    frame_instruments_columns_titles_share_percentage.setObjectName("frame_shares_columns_titles_share_percentage")
    frame_instruments_columns_titles_share_percentage.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_share_percentage.adjustSize()
    frame_instruments_columns_titles_share_percentage.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_share_percentage.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_share_percentage)

    frame_instruments_layout.addWidget(frame_instruments_columns_titles)

    c = 0
    for indexRow in range(len(df.index)):
        row = df.iloc[indexRow]
        c += 1
        frame_instrument = QFrame()
        # frame_inst = QFrame(self.scrollAreaWidgetContents_4)
        frame_instrument.setObjectName("instr_share" + str(c))
        frame_instrument.setGeometry(QRect(0, 0, 401, 41))
        frame_instrument.setFrameShape(QFrame.StyledPanel)
        frame_instrument.setFrameShadow(QFrame.Raised)
        frame_inst_layout = QHBoxLayout(frame_instrument)
        frame_instrument.setStyleSheet('''
                background-color: #2A2A2C;
                padding-left: 0px;
            ''')

        inst_name = QLabel()
        inst_name.setText(row['name'])
        inst_name.setObjectName("inst_name" + str(c))
        inst_name.setGeometry(QRect(10, -10, 51, 61))
        # inst_name.setMaximumSize(QSize(80, 16777215))
        inst_name.adjustSize()
        inst_name.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                "")
        inst_name.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_name)

        inst_ticker = QLabel()
        inst_ticker.setText(row['ticker'])
        inst_ticker.setObjectName("inst_ticker" + str(c))
        inst_ticker.setGeometry(QRect(10, -10, 20, 61))
        # inst_name.setMaximumSize(QSize(80, 16777215))
        inst_ticker.adjustSize()
        inst_ticker.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                  "")
        inst_ticker.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_ticker)

        inst_country = QLabel()
        inst_country.setText(row['short_country_name'])
        inst_country.setObjectName("inst_short_country_name" + str(c))
        inst_country.setGeometry(QRect(80, -10, 21, 61))
        # inst_type.setMaximumSize(QSize(65, 16777215))
        inst_country.adjustSize()
        inst_country.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                   "")
        inst_country.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_country)


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
        inst_quan.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_quan)

        inst_current_buy_price = QLabel()
        inst_current_buy_price.setText(str(round(row['current_buy_price'], 2)) + "₽")
        inst_current_buy_price.setObjectName("inst_current_buy_price" + str(c))
        inst_current_buy_price.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_current_buy_price.adjustSize()
        inst_current_buy_price.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                             "")
        inst_current_buy_price.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_current_buy_price)

        inst_average_buy_price = QLabel()
        inst_average_buy_price.setText(str(round(row['average_buy_price'], 2)) + "₽")
        inst_average_buy_price.setObjectName("inst_inst_average_buy_price" + str(c))
        inst_average_buy_price.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_average_buy_price.adjustSize()
        inst_average_buy_price.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                             "")
        inst_average_buy_price.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_average_buy_price)

        inst_cost = QLabel()
        inst_cost.setText(str(round(row['cost'], 2)) + "₽")
        inst_cost.setObjectName("inst_cost" + str(c))
        inst_cost.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_cost.adjustSize()
        inst_cost.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                "")
        inst_cost.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_cost)

        inst_expected_yield = QLabel()
        inst_expected_yield_percentage = QLabel()
        if row['expected_yield'] < 0:
            inst_expected_yield.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {minus_profit}")
            inst_expected_yield_percentage.setStyleSheet(
                f"font-size : 13px; font-family : Open Sans; color : {minus_profit}")
            # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {minus_profit}")
        elif row['expected_yield'] == 0:
            inst_expected_yield.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {zero_porfit}")
            inst_expected_yield_percentage.setStyleSheet(
                f"font-size : 13px; font-family : Open Sans; color : {zero_porfit}")
            # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {zero_porfit}")
        elif row['expected_yield'] > 0:
            inst_expected_yield.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {plus_profit}")
            inst_expected_yield_percentage.setStyleSheet(
                f"font-size : 13px; font-family : Open Sans; color : {plus_profit}")
            # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {plus_profit}")
        inst_expected_yield.setText(str(round(row['expected_yield'], 2)) + "₽")
        inst_expected_yield.setObjectName("inst_expected_yield" + str(c))
        inst_expected_yield.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_expected_yield.adjustSize()
        inst_expected_yield.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_expected_yield)

        inst_expected_yield_percentage.setText(str(round(row['expected_yield_percentage'], 2)) + "%")
        inst_expected_yield_percentage.setObjectName("inst_expected_yield" + str(c))
        inst_expected_yield_percentage.setGeometry(QRect(190, -10, 48, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_expected_yield_percentage.adjustSize()
        inst_expected_yield_percentage.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_expected_yield_percentage)

        inst_percent = QLabel()
        inst_percent.setText(str(round(row['portfolio_share'], 2)) + "%")
        inst_percent.setObjectName("inst_percent" + str(c))
        inst_percent.setGeometry(QRect(340, -20, 48, 61))
        inst_percent.setMaximumSize(QSize(56, 16777215))
        inst_percent.adjustSize()
        inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {zero_porfit}")
        inst_percent.setAlignment(Qt.AlignRight)
        inst_percent.setContentsMargins(0, 0, 0, 0)
        frame_inst_layout.addWidget(inst_percent)

        frame_instruments_layout.addWidget(frame_instrument)
    return frame_instruments

def create_currencies_frame_on_analytic_page(df):
    frame_instruments = QFrame()
    frame_instruments.setObjectName("frame_instruments")
    frame_instruments.setFrameShape(QFrame.StyledPanel)
    frame_instruments.setFrameShadow(QFrame.Raised)
    frame_instruments.setStyleSheet('''
                background-color: #222226;
                padding-left: 0px;
            ''')
    frame_instruments_layout = QVBoxLayout(frame_instruments)

    frame_instruments_title = QLabel()
    frame_instruments_title.setText("Валюты")
    frame_instruments_title.setObjectName("frame_title_shares")
    frame_instruments_title.setGeometry(QRect(0, 0, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_title.adjustSize()
    frame_instruments_title.setStyleSheet(u"font-size : 16px; font-family : Open Sans; color : #F9F9FB\n"
                                          "")
    frame_instruments_title.setAlignment(Qt.AlignCenter)
    frame_instruments_layout.addWidget(frame_instruments_title)

    frame_instruments_columns_titles = QFrame()
    frame_instruments_columns_titles.setObjectName("frame_instruments_columns_titles")
    frame_instruments_columns_titles.setFrameShape(QFrame.StyledPanel)
    frame_instruments_columns_titles.setFrameShadow(QFrame.Raised)
    frame_instruments_columns_titles.setStyleSheet('''
                       background-color: #2A2A2C;
                       padding-left: 0px;
                   ''')
    frame_instruments_name_columns_layout = QHBoxLayout(frame_instruments_columns_titles)

    frame_instruments_columns_titles_name = QLabel()
    frame_instruments_columns_titles_name.setText("Название")
    frame_instruments_columns_titles_name.setObjectName("frame_instruments_columns_titles_name")
    frame_instruments_columns_titles_name.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_name.adjustSize()
    frame_instruments_columns_titles_name.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                                        "")
    frame_instruments_columns_titles_name.setAlignment(Qt.AlignLeft)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_name)


    frame_instruments_columns_titles_quantity = QLabel()
    frame_instruments_columns_titles_quantity.setText("Количество")
    frame_instruments_columns_titles_quantity.setObjectName("frame_shares_columns_titles_quantity")
    frame_instruments_columns_titles_quantity.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_quantity.adjustSize()
    frame_instruments_columns_titles_quantity.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_quantity.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_quantity)

    frame_instruments_columns_titles_current_cost = QLabel()
    frame_instruments_columns_titles_current_cost.setText("Тек. цена")
    frame_instruments_columns_titles_current_cost.setObjectName("frame_shares_columns_titles_current_cost")
    frame_instruments_columns_titles_current_cost.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_current_cost.adjustSize()
    frame_instruments_columns_titles_current_cost.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_current_cost.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_current_cost)

    frame_instruments_columns_titles_average_cost = QLabel()
    frame_instruments_columns_titles_average_cost.setText("Сред. цена")
    frame_instruments_columns_titles_average_cost.setObjectName("frame_shares_columns_titles_average_cost")
    frame_instruments_columns_titles_average_cost.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_average_cost.adjustSize()
    frame_instruments_columns_titles_average_cost.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_average_cost.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_average_cost)

    frame_instruments_columns_titles_total_cost = QLabel()
    frame_instruments_columns_titles_total_cost.setText("Стоимость")
    frame_instruments_columns_titles_total_cost.setObjectName("frame_instruments_columns_titles_total_cost")
    frame_instruments_columns_titles_total_cost.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_total_cost.adjustSize()
    frame_instruments_columns_titles_total_cost.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_total_cost.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_total_cost)

    frame_instruments_columns_titles_profit = QLabel()
    frame_instruments_columns_titles_profit.setText("Прибыль")
    frame_instruments_columns_titles_profit.setObjectName("frame_shares_columns_titles_profit")
    frame_instruments_columns_titles_profit.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_profit.adjustSize()
    frame_instruments_columns_titles_profit.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_profit.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_profit)

    frame_instruments_columns_titles_profit_percentage = QLabel()
    frame_instruments_columns_titles_profit_percentage.setText("Доходность")
    frame_instruments_columns_titles_profit_percentage.setObjectName("frame_shares_columns_titles_profit_percentage")
    frame_instruments_columns_titles_profit_percentage.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_profit_percentage.adjustSize()
    frame_instruments_columns_titles_profit_percentage.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_profit_percentage.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_profit_percentage)

    frame_instruments_columns_titles_share_percentage = QLabel()
    frame_instruments_columns_titles_share_percentage.setText("Доля в портфеле")
    frame_instruments_columns_titles_share_percentage.setObjectName("frame_shares_columns_titles_share_percentage")
    frame_instruments_columns_titles_share_percentage.setGeometry(QRect(0, 5, 50, 61))
    # inst_name.setMaximumSize(QSize(80, 16777215))
    frame_instruments_columns_titles_share_percentage.adjustSize()
    frame_instruments_columns_titles_share_percentage.setStyleSheet(
        u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
        "")
    frame_instruments_columns_titles_share_percentage.setAlignment(Qt.AlignRight)
    frame_instruments_name_columns_layout.addWidget(frame_instruments_columns_titles_share_percentage)

    frame_instruments_layout.addWidget(frame_instruments_columns_titles)

    c = 0
    for indexRow in range(len(df.index)):
        row = df.iloc[indexRow]
        c += 1
        frame_instrument = QFrame()
        # frame_inst = QFrame(self.scrollAreaWidgetContents_4)
        frame_instrument.setObjectName("instr_share" + str(c))
        frame_instrument.setGeometry(QRect(0, 0, 401, 41))
        frame_instrument.setFrameShape(QFrame.StyledPanel)
        frame_instrument.setFrameShadow(QFrame.Raised)
        frame_inst_layout = QHBoxLayout(frame_instrument)
        frame_instrument.setStyleSheet('''
                background-color: #2A2A2C;
                padding-left: 0px;
            ''')

        inst_name = QLabel()
        inst_name.setText(row['name'])
        inst_name.setObjectName("inst_name" + str(c))
        inst_name.setGeometry(QRect(10, -10, 51, 61))
        # inst_name.setMaximumSize(QSize(80, 16777215))
        inst_name.adjustSize()
        inst_name.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                "")
        inst_name.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_name)

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
        inst_quan.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_quan)

        inst_current_buy_price = QLabel()
        inst_current_buy_price.setText(str(round(row['current_buy_price'], 2)) + "₽")
        inst_current_buy_price.setObjectName("inst_current_buy_price" + str(c))
        inst_current_buy_price.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_current_buy_price.adjustSize()
        inst_current_buy_price.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                             "")
        inst_current_buy_price.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_current_buy_price)

        inst_average_buy_price = QLabel()
        inst_average_buy_price.setText(str(round(row['average_buy_price'], 2)) + "₽")
        inst_average_buy_price.setObjectName("inst_inst_average_buy_price" + str(c))
        inst_average_buy_price.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_average_buy_price.adjustSize()
        inst_average_buy_price.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                             "")
        inst_average_buy_price.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_average_buy_price)

        inst_cost = QLabel()
        inst_cost.setText(str(round(row['cost'], 2)) + "₽")
        inst_cost.setObjectName("inst_cost" + str(c))
        inst_cost.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_cost.adjustSize()
        inst_cost.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
                                "")
        inst_cost.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_cost)

        inst_expected_yield = QLabel()
        inst_expected_yield_percentage = QLabel()
        if row['expected_yield'] < 0:
            inst_expected_yield.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {minus_profit}")
            inst_expected_yield_percentage.setStyleSheet(
                f"font-size : 13px; font-family : Open Sans; color : {minus_profit}")
            # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {minus_profit}")
        elif row['expected_yield'] == 0:
            inst_expected_yield.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {zero_porfit}")
            inst_expected_yield_percentage.setStyleSheet(
                f"font-size : 13px; font-family : Open Sans; color : {zero_porfit}")
            # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {zero_porfit}")
        elif row['expected_yield'] > 0:
            inst_expected_yield.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {plus_profit}")
            inst_expected_yield_percentage.setStyleSheet(
                f"font-size : 13px; font-family : Open Sans; color : {plus_profit}")
            # inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color :  {plus_profit}")
        inst_expected_yield.setText(str(round(row['expected_yield'], 2)) + "₽")
        inst_expected_yield.setObjectName("inst_expected_yield" + str(c))
        inst_expected_yield.setGeometry(QRect(190, -10, 51, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_expected_yield.adjustSize()
        inst_expected_yield.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_expected_yield)

        inst_expected_yield_percentage.setText(str(round(row['expected_yield_percentage'], 2)) + "%")
        inst_expected_yield_percentage.setObjectName("inst_expected_yield" + str(c))
        inst_expected_yield_percentage.setGeometry(QRect(190, -10, 48, 61))
        # inst_cost.setMaximumSize(QSize(56, 16777215))
        inst_expected_yield_percentage.adjustSize()
        inst_expected_yield_percentage.setAlignment(Qt.AlignLeft)
        frame_inst_layout.addWidget(inst_expected_yield_percentage)

        inst_percent = QLabel()
        inst_percent.setText(str(round(row['portfolio_share'], 2)) + "%")
        inst_percent.setObjectName("inst_percent" + str(c))
        inst_percent.setGeometry(QRect(340, -20, 48, 61))
        inst_percent.setMaximumSize(QSize(56, 16777215))
        inst_percent.adjustSize()
        inst_percent.setStyleSheet(f"font-size : 13px; font-family : Open Sans; color : {zero_porfit}")
        inst_percent.setAlignment(Qt.AlignRight)
        inst_percent.setContentsMargins(0, 0, 0, 0)
        frame_inst_layout.addWidget(inst_percent)

        frame_instruments_layout.addWidget(frame_instrument)
    return frame_instruments