# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_guide.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(889, 757)
        Dialog.setMaximumSize(QSize(965, 16777215))
        Dialog.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(867, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(37,37,40); border-radius: 30px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_bar_guide_window = QFrame(self.frame)
        self.title_bar_guide_window.setObjectName(u"title_bar_guide_window")
        self.title_bar_guide_window.setMinimumSize(QSize(850, 60))
        self.title_bar_guide_window.setMaximumSize(QSize(850, 60))
        self.title_bar_guide_window.setStyleSheet(u"background-color:None")
        self.title_bar_guide_window.setFrameShape(QFrame.NoFrame)
        self.title_bar_guide_window.setFrameShadow(QFrame.Raised)
        self.frame_logo_2 = QFrame(self.title_bar_guide_window)
        self.frame_logo_2.setObjectName(u"frame_logo_2")
        self.frame_logo_2.setGeometry(QRect(0, 0, 850, 60))
        self.frame_logo_2.setMinimumSize(QSize(0, 60))
        self.frame_logo_2.setMaximumSize(QSize(850, 60))
        self.frame_logo_2.setStyleSheet(u"border-radius-top: 5px;")
        self.frame_logo_2.setFrameShape(QFrame.StyledPanel)
        self.frame_logo_2.setFrameShadow(QFrame.Raised)
        self.frame_space = QFrame(self.frame_logo_2)
        self.frame_space.setObjectName(u"frame_space")
        self.frame_space.setGeometry(QRect(0, 0, 10, 70))
        self.frame_space.setMinimumSize(QSize(10, 70))
        self.frame_space.setMaximumSize(QSize(10, 70))
        self.frame_space.setFrameShape(QFrame.StyledPanel)
        self.frame_space.setFrameShadow(QFrame.Raised)
        self.frame_head = QFrame(self.frame_logo_2)
        self.frame_head.setObjectName(u"frame_head")
        self.frame_head.setGeometry(QRect(10, 0, 322, 51))
        self.frame_head.setFrameShape(QFrame.StyledPanel)
        self.frame_head.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_head)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 300, 41))
        self.label_4.setMinimumSize(QSize(300, 41))
        self.label_4.setPixmap(QPixmap(u"images/Frame_13.jpg"))
        self.btn_close_3 = QPushButton(self.frame_logo_2)
        self.btn_close_3.setObjectName(u"btn_close_3")
        self.btn_close_3.setGeometry(QRect(790, 10, 40, 40))
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
        self.label_5 = QLabel(self.frame_logo_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(370, 10, 121, 41))
        self.label_5.setStyleSheet(u"font-size : 23px; \n"
"font-family : Open Sans;\n"
"color: #F9F9FB;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title_bar_guide_window)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(850, 0))
        self.frame_2.setMaximumSize(QSize(850, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 10, 850, 651))
        self.scrollArea.setMinimumSize(QSize(850, 0))
        self.scrollArea.setMaximumSize(QSize(850, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 850, 651))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText("")
        self.btn_close_3.setText(QCoreApplication.translate("Dialog", u"\u00d7", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0443\u0447\u0435\u043d\u0438\u0435", None))
    # retranslateUi

