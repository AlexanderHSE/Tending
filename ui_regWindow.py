# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_regWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RegWindow(object):
    def setupUi(self, RegWindow):
        if not RegWindow.objectName():
            RegWindow.setObjectName(u"RegWindow")
        RegWindow.resize(524, 600)
        self.centralwidget = QWidget(RegWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(37,37,40);\n"
"border-radius: 40")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.frame)
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
        self.frame_2 = QFrame(self.frame_logo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(25, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_logo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 341, 41))
        self.label.setMinimumSize(QSize(341, 41))
        self.label.setPixmap(QPixmap(u"../../Frame_13.jpg"))

        self.horizontalLayout_2.addWidget(self.frame_3)


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


        self.verticalLayout_4.addWidget(self.title_bar)

        self.content_bar = QFrame(self.frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color:None")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content_bar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_title = QFrame(self.content_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 5))
        self.frame_title.setMaximumSize(QSize(16777215, 100))
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


        self.verticalLayout_2.addWidget(self.frame_title)

        self.frame_login = QFrame(self.content_bar)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_login)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 480, 271))
        self.frame_4.setMinimumSize(QSize(300, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.edit_login = QLineEdit(self.frame_4)
        self.edit_login.setObjectName(u"edit_login")
        self.edit_login.setGeometry(QRect(115, 80, 261, 41))
        self.edit_login.setStyleSheet(u"border-radius: 10px; background-color: rgb(73, 73, 77); color: rgb(180, 180, 189); padding-left: 12px;")
        self.edit_login.setMaxLength(1000)
        self.edit_password = QLineEdit(self.frame_4)
        self.edit_password.setObjectName(u"edit_password")
        self.edit_password.setGeometry(QRect(115, 150, 261, 41))
        self.edit_password.setStyleSheet(u"border-radius: 10px; \n"
"background-color: rgb(73, 73, 77); \n"
"color: rgb(180, 180, 189);\n"
"padding-left: 12px;")
        self.edit_password.setMaxLength(1000)
        self.edit_password.setFrame(False)
        self.edit_password.setEchoMode(QLineEdit.Password)
        self.edit_password.setClearButtonEnabled(False)
        self.tip_email = QLabel(self.frame_4)
        self.tip_email.setObjectName(u"tip_email")
        self.tip_email.setGeometry(QRect(115, 125, 103, 16))
        self.tip_email.setStyleSheet(u"color: rgb(239, 88, 88); font-size: 11px;")
        self.tip_password = QLabel(self.frame_4)
        self.tip_password.setObjectName(u"tip_password")
        self.tip_password.setGeometry(QRect(115, 195, 82, 16))
        self.tip_password.setStyleSheet(u"color: rgb(239, 88, 88); font-size: 11px")
        self.confirm_password = QLineEdit(self.frame_4)
        self.confirm_password.setObjectName(u"confirm_password")
        self.confirm_password.setGeometry(QRect(115, 220, 261, 41))
        self.confirm_password.setStyleSheet(u"border-radius: 10px; \n"
"background-color: rgb(73, 73, 77); \n"
"color: rgb(180, 180, 189);\n"
"padding-left: 12px;")
        self.confirm_password.setMaxLength(1000)
        self.confirm_password.setFrame(False)
        self.confirm_password.setEchoMode(QLineEdit.Password)
        self.confirm_password.setClearButtonEnabled(False)
        self.edit_user_name = QLineEdit(self.frame_4)
        self.edit_user_name.setObjectName(u"edit_user_name")
        self.edit_user_name.setGeometry(QRect(115, 20, 261, 41))
        self.edit_user_name.setStyleSheet(u"border-radius: 10px; background-color: rgb(73, 73, 77); color: rgb(180, 180, 189); padding-left: 12px;")
        self.edit_user_name.setMaxLength(1000)
        self.frame_forgot_password = QFrame(self.frame_login)
        self.frame_forgot_password.setObjectName(u"frame_forgot_password")
        self.frame_forgot_password.setGeometry(QRect(0, 280, 502, 131))
        self.frame_forgot_password.setFrameShape(QFrame.StyledPanel)
        self.frame_forgot_password.setFrameShadow(QFrame.Raised)
        self.btn_signin = QPushButton(self.frame_forgot_password)
        self.btn_signin.setObjectName(u"btn_signin")
        self.btn_signin.setGeometry(QRect(110, 20, 111, 28))
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
"")
        self.btn_signin_2 = QPushButton(self.frame_forgot_password)
        self.btn_signin_2.setObjectName(u"btn_signin_2")
        self.btn_signin_2.setGeometry(QRect(260, 20, 131, 28))
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
"")

        self.verticalLayout_2.addWidget(self.frame_login)


        self.verticalLayout_4.addWidget(self.content_bar)


        self.verticalLayout.addWidget(self.frame)

        RegWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegWindow)

        QMetaObject.connectSlotsByName(RegWindow)
    # setupUi

    def retranslateUi(self, RegWindow):
        RegWindow.setWindowTitle(QCoreApplication.translate("RegWindow", u"MainWindow", None))
        self.label.setText("")
        self.btn_minimize.setText(QCoreApplication.translate("RegWindow", u"\u2013", None))
        self.btn_close.setText(QCoreApplication.translate("RegWindow", u"\u00d7", None))
        self.label_2.setText(QCoreApplication.translate("RegWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.edit_login.setPlaceholderText(QCoreApplication.translate("RegWindow", u"Email", None))
        self.edit_password.setPlaceholderText(QCoreApplication.translate("RegWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.tip_email.setText(QCoreApplication.translate("RegWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 email \u0430\u0434\u0440\u0435\u0441", None))
        self.tip_password.setText(QCoreApplication.translate("RegWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.confirm_password.setPlaceholderText(QCoreApplication.translate("RegWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.edit_user_name.setPlaceholderText(QCoreApplication.translate("RegWindow", u"\u041a\u0430\u043a \u0432\u0430\u0441 \u0437\u043e\u0432\u0443\u0442?", None))
        self.btn_signin.setText(QCoreApplication.translate("RegWindow", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
        self.btn_signin_2.setText(QCoreApplication.translate("RegWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

