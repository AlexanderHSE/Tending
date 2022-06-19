from main import MainWindow
from GuideWindow import GuideWindow
from PySide2 import QtCore


class UIFuncsGuide(GuideWindow):

    def uiDefinitions(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # Закрытие окна
        self.ui.btn_close_3.clicked.connect(lambda: self.close())


class UIFuncs(MainWindow):

    def uiDefinitions(self):

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # Сворачивание окна
        self.ui.btn_minimize_2.clicked.connect(lambda: self.showMinimized())
        # Закрытие окна
        self.ui.btn_close_2.clicked.connect(lambda: self.close())
