from main import *


GLOBAL_STATE = 0


class UIFunctions(LogWindow):

    def uiDefinitions(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.btn_minimize_2.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_minimize_3.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close_2.clicked.connect(lambda: self.close())
        self.ui.btn_close_3.clicked.connect(lambda: self.close())
