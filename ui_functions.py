from main import *


GLOBAL_STATE = 0


class UIFunctions(MainWindow):

    def uiDefinitions(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda: self.close())
