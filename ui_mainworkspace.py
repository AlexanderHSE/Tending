# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainworkspace.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindowBig(object):
    def setupUi(self, MainWindowBig):
        if not MainWindowBig.objectName():
            MainWindowBig.setObjectName(u"MainWindowBig")
        MainWindowBig.resize(947, 739)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindowBig.sizePolicy().hasHeightForWidth())
        MainWindowBig.setSizePolicy(sizePolicy)
        MainWindowBig.setMinimumSize(QSize(947, 739))
        self.centralwidget = QWidget(MainWindowBig)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 637))
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setStyleSheet(u".QFrame#frame {\n"
"border-radius: 30;\n"
"}\n"
"* {\n"
"background-color: rgb(37,37,40);\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.title_bar_2 = QFrame(self.frame)
        self.title_bar_2.setObjectName(u"title_bar_2")
        self.title_bar_2.setMinimumSize(QSize(905, 70))
        self.title_bar_2.setMaximumSize(QSize(16777215, 70))
        self.title_bar_2.setStyleSheet(u"background-color:None")
        self.title_bar_2.setFrameShape(QFrame.NoFrame)
        self.title_bar_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.title_bar_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_logo_2 = QFrame(self.title_bar_2)
        self.frame_logo_2.setObjectName(u"frame_logo_2")
        self.frame_logo_2.setStyleSheet(u"")
        self.frame_logo_2.setFrameShape(QFrame.StyledPanel)
        self.frame_logo_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_logo_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_space = QFrame(self.frame_logo_2)
        self.frame_space.setObjectName(u"frame_space")
        self.frame_space.setMinimumSize(QSize(10, 70))
        self.frame_space.setMaximumSize(QSize(10, 70))
        self.frame_space.setFrameShape(QFrame.StyledPanel)
        self.frame_space.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_space)

        self.frame_head = QFrame(self.frame_logo_2)
        self.frame_head.setObjectName(u"frame_head")
        self.frame_head.setFrameShape(QFrame.StyledPanel)
        self.frame_head.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_head)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame_head)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(300, 41))
        self.label_4.setPixmap(QPixmap(u"Frame_13.jpg"))

        self.horizontalLayout_3.addWidget(self.label_4)

        self.frame_tagLine = QFrame(self.frame_head)
        self.frame_tagLine.setObjectName(u"frame_tagLine")
        self.frame_tagLine.setMinimumSize(QSize(433, 48))
        self.frame_tagLine.setMaximumSize(QSize(433, 16777215))
        self.frame_tagLine.setFrameShape(QFrame.StyledPanel)
        self.frame_tagLine.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_tagLine)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_casemain = QPushButton(self.frame_tagLine)
        self.btn_casemain.setObjectName(u"btn_casemain")
        self.btn_casemain.setMaximumSize(QSize(115, 16777215))
        self.btn_casemain.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color: rgb(155, 156, 151);\n"
"	font-family: Ubuntu;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(234, 234, 234);\n"
"}")
        self.btn_casemain.setCheckable(False)
        self.btn_casemain.setFlat(True)

        self.horizontalLayout_7.addWidget(self.btn_casemain)

        self.btn_analtics = QPushButton(self.frame_tagLine)
        self.btn_analtics.setObjectName(u"btn_analtics")
        self.btn_analtics.setMaximumSize(QSize(120, 16777215))
        self.btn_analtics.setFocusPolicy(Qt.NoFocus)
        self.btn_analtics.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color: rgb(155, 156, 151);\n"
"	font-family: Ubuntu;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(234, 234, 234);\n"
"}")
        self.btn_analtics.setFlat(True)

        self.horizontalLayout_7.addWidget(self.btn_analtics)

        self.btn_currency = QPushButton(self.frame_tagLine)
        self.btn_currency.setObjectName(u"btn_currency")
        self.btn_currency.setMaximumSize(QSize(30, 16777215))
        self.btn_currency.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color: rgb(155, 156, 151);\n"
"	font-family: Ubuntu;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(234, 234, 234);\n"
"}")
        self.btn_currency.setFlat(True)

        self.horizontalLayout_7.addWidget(self.btn_currency)

        self.btn_case = QPushButton(self.frame_tagLine)
        self.btn_case.setObjectName(u"btn_case")
        self.btn_case.setMaximumSize(QSize(40, 16777215))
        self.btn_case.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color: rgb(155, 156, 151);\n"
"	font-family: Ubuntu;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(234, 234, 234);\n"
"}")
        icon = QIcon()
        icon.addFile(u"briefcase (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_case.setIcon(icon)
        self.btn_case.setIconSize(QSize(50, 50))
        self.btn_case.setCheckable(False)
        self.btn_case.setFlat(True)

        self.horizontalLayout_7.addWidget(self.btn_case)


        self.horizontalLayout_3.addWidget(self.frame_tagLine)


        self.horizontalLayout_5.addWidget(self.frame_head)


        self.horizontalLayout_4.addWidget(self.frame_logo_2)

        self.frame_btns_2 = QFrame(self.title_bar_2)
        self.frame_btns_2.setObjectName(u"frame_btns_2")
        self.frame_btns_2.setMaximumSize(QSize(150, 16777215))
        self.frame_btns_2.setFrameShape(QFrame.StyledPanel)
        self.frame_btns_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_btns_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize_2 = QPushButton(self.frame_btns_2)
        self.btn_minimize_2.setObjectName(u"btn_minimize_2")
        self.btn_minimize_2.setMinimumSize(QSize(20, 20))
        self.btn_minimize_2.setMaximumSize(QSize(40, 40))
        self.btn_minimize_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color: rgb(155, 156, 151);\n"
"	font-family: Ubuntu;\n"
"	font-size: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(234, 234, 234)\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_minimize_2)

        self.btn_maximize_restore = QPushButton(self.frame_btns_2)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color: rgb(155, 156, 151);\n"
"	font-family: Ubuntu;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"maximize-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)
        self.btn_maximize_restore.setIconSize(QSize(20, 20))
        self.btn_maximize_restore.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btn_maximize_restore)

        self.btn_close_2 = QPushButton(self.frame_btns_2)
        self.btn_close_2.setObjectName(u"btn_close_2")
        self.btn_close_2.setMinimumSize(QSize(20, 20))
        self.btn_close_2.setMaximumSize(QSize(40, 40))
        self.btn_close_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color: rgb(155, 156, 151);\n"
