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


class UIFuncs(MainWindow):

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1

            self.ui.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame.setStyleSheet(".QFrame#frame {border-radius: 0px;}* {background-color: rgb(37,37,40);}")
            new_icon = QPixmap('minimize-2.png')
            self.ui.btn_maximize_restore.setIcon(QIcon(new_icon))
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.verticalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.frame.setStyleSheet(".QFrame#frame {border-radius: 30px;}* {background-color: rgb(37,37,40);}")
            new_icon = QPixmap('maximize-2.png')
            self.ui.btn_maximize_restore.setIcon(QIcon(new_icon))

    def uiDefinitions(self):

        # Установка соответствия для size grip
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("QSizeGrip {width: 20px; height: 17px;}")

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # Сворачивание окна
        self.ui.btn_minimize_2.clicked.connect(lambda: self.showMinimized())
        # Закрытие окна
        self.ui.btn_close_2.clicked.connect(lambda: self.close())
        # Разворачивание/сворачивание окна
        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFuncs.maximize_restore(self))

    def returnStatus(self):
        return GLOBAL_STATE