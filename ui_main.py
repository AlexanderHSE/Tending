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


class Ui_MainWindowBase(object):
    def setupUi(self, MainWindowBase):
        if not MainWindowBase.objectName():
            MainWindowBase.setObjectName(u"MainWindowBase")
        MainWindowBase.resize(799, 600)
        self.centralwidget = QWidget(MainWindowBase)
        self.centralwidget.setObjectName(u"centralwidget")
        self.to_login = QPushButton(self.centralwidget)
        self.to_login.setObjectName(u"to_login")
        self.to_login.setGeometry(QRect(180, 110, 93, 28))
        MainWindowBase.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowBase)

        QMetaObject.connectSlotsByName(MainWindowBase)
    # setupUi

    def retranslateUi(self, MainWindowBase):
        MainWindowBase.setWindowTitle(QCoreApplication.translate("MainWindowBase", u"MainWindow", None))
        self.to_login.setText(QCoreApplication.translate("MainWindowBase", u"PushButton", None))
    # retranslateUi

