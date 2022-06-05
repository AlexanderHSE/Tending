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
        self.frame.setStyleSheet(u".QFrame#frame {\n"
"border-radius: 40;\n"
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
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
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
        self.label_4.setMinimumSize(QSize(341, 41))
        self.label_4.setPixmap(QPixmap(u"Frame_13.jpg"))

        self.horizontalLayout_3.addWidget(self.label_4)

        self.frame_tagLine = QFrame(self.frame_head)
        self.frame_tagLine.setObjectName(u"frame_tagLine")
        self.frame_tagLine.setMinimumSize(QSize(433, 48))
        self.frame_tagLine.setFrameShape(QFrame.StyledPanel)
        self.frame_tagLine.setFrameShadow(QFrame.Raised)
        self.btn_casemain = QPushButton(self.frame_tagLine)
        self.btn_casemain.setObjectName(u"btn_casemain")
        self.btn_casemain.setGeometry(QRect(80, 10, 96, 24))
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
        self.btn_analtics = QPushButton(self.frame_tagLine)
        self.btn_analtics.setObjectName(u"btn_analtics")
        self.btn_analtics.setGeometry(QRect(210, 10, 100, 24))
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
        self.btn_currency = QPushButton(self.frame_tagLine)
        self.btn_currency.setObjectName(u"btn_currency")
        self.btn_currency.setGeometry(QRect(330, 10, 21, 24))
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
        self.btn_case = QPushButton(self.frame_tagLine)
        self.btn_case.setObjectName(u"btn_case")
        self.btn_case.setGeometry(QRect(380, 5, 41, 31))
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

        self.horizontalLayout_3.addWidget(self.frame_tagLine)


        self.horizontalLayout_5.addWidget(self.frame_head)


        self.horizontalLayout_4.addWidget(self.frame_logo_2)

        self.frame_btns_2 = QFrame(self.title_bar_2)
        self.frame_btns_2.setObjectName(u"frame_btns_2")
        self.frame_btns_2.setMaximumSize(QSize(100, 16777215))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 881, 607))
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
        self.scrollAreaWidgetContents_caseList.setGeometry(QRect(0, 0, 883, 559))
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
        icon1 = QIcon()
        icon1.addFile(u"plus-square_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_addCase.setIcon(icon1)
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
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_token.sizePolicy().hasHeightForWidth())
        self.edit_token.setSizePolicy(sizePolicy)
        self.edit_token.setMinimumSize(QSize(0, 50))
        self.edit_token.setStyleSheet(u"border-radius: 20px; background-color: rgb(73, 73, 77); color: rgb(180, 180, 189); padding-left: 12px;")
        self.edit_token.setMaxLength(1000)
        self.edit_token.setEchoMode(QLineEdit.Password)
        self.edit_token.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.edit_token)

        self.btn_addToList = QPushButton(self.frame_7)
        self.btn_addToList.setObjectName(u"btn_addToList")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_addToList.sizePolicy().hasHeightForWidth())
        self.btn_addToList.setSizePolicy(sizePolicy1)
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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 881, 530))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_15.addWidget(self.scrollArea_3)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.page_add_case)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame)

        MainWindowBig.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowBig)

        self.stackedWidget.setCurrentIndex(0)


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
        self.btn_close_2.setText(QCoreApplication.translate("MainWindowBig", u"\u00d7", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindowBig", u"Analytics", None))
        self.btn_addCase.setText("")
        self.edit_token.setPlaceholderText(QCoreApplication.translate("MainWindowBig", u"Token", None))
        self.btn_addToList.setText(QCoreApplication.translate("MainWindowBig", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
    # retranslateUi