"	font-family: Ubuntu;\n"
"	font-size: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(234, 234, 234)\n"
"}")
        self.btn_close_2.setFlat(False)

        self.horizontalLayout_6.addWidget(self.btn_close_2)


        self.horizontalLayout_4.addWidget(self.frame_btns_2)


        self.verticalLayout_2.addWidget(self.title_bar_2)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_casebig = QWidget()
        self.page_casebig.setObjectName(u"page_casebig")
        self.verticalLayout_7 = QVBoxLayout(self.page_casebig)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea_2 = QScrollArea(self.page_casebig)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 881, 591))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 101))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cost_all = QFrame(self.frame_2)
        self.cost_all.setObjectName(u"cost_all")
        self.cost_all.setMaximumSize(QSize(171, 81))
        self.cost_all.setStyleSheet(u"background-color: #2A2A2C; border-radius: 10")
        self.cost_all.setFrameShape(QFrame.StyledPanel)
        self.cost_all.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.cost_all)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.cost_text_all = QLabel(self.cost_all)
        self.cost_text_all.setObjectName(u"cost_text_all")
        self.cost_text_all.setStyleSheet(u"font-size : 24px; font-family : Open Sans; color : #F9F9FB\n"
"")
        self.cost_text_all.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.cost_text_all)

        self.cost_number_all = QLabel(self.cost_all)
        self.cost_number_all.setObjectName(u"cost_number_all")
        self.cost_number_all.setLayoutDirection(Qt.RightToLeft)
        self.cost_number_all.setStyleSheet(u"font-size : 20px; font-family : Open Sans; \n"
"")
        self.cost_number_all.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.cost_number_all)


        self.horizontalLayout_8.addWidget(self.cost_all)

        self.profit_all = QFrame(self.frame_2)
        self.profit_all.setObjectName(u"profit_all")
        self.profit_all.setMaximumSize(QSize(171, 81))
        self.profit_all.setStyleSheet(u"background-color: #2A2A2C; border-radius: 10")
        self.profit_all.setFrameShape(QFrame.StyledPanel)
        self.profit_all.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.profit_all)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.profit_text_all = QLabel(self.profit_all)
        self.profit_text_all.setObjectName(u"profit_text_all")
        self.profit_text_all.setStyleSheet(u"font-size : 24px; font-family : Open Sans; color : #F9F9FB")
        self.profit_text_all.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.profit_text_all)

        self.profit_number_all = QLabel(self.profit_all)
        self.profit_number_all.setObjectName(u"profit_number_all")
        self.profit_number_all.setLayoutDirection(Qt.RightToLeft)
        self.profit_number_all.setStyleSheet(u"font-size : 20px; font-family : Open Sans; \n"
"")
        self.profit_number_all.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.profit_number_all)


        self.horizontalLayout_8.addWidget(self.profit_all)

        self.yield_all = QFrame(self.frame_2)
        self.yield_all.setObjectName(u"yield_all")
        self.yield_all.setMaximumSize(QSize(200, 81))
        self.yield_all.setStyleSheet(u"background-color: #2A2A2C; border-radius: 10")
        self.yield_all.setFrameShape(QFrame.StyledPanel)
        self.yield_all.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.yield_all)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.yield_text_all = QLabel(self.yield_all)
        self.yield_text_all.setObjectName(u"yield_text_all")
        self.yield_text_all.setStyleSheet(u"font-size : 24px; font-family : Open Sans; color : #F9F9FB\n"
"")
        self.yield_text_all.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.yield_text_all)

        self.yield_number_all = QLabel(self.yield_all)
        self.yield_number_all.setObjectName(u"yield_number_all")
        self.yield_number_all.setLayoutDirection(Qt.RightToLeft)
        self.yield_number_all.setStyleSheet(u"font-size : 20px; font-family : Open Sans; \n"
"")
        self.yield_number_all.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.yield_number_all)


        self.horizontalLayout_8.addWidget(self.yield_all)


        self.verticalLayout_10.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pie_chart_area = QFrame(self.frame_3)
        self.pie_chart_area.setObjectName(u"pie_chart_area")
        self.pie_chart_area.setMinimumSize(QSize(366, 0))
        self.pie_chart_area.setStyleSheet(u"background-color: #2A2A2C; border-radius: 10")
        self.pie_chart_area.setFrameShape(QFrame.StyledPanel)
        self.pie_chart_area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.pie_chart_area)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_5 = QFrame(self.pie_chart_area)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 51))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pie_chart_name = QLabel(self.frame_5)
        self.pie_chart_name.setObjectName(u"pie_chart_name")
        self.pie_chart_name.setStyleSheet(u"font-size : 20px; font-family : Open Sans; color : #F9F9FB\n"
"")
        self.pie_chart_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.pie_chart_name)


        self.verticalLayout_14.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.pie_chart_area)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_6)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_15.addItem(self.horizontalSpacer_3)


        self.verticalLayout_14.addWidget(self.frame_6)


        self.horizontalLayout_9.addWidget(self.pie_chart_area)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.instruments_close_pie_area = QFrame(self.frame_3)
        self.instruments_close_pie_area.setObjectName(u"instruments_close_pie_area")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.instruments_close_pie_area.sizePolicy().hasHeightForWidth())
        self.instruments_close_pie_area.setSizePolicy(sizePolicy1)
        self.instruments_close_pie_area.setStyleSheet(u"background-color: #2A2A2C; border-radius: 10")
        self.instruments_close_pie_area.setFrameShape(QFrame.StyledPanel)
        self.instruments_close_pie_area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.instruments_close_pie_area)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_4 = QFrame(self.instruments_close_pie_area)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMaximumSize(QSize(16777215, 83))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.column_title_name = QLabel(self.frame_4)
        self.column_title_name.setObjectName(u"column_title_name")
        self.column_title_name.setMaximumSize(QSize(56, 16777215))
        self.column_title_name.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
"")
        self.column_title_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.column_title_name)

        self.column_title_type = QLabel(self.frame_4)
        self.column_title_type.setObjectName(u"column_title_type")
        self.column_title_type.setMaximumSize(QSize(37, 16777215))
        self.column_title_type.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
"")
        self.column_title_type.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.column_title_type)

        self.column_title_quantity = QLabel(self.frame_4)
        self.column_title_quantity.setObjectName(u"column_title_quantity")
        self.column_title_quantity.setMaximumSize(QSize(68, 16777215))
        self.column_title_quantity.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
"")
        self.column_title_quantity.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.column_title_quantity)

        self.column_title_price = QFrame(self.frame_4)
        self.column_title_price.setObjectName(u"column_title_price")
        self.column_title_price.setMaximumSize(QSize(79, 16777215))
        self.column_title_price.setFrameShape(QFrame.StyledPanel)
        self.column_title_price.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.column_title_price)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.price_now = QLabel(self.column_title_price)
        self.price_now.setObjectName(u"price_now")
        self.price_now.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
