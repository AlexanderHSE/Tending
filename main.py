import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from qtwidgets import PasswordEdit

from ui_main import Ui_MainWindow
from ui_regWindow import Ui_RegWindow

from ui_functions import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.dragPos = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_show_password.clicked.connect(self.toggleVisibility)
        # Move Window
        def moveWindow(event):
            # If left click - move window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # Set title bar
        self.ui.title_bar.mouseMoveEvent = moveWindow

        UIFunctions.uiDefinitions(self)

        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # Изменение видимости пароля
    def toggleVisibility(self):
        if self.ui.edit_password.echoMode() == QLineEdit.Normal:
            self.ui.edit_password.setEchoMode(QLineEdit.Password)
            new_icon = QPixmap('closedEyeChanged.png')
            self.ui.btn_show_password.setIcon(QIcon(new_icon))
        else:
            self.ui.edit_password.setEchoMode(QLineEdit.Normal)
            new_icon = QPixmap('openedEye.png')
            self.ui.btn_show_password.setIcon(QIcon(new_icon))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
