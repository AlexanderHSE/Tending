# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_stacked.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(522, 601)
        MainWindow.setMinimumSize(QSize(522, 601))
        MainWindow.setMaximumSize(QSize(522, 601))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(522, 601))
        self.centralwidget.setMaximumSize(QSize(522, 601))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.wrapper_stacked = QFrame(self.centralwidget)
        self.wrapper_stacked.setObjectName(u"wrapper_stacked")
        self.wrapper_stacked.setMaximumSize(QSize(502, 581))
        self.wrapper_stacked.setStyleSheet(u"background-color: rgb(37,37,40);\n"
"border-radius: 40;")
        self.wrapper_stacked.setFrameShape(QFrame.StyledPanel)
        self.wrapper_stacked.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.wrapper_stacked)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.wrapper_stacked)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(37,37,40);\n"
"border-radius: 40;")
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.drop_shadow_frame = QFrame(self.page_login)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setGeometry(QRect(0, 0, 502, 581))
        self.drop_shadow_frame.setMinimumSize(QSize(502, 581))
        self.drop_shadow_frame.setMaximumSize(QSize(502, 581))
        self.drop_shadow_frame.setStyleSheet(u"background-color: rgb(37,37,40);\n"
"border-radius: 40;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.title_bar_2 = QFrame(self.drop_shadow_frame)
        self.title_bar_2.setObjectName(u"title_bar_2")
        self.title_bar_2.setMinimumSize(QSize(502, 70))
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
        self.frame_logo_2.setFrameShape(QFrame.StyledPanel)
        self.frame_logo_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_logo_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_logo_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(25, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_logo_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 20, 341, 41))
        self.label_4.setMinimumSize(QSize(341, 41))
        self.label_4.setPixmap(QPixmap(u"../../Frame_13.jpg"))

        self.horizontalLayout_5.addWidget(self.frame_5)


        self.horizontalLayout_4.addWidget(self.frame_logo_2)

        self.frame_btns_2 = QFrame(self.title_bar_2)
        self.frame_btns_2.setObjectName(u"frame_btns_2")
        self.frame_btns_2.setMaximumSize(QSize(100, 16777215))
        self.frame_btns_2.setFrameShape(QFrame.StyledPanel)
        self.frame_btns_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_btns_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
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


        self.verticalLayout_6.addWidget(self.title_bar_2)

        self.content_bar_2 = QFrame(self.drop_shadow_frame)
        self.content_bar_2.setObjectName(u"content_bar_2")
        self.content_bar_2.setStyleSheet(u"background-color:None")
        self.content_bar_2.setFrameShape(QFrame.StyledPanel)
        self.content_bar_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.content_bar_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_2 = QFrame(self.content_bar_2)
        self.frame_title_2.setObjectName(u"frame_title_2")
        self.frame_title_2.setMinimumSize(QSize(0, 5))
        self.frame_title_2.setMaximumSize(QSize(16777215, 200))
        self.frame_title_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 15, 0, 0)
        self.label_5 = QLabel(self.frame_title_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 40))
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setStyleSheet(u"color: rgb(249, 249, 251);\n"
"font-size: 37px;\n"
"font-family: \"Ubuntu\";")
        self.label_5.setTextFormat(Qt.MarkdownText)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_title_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setStyleSheet(u"color: rgb(249, 249, 251);\n"
"font-size: 13px;\n"
"font-family: \"Ubuntu\";")
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_6.setWordWrap(False)

        self.verticalLayout_8.addWidget(self.label_6)


        self.verticalLayout_7.addWidget(self.frame_title_2)

        self.frame_login_2 = QFrame(self.content_bar_2)
        self.frame_login_2.setObjectName(u"frame_login_2")
        self.frame_login_2.setFrameShape(QFrame.StyledPanel)
        self.frame_login_2.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.frame_login_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 10, 480, 149))
        self.frame_6.setMinimumSize(QSize(300, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.edit_login_2 = QLineEdit(self.frame_6)
        self.edit_login_2.setObjectName(u"edit_login_2")
        self.edit_login_2.setGeometry(QRect(115, -1, 261, 41))
        self.edit_login_2.setStyleSheet(u"border-radius: 10px; background-color: rgb(73, 73, 77); color: rgb(180, 180, 189); padding-left: 12px;")
        self.edit_login_2.setMaxLength(1000)
        self.edit_password_2 = QLineEdit(self.frame_6)
        self.edit_password_2.setObjectName(u"edit_password_2")
        self.edit_password_2.setGeometry(QRect(115, 80, 261, 41))
        self.edit_password_2.setStyleSheet(u"border-radius: 10px; \n"
"background-color: rgb(73, 73, 77); \n"
"color: rgb(180, 180, 189);\n"
"padding-left: 12px;")
        self.edit_password_2.setMaxLength(1000)
        self.edit_password_2.setFrame(False)
        self.edit_password_2.setEchoMode(QLineEdit.Password)
        self.edit_password_2.setClearButtonEnabled(False)
        self.tip_email_2 = QLabel(self.frame_6)
        self.tip_email_2.setObjectName(u"tip_email_2")
        self.tip_email_2.setGeometry(QRect(115, 50, 161, 16))
        self.tip_email_2.setStyleSheet(u"color: rgb(239, 88, 88); font-size: 16px;")
        self.tip_password_2 = QLabel(self.frame_6)
        self.tip_password_2.setObjectName(u"tip_password_2")
        self.tip_password_2.setGeometry(QRect(115, 130, 121, 16))
        self.tip_password_2.setStyleSheet(u"color: rgb(239, 88, 88); font-size: 16px")
        self.btn_show_password_2 = QPushButton(self.frame_6)
        self.btn_show_password_2.setObjectName(u"btn_show_password_2")
        self.btn_show_password_2.setGeometry(QRect(350, 90, 21, 21))
        self.btn_show_password_2.setStyleSheet(u"border:none; background: none;")
        icon = QIcon()
        icon.addFile(u"closedEyeChanged.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_show_password_2.setIcon(icon)
        self.frame_forgot_password_2 = QFrame(self.frame_login_2)
        self.frame_forgot_password_2.setObjectName(u"frame_forgot_password_2")
        self.frame_forgot_password_2.setGeometry(QRect(0, 150, 502, 170))
        self.frame_forgot_password_2.setFrameShape(QFrame.StyledPanel)
        self.frame_forgot_password_2.setFrameShadow(QFrame.Raised)
        self.btn_signin_3 = QPushButton(self.frame_forgot_password_2)
        self.btn_signin_3.setObjectName(u"btn_signin_3")
        self.btn_signin_3.setGeometry(QRect(120, 40, 111, 28))
        self.btn_signin_3.setStyleSheet(u"QPushButton {\n"
"border: 1px solid silver; \n"
"border-radius: 10px; \n"
"color: rgb(249, 249, 251);\n"
"background-color: rgb(74, 80, 133);\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(157, 155, 161);\n"
"}\n"
"QPushButton:focus {\n"
"outline: 0; \n"
"outline-offset: 0;\n"
"}\n"
"")
        self.btn_signin_4 = QPushButton(self.frame_forgot_password_2)
        self.btn_signin_4.setObjectName(u"btn_signin_4")
        self.btn_signin_4.setGeometry(QRect(260, 40, 131, 28))
        self.btn_signin_4.setStyleSheet(u"QPushButton {\n"
"border: 1px solid silver; \n"
"border-radius: 10px; \n"
"color: rgb(249, 249, 251);\n"
"background-color: rgb(74, 80, 133);\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(157, 155, 161);\n"
"}\n"
"QPushButton:focus {\n"
"outline: 0; \n"
"outline-offset: 0;\n"
"}\n"
"")
        self.label_forgot_password_2 = QLabel(self.frame_forgot_password_2)
        self.label_forgot_password_2.setObjectName(u"label_forgot_password_2")
        self.label_forgot_password_2.setGeometry(QRect(120, 80, 111, 16))
        self.label_forgot_password_2.setStyleSheet(u"QLabel {\n"
"color: rgb(249, 249, 251);\n"
"font-size: 11px;\n"
"font-family: \"Ubuntu\";\n"
"font-weight: bold;\n"
"}\n"
"QLabel:hover {\n"
"color: rgb(196, 186, 208);\n"
"}")

        self.verticalLayout_7.addWidget(self.frame_login_2)


        self.verticalLayout_6.addWidget(self.content_bar_2)

        self.stackedWidget.addWidget(self.page_login)
        self.page_reg = QWidget()
        self.page_reg.setObjectName(u"page_reg")
        self.frame_reg = QFrame(self.page_reg)
        self.frame_reg.setObjectName(u"frame_reg")
        self.frame_reg.setGeometry(QRect(0, 0, 502, 581))
        self.frame_reg.setStyleSheet(u"background-color: rgb(37,37,40);\n"
"border-radius: 40")
        self.frame_reg.setFrameShape(QFrame.StyledPanel)
        self.frame_reg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_reg)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.title_bar_3 = QFrame(self.frame_reg)
        self.title_bar_3.setObjectName(u"title_bar_3")
        self.title_bar_3.setMinimumSize(QSize(502, 70))
        self.title_bar_3.setMaximumSize(QSize(16777215, 70))
        self.title_bar_3.setStyleSheet(u"background-color:None")
        self.title_bar_3.setFrameShape(QFrame.NoFrame)
        self.title_bar_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.title_bar_3)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_logo_3 = QFrame(self.title_bar_3)
        self.frame_logo_3.setObjectName(u"frame_logo_3")
        self.frame_logo_3.setFrameShape(QFrame.StyledPanel)
        self.frame_logo_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_logo_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_logo_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(25, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_logo_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 20, 341, 41))
        self.label_7.setMinimumSize(QSize(341, 41))
        self.label_7.setPixmap(QPixmap(u"../../Frame_13.jpg"))

        self.horizontalLayout_8.addWidget(self.frame_8)


        self.horizontalLayout_7.addWidget(self.frame_logo_3)

        self.frame_btns_3 = QFrame(self.title_bar_3)
        self.frame_btns_3.setObjectName(u"frame_btns_3")
        self.frame_btns_3.setMaximumSize(QSize(100, 16777215))
        self.frame_btns_3.setFrameShape(QFrame.StyledPanel)
        self.frame_btns_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_btns_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_minimize_3 = QPushButton(self.frame_btns_3)
        self.btn_minimize_3.setObjectName(u"btn_minimize_3")
        self.btn_minimize_3.setMinimumSize(QSize(20, 20))
        self.btn_minimize_3.setMaximumSize(QSize(40, 40))
        self.btn_minimize_3.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color: rgb(155, 156, 151);\n"