"")
        self.price_now.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.price_now)

        self.price_average = QLabel(self.column_title_price)
        self.price_average.setObjectName(u"price_average")
        self.price_average.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
"")
        self.price_average.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.price_average)


        self.horizontalLayout_10.addWidget(self.column_title_price)

        self.column_title_res = QFrame(self.frame_4)
        self.column_title_res.setObjectName(u"column_title_res")
        self.column_title_res.setMaximumSize(QSize(91, 16777215))
        self.column_title_res.setFrameShape(QFrame.StyledPanel)
        self.column_title_res.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.column_title_res)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.column_title_yeild = QLabel(self.column_title_res)
        self.column_title_yeild.setObjectName(u"column_title_yeild")
        self.column_title_yeild.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
"")
        self.column_title_yeild.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.column_title_yeild)

        self.column_title_profit = QLabel(self.column_title_res)
        self.column_title_profit.setObjectName(u"column_title_profit")
        self.column_title_profit.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB\n"
"")
        self.column_title_profit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.column_title_profit)


        self.horizontalLayout_10.addWidget(self.column_title_res)

        self.column_tittle_percentage = QLabel(self.frame_4)
        self.column_tittle_percentage.setObjectName(u"column_tittle_percentage")
        self.column_tittle_percentage.setMaximumSize(QSize(37, 16777215))
        self.column_tittle_percentage.setStyleSheet(u"font-size : 13px; font-family : Open Sans; color : #F9F9FB;\n"
"")
        self.column_tittle_percentage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.column_tittle_percentage)


        self.verticalLayout_13.addWidget(self.frame_4)

        self.instruments_cpa_scrollArea = QScrollArea(self.instruments_close_pie_area)
        self.instruments_cpa_scrollArea.setObjectName(u"instruments_cpa_scrollArea")
        self.instruments_cpa_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 403, 325))
        self.instruments_cpa_scrollArea.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_13.addWidget(self.instruments_cpa_scrollArea)


        self.horizontalLayout_9.addWidget(self.instruments_close_pie_area)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.page_casebig)
        self.page_analytics = QWidget()
        self.page_analytics.setObjectName(u"page_analytics")
        self.lineEdit = QLineEdit(self.page_analytics)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(380, 270, 113, 22))
        self.stackedWidget.addWidget(self.page_analytics)
        self.page_caseList = QWidget()
        self.page_caseList.setObjectName(u"page_caseList")
        self.verticalLayout_6 = QVBoxLayout(self.page_caseList)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_8 = QFrame(self.page_caseList)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_8)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_caseList = QWidget()
        self.scrollAreaWidgetContents_caseList.setObjectName(u"scrollAreaWidgetContents_caseList")
        self.scrollAreaWidgetContents_caseList.setGeometry(QRect(0, 0, 883, 543))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_caseList)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.frame_addCase = QFrame(self.frame_8)
        self.frame_addCase.setObjectName(u"frame_addCase")
        self.frame_addCase.setMinimumSize(QSize(859, 40))
        self.frame_addCase.setStyleSheet(u"border-radius: 20px; background-color: rgb(148, 148, 152);")
        self.frame_addCase.setFrameShape(QFrame.StyledPanel)
        self.frame_addCase.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_addCase)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_addCase = QPushButton(self.frame_addCase)
        self.btn_addCase.setObjectName(u"btn_addCase")
        icon2 = QIcon()
        icon2.addFile(u"plus-square_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_addCase.setIcon(icon2)
        self.btn_addCase.setIconSize(QSize(50, 50))
        self.btn_addCase.setCheckable(False)
        self.btn_addCase.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_addCase)


        self.verticalLayout_3.addWidget(self.frame_addCase)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.page_caseList)
        self.page_add_case = QWidget()
        self.page_add_case.setObjectName(u"page_add_case")
        self.verticalLayout_4 = QVBoxLayout(self.page_add_case)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_7 = QFrame(self.page_add_case)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 70))
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.edit_token = QLineEdit(self.frame_7)
        self.edit_token.setObjectName(u"edit_token")
        self.edit_token.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.edit_token.sizePolicy().hasHeightForWidth())
        self.edit_token.setSizePolicy(sizePolicy2)
        self.edit_token.setMinimumSize(QSize(0, 50))
        self.edit_token.setStyleSheet(u"border-radius: 20px; background-color: rgb(73, 73, 77); color: rgb(180, 180, 189); padding-left: 12px;")
        self.edit_token.setMaxLength(1000)
        self.edit_token.setEchoMode(QLineEdit.Password)
        self.edit_token.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.edit_token)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_addToList = QPushButton(self.frame_7)
        self.btn_addToList.setObjectName(u"btn_addToList")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_addToList.sizePolicy().hasHeightForWidth())
        self.btn_addToList.setSizePolicy(sizePolicy3)
        self.btn_addToList.setMinimumSize(QSize(100, 50))
        self.btn_addToList.setStyleSheet(u"QPushButton {\n"
"border-radius: 25px; \n"
"color: rgb(249, 249, 251);\n"
"background-color: rgb(74, 80, 133);\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(157, 155, 161);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_addToList)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_9 = QFrame(self.page_add_case)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.frame_9)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 881, 514))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_15.addWidget(self.scrollArea_3)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.page_add_case)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.frame_grip = QFrame(self.frame)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(10, 20))
        self.frame_grip.setMaximumSize(QSize(20, 17))
        self.frame_grip.setLayoutDirection(Qt.RightToLeft)
        self.frame_grip.setStyleSheet(u"border-bottom-right-radius: 10px; margin-right: 20px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.frame)

        MainWindowBig.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowBig)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindowBig)
    # setupUi

    def retranslateUi(self, MainWindowBig):
        MainWindowBig.setWindowTitle(QCoreApplication.translate("MainWindowBig", u"MainWindow", None))
        self.label_4.setText("")
        self.btn_casemain.setText(QCoreApplication.translate("MainWindowBig", u"\u041f\u043e\u0440\u0442\u0444\u0435\u043b\u044c", None))
        self.btn_analtics.setText(QCoreApplication.translate("MainWindowBig", u"\u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430", None))
        self.btn_currency.setText(QCoreApplication.translate("MainWindowBig", u"\u20bd", None))
        self.btn_case.setText("")
        self.btn_minimize_2.setText(QCoreApplication.translate("MainWindowBig", u"\u2013", None))
        self.btn_maximize_restore.setText("")
        self.btn_close_2.setText(QCoreApplication.translate("MainWindowBig", u"\u00d7", None))
        self.cost_text_all.setText(QCoreApplication.translate("MainWindowBig", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None))
        self.cost_number_all.setText(QCoreApplication.translate("MainWindowBig", u"TextLabel", None))
        self.profit_text_all.setText(QCoreApplication.translate("MainWindowBig", u"\u041f\u0440\u0438\u0431\u044b\u043b\u044c", None))
        self.profit_number_all.setText(QCoreApplication.translate("MainWindowBig", u"TextLabel", None))
        self.yield_text_all.setText(QCoreApplication.translate("MainWindowBig", u"\u0414\u043e\u0445\u043e\u0434\u043d\u043e\u0441\u0442\u044c", None))
        self.yield_number_all.setText(QCoreApplication.translate("MainWindowBig", u"TextLabel", None))
        self.pie_chart_name.setText(QCoreApplication.translate("MainWindowBig", u"\u0412\u0441\u0435 \u0430\u043a\u0442\u0438\u0432\u044b", None))
        self.column_title_name.setText(QCoreApplication.translate("MainWindowBig", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.column_title_type.setText(QCoreApplication.translate("MainWindowBig", u"\u0422\u0438\u043f", None))
        self.column_title_quantity.setText(QCoreApplication.translate("MainWindowBig", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.price_now.setText(QCoreApplication.translate("MainWindowBig", u"\u0422\u0435\u043a. \u0446\u0435\u043d\u0430", None))
        self.price_average.setText(QCoreApplication.translate("MainWindowBig", u"\u0421\u0440. \u0446\u0435\u043d\u0430", None))
        self.column_title_yeild.setText(QCoreApplication.translate("MainWindowBig", u"\u041f\u0440\u0438\u0431\u044b\u043b\u044c", None))
        self.column_title_profit.setText(QCoreApplication.translate("MainWindowBig", u"\u0414\u043e\u0445\u043e\u0434\u043d\u043e\u0441\u0442\u044c", None))
        self.column_tittle_percentage.setText(QCoreApplication.translate("MainWindowBig", u"\u0414\u043e\u043b\u044f", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindowBig", u"Analytics", None))
        self.btn_addCase.setText("")
        self.edit_token.setPlaceholderText(QCoreApplication.translate("MainWindowBig", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u043e\u043a\u0435\u043d", None))
        self.btn_addToList.setText(QCoreApplication.translate("MainWindowBig", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
    # retranslateUi

