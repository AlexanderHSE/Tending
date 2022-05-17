# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setMinimumSize(QSize(502, 581))
        self.drop_shadow_frame.setMaximumSize(QSize(502, 581))
        self.drop_shadow_frame.setStyleSheet(u"background-color: rgb(37,37,40);\n"
"border-radius: 40;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(502, 70))
        self.title_bar.setMaximumSize(QSize(16777215, 70))
        self.title_bar.setStyleSheet(u"background-color:None")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_logo = QFrame(self.title_bar)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_logo)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_logo)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(25, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_logo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 341, 41))
        self.label.setMinimumSize(QSize(341, 41))
        self.label.setPixmap(QPixmap(u"../../Frame_13.jpg"))

        self.horizontalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame_logo)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(20, 20))
        self.btn_minimize.setMaximumSize(QSize(40, 40))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color: rgb(155, 156, 151);\n"
"	font-family: Ubuntu;\n"
"	font-size: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(234, 234, 234)\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(20, 20))
        self.btn_close.setMaximumSize(QSize(40, 40))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color: rgb(155, 156, 151);\n"
"	font-family: Ubuntu;\n"
"	font-size: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(234, 234, 234)\n"
"}")
        self.btn_close.setFlat(False)

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color:None")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content_bar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.content_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 5))
        self.frame_title.setMaximumSize(QSize(16777215, 200))
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_title)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 15, 0, 0)
        self.label_2 = QLabel(self.frame_title)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setStyleSheet(u"color: rgb(249, 249, 251);\n"
"font-size: 37px;\n"
"font-family: \"Ubuntu\";")
        self.label_2.setTextFormat(Qt.MarkdownText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_title)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setStyleSheet(u"color: rgb(249, 249, 251);\n"
"font-size: 13px;\n"
"font-family: \"Ubuntu\";")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_3.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_title)

        self.frame_login = QFrame(self.content_bar)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_login)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 10, 480, 149))
        self.frame_3.setMinimumSize(QSize(300, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.edit_login = QLineEdit(self.frame_3)
        self.edit_login.setObjectName(u"edit_login")
        self.edit_login.setGeometry(QRect(115, -1, 261, 41))
        self.edit_login.setStyleSheet(u"border-radius: 10px; background-color: rgb(73, 73, 77); color: rgb(180, 180, 189); padding-left: 12px;")
        self.edit_login.setMaxLength(1000)
        self.edit_password = QLineEdit(self.frame_3)
        self.edit_password.setObjectName(u"edit_password")
        self.edit_password.setGeometry(QRect(115, 80, 261, 41))
        self.edit_password.setStyleSheet(u"border-radius: 10px; \n"
"background-color: rgb(73, 73, 77); \n"
"color: rgb(180, 180, 189);\n"
"padding-left: 12px;")
        self.edit_password.setMaxLength(1000)
        self.edit_password.setFrame(False)
        self.edit_password.setEchoMode(QLineEdit.Password)
        self.edit_password.setClearButtonEnabled(False)
        self.tip_email = QLabel(self.frame_3)
        self.tip_email.setObjectName(u"tip_email")
        self.tip_email.setGeometry(QRect(115, 50, 103, 16))
        self.tip_email.setStyleSheet(u"color: rgb(239, 88, 88); font-size: 11px;")
        self.tip_password = QLabel(self.frame_3)
        self.tip_password.setObjectName(u"tip_password")
        self.tip_password.setGeometry(QRect(115, 130, 82, 16))
        self.tip_password.setStyleSheet(u"color: rgb(239, 88, 88); font-size: 11px")
        self.btn_show_password = QPushButton(self.frame_3)
        self.btn_show_password.setObjectName(u"btn_show_password")
        self.btn_show_password.setGeometry(QRect(350, 90, 21, 21))
        self.btn_show_password.setStyleSheet(u"border:none; background: none;")
        icon = QIcon()
        icon.addFile(u"closedEyeChanged.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_show_password.setIcon(icon)
        self.frame_forgot_password = QFrame(self.frame_login)
        self.frame_forgot_password.setObjectName(u"frame_forgot_password")
        self.frame_forgot_password.setGeometry(QRect(0, 150, 502, 170))
        self.frame_forgot_password.setFrameShape(QFrame.StyledPanel)
        self.frame_forgot_password.setFrameShadow(QFrame.Raised)
        self.btn_signin = QPushButton(self.frame_forgot_password)
        self.btn_signin.setObjectName(u"btn_signin")
        self.btn_signin.setGeometry(QRect(120, 40, 111, 28))
        self.btn_signin.setStyleSheet(u"QPushButton {\n"
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
        self.btn_signin_2 = QPushButton(self.frame_forgot_password)
        self.btn_signin_2.setObjectName(u"btn_signin_2")
        self.btn_signin_2.setGeometry(QRect(260, 40, 131, 28))
        self.btn_signin_2.setStyleSheet(u"QPushButton {\n"
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
        self.label_forgot_password = QLabel(self.frame_forgot_password)
        self.label_forgot_password.setObjectName(u"label_forgot_password")
        self.label_forgot_password.setGeometry(QRect(120, 80, 111, 16))
        self.label_forgot_password.setStyleSheet(u"QLabel {\n"
"color: rgb(249, 249, 251);\n"
"font-size: 11px;\n"
"font-family: \"Ubuntu\";\n"
"font-weight: bold;\n"
"}\n"
"QLabel:hover {\n"
"color: rgb(196, 186, 208);\n"
"}")

        self.verticalLayout_2.addWidget(self.frame_login)


        self.verticalLayout.addWidget(self.content_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.btn_minimize.setText(QCoreApplication.translate("MainWindow", u"\u2013", None))
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f \u0438 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.edit_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.edit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.tip_email.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 email \u0430\u0434\u0440\u0435\u0441", None))
        self.tip_password.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_show_password.setText("")
        self.btn_signin.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.btn_signin_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label_forgot_password.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0431\u044b\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c?", None))
    # retranslateUi