"	font-family: Ubuntu;\n"
"	font-size: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(234, 234, 234)\n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_minimize_3)

        self.btn_close_3 = QPushButton(self.frame_btns_3)
        self.btn_close_3.setObjectName(u"btn_close_3")
        self.btn_close_3.setMinimumSize(QSize(20, 20))
        self.btn_close_3.setMaximumSize(QSize(40, 40))
        self.btn_close_3.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color: rgb(155, 156, 151);\n"
"	font-family: Ubuntu;\n"
"	font-size: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(234, 234, 234)\n"
"}")
        self.btn_close_3.setFlat(False)

        self.horizontalLayout_9.addWidget(self.btn_close_3)


        self.horizontalLayout_7.addWidget(self.frame_btns_3)


        self.verticalLayout_9.addWidget(self.title_bar_3)

        self.content_bar_3 = QFrame(self.frame_reg)
        self.content_bar_3.setObjectName(u"content_bar_3")
        self.content_bar_3.setStyleSheet(u"background-color:None")
        self.content_bar_3.setFrameShape(QFrame.StyledPanel)
        self.content_bar_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.content_bar_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_title_3 = QFrame(self.content_bar_3)
        self.frame_title_3.setObjectName(u"frame_title_3")
        self.frame_title_3.setMinimumSize(QSize(0, 5))
        self.frame_title_3.setMaximumSize(QSize(16777215, 100))
        self.frame_title_3.setFrameShape(QFrame.StyledPanel)
        self.frame_title_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_title_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 15, 0, 0)
        self.label_8 = QLabel(self.frame_title_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 40))
        self.label_8.setMaximumSize(QSize(16777215, 40))
        self.label_8.setStyleSheet(u"color: rgb(249, 249, 251);\n"
"font-size: 37px;\n"
"font-family: \"Ubuntu\";")
        self.label_8.setTextFormat(Qt.MarkdownText)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_8)


        self.verticalLayout_10.addWidget(self.frame_title_3)

        self.frame_login_3 = QFrame(self.content_bar_3)
        self.frame_login_3.setObjectName(u"frame_login_3")
        self.frame_login_3.setFrameShape(QFrame.StyledPanel)
        self.frame_login_3.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.frame_login_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 10, 480, 271))
        self.frame_9.setMinimumSize(QSize(300, 0))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.edit_login_3 = QLineEdit(self.frame_9)
        self.edit_login_3.setObjectName(u"edit_login_3")
        self.edit_login_3.setGeometry(QRect(105, 80, 261, 41))
        self.edit_login_3.setStyleSheet(u"border-radius: 10px; background-color: rgb(73, 73, 77); color: rgb(180, 180, 189); padding-left: 12px;")
        self.edit_login_3.setMaxLength(1000)
        self.edit_password_3 = QLineEdit(self.frame_9)
        self.edit_password_3.setObjectName(u"edit_password_3")
        self.edit_password_3.setGeometry(QRect(105, 150, 261, 41))
        self.edit_password_3.setStyleSheet(u"border-radius: 10px; \n"
"background-color: rgb(73, 73, 77); \n"
"color: rgb(180, 180, 189);\n"
"padding-left: 12px;")
        self.edit_password_3.setMaxLength(1000)
        self.edit_password_3.setFrame(False)
        self.edit_password_3.setEchoMode(QLineEdit.Password)
        self.edit_password_3.setClearButtonEnabled(False)
        self.tip_email_3 = QLabel(self.frame_9)
        self.tip_email_3.setObjectName(u"tip_email_3")
        self.tip_email_3.setGeometry(QRect(105, 125, 151, 16))
        self.tip_email_3.setStyleSheet(u"color: rgb(239, 88, 88); font-size: 16px;")
        self.tip_password_3 = QLabel(self.frame_9)
        self.tip_password_3.setObjectName(u"tip_password_3")
        self.tip_password_3.setGeometry(QRect(105, 195, 121, 16))
        self.tip_password_3.setStyleSheet(u"color: rgb(239, 88, 88); font-size: 16px")
        self.confirm_password = QLineEdit(self.frame_9)
        self.confirm_password.setObjectName(u"confirm_password")
        self.confirm_password.setGeometry(QRect(105, 220, 261, 41))
        self.confirm_password.setStyleSheet(u"border-radius: 10px; \n"
"background-color: rgb(73, 73, 77); \n"
"color: rgb(180, 180, 189);\n"
"padding-left: 12px;")
        self.confirm_password.setMaxLength(1000)
        self.confirm_password.setFrame(False)
        self.confirm_password.setEchoMode(QLineEdit.Password)
        self.confirm_password.setClearButtonEnabled(False)
        self.edit_user_name = QLineEdit(self.frame_9)
        self.edit_user_name.setObjectName(u"edit_user_name")
        self.edit_user_name.setGeometry(QRect(105, 20, 261, 41))
        self.edit_user_name.setStyleSheet(u"border-radius: 10px; background-color: rgb(73, 73, 77); color: rgb(180, 180, 189); padding-left: 12px;")
        self.edit_user_name.setMaxLength(1000)
        self.frame_forgot_password_3 = QFrame(self.frame_login_3)
        self.frame_forgot_password_3.setObjectName(u"frame_forgot_password_3")
        self.frame_forgot_password_3.setGeometry(QRect(0, 280, 502, 131))
        self.frame_forgot_password_3.setFrameShape(QFrame.StyledPanel)
        self.frame_forgot_password_3.setFrameShadow(QFrame.Raised)
        self.btn_signin_5 = QPushButton(self.frame_forgot_password_3)
        self.btn_signin_5.setObjectName(u"btn_signin_5")
        self.btn_signin_5.setGeometry(QRect(110, 20, 111, 28))
        self.btn_signin_5.setStyleSheet(u"QPushButton {\n"
"border: 1px solid silver; \n"
"border-radius: 10px; \n"
"color: rgb(249, 249, 251);\n"
"background-color: rgb(74, 80, 133);\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(157, 155, 161);\n"
"}\n"
"")
        self.btn_signin_6 = QPushButton(self.frame_forgot_password_3)
        self.btn_signin_6.setObjectName(u"btn_signin_6")
        self.btn_signin_6.setGeometry(QRect(250, 20, 131, 28))
        self.btn_signin_6.setStyleSheet(u"QPushButton {\n"
"border: 1px solid silver; \n"
"border-radius: 10px; \n"
"color: rgb(249, 249, 251);\n"
"background-color: rgb(74, 80, 133);\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(157, 155, 161);\n"
"}\n"
"")

        self.verticalLayout_10.addWidget(self.frame_login_3)


        self.verticalLayout_9.addWidget(self.content_bar_3)

        self.stackedWidget.addWidget(self.page_reg)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.wrapper_stacked)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.btn_minimize_2.setText(QCoreApplication.translate("MainWindow", u"\u2013", None))
        self.btn_close_2.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f \u0438 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.edit_login_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.edit_password_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.tip_email_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 email \u0430\u0434\u0440\u0435\u0441", None))
        self.tip_password_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_show_password_2.setText("")
        self.btn_signin_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.btn_signin_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label_forgot_password_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0431\u044b\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c?", None))
        self.label_7.setText("")
        self.btn_minimize_3.setText(QCoreApplication.translate("MainWindow", u"\u2013", None))
        self.btn_close_3.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.edit_login_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.edit_password_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.tip_email_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 email \u0430\u0434\u0440\u0435\u0441", None))
        self.tip_password_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.confirm_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.edit_user_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043a \u0432\u0430\u0441 \u0437\u043e\u0432\u0443\u0442?", None))
        self.btn_signin_5.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
        self.btn_signin_6.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

