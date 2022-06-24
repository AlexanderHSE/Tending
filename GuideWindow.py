import os
import sys
from PySide2.QtWidgets import (QDialog, QLabel, QVBoxLayout, QFrame)
from PySide2.QtGui import (QFontDatabase, QMovie, QPixmap)
from PySide2.QtCore import (Qt, QRect)
from PySide2.QtCore import (QEvent)
from ui_guide import Ui_Dialog
import ui_functions


def resource_path(relative_path):
    """
    Получает абсолютный путь к ресурсу, используется PyInstaller
    """
    try:
        # PyInstaller создаёт временную папку и сохраняет путь в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class GuideWindow(QDialog):
    """
    Класс, создающий окно обучения
    """
    def __init__(self):
        QFontDatabase.addApplicationFont(resource_path('fonts/Ubuntu-Regular.ttf'))
        QFontDatabase.addApplicationFont(resource_path('fonts/OpenSans-Regular.ttf'))
        QDialog.__init__(self)
        self.dragPos = None
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.label_gif = QLabel()
        self.label_gif_input_token = QLabel()
        self.label_gif_portfolio = QLabel()
        self.label_gif_analytics = QLabel()

        # Подключение GIF
        self.gif = QMovie(resource_path('images/get_token (2).gif'))
        self.gif_input_token = QMovie(resource_path('images/input_token (2).gif'))
        self.gif_portfolio = QMovie(resource_path('images/portfolio.gif'))
        self.gif_analytics = QMovie(resource_path('images/gif_analytics.gif'))

        self.items_scroll_area = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.ui.scrollArea.verticalScrollBar().setStyleSheet('QScrollBar {width:0px;}')
        self.createGetTokenFrame()
        self.createInputTokenInstruction()
        self.createMainPortfolioInstruction()
        self.createAnalyticsInstruction()

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.title_bar_guide_window.mouseMoveEvent = moveWindow

        ui_functions.UIFuncsGuide.uiDefinitions(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # Переопределение события ввода курсора в область
    def enterEvent(self, e):
        super().enterEvent(e)

    # Переопределение события выхода курсора из области
    def leaveEvent(self, e):
        super().leaveEvent(e)

    # Переопределение фильтра событий
    def eventFilter(self, obj, event: QEvent):
        """
        При попадании курсора в одно из четырёх GIF-изображений, запускается соответствующая функция запуска воспроизведения GIF

        При перемещении курсора с GIF-изображения, запускается функция, выполняющая остановку воспроизведения GIF
        """
        if obj == self.label_gif and event.type() == QEvent.Enter:
            self.gif_starter()
            return False
        if obj == self.label_gif_input_token and event.type() == QEvent.Enter:
            self.gif_starter_input_token()
            return False
        if obj == self.label_gif_portfolio and event.type() == QEvent.Enter:
            self.gif_portfolio.start()
            return False
        if obj == self.label_gif_analytics and event.type() == QEvent.Enter:
            self.gif_starter_analytics()
            return False

        if obj == self.label_gif and event.type() == QEvent.Leave:
            self.gif_stopper()
            return False
        if obj == self.label_gif_input_token and event.type() == QEvent.Leave:
            self.gif_stopper_input_token()
            return False
        if obj == self.label_gif_portfolio and event.type() == QEvent.Leave:
            self.gif_portfolio.stop()
            return False
        if obj == self.label_gif_analytics and event.type() == QEvent.Leave:
            self.gif_analytics.stop()
            return False
        return super().eventFilter(obj, event)

    # Функция запуска GIF-изображения get_token (2).gif
    def gif_starter(self):
        self.gif.start()

    # Функция запуска GIF-изображения input_token (2).gif
    def gif_starter_input_token(self):
        self.gif_input_token.start()

    # Функция запуска GIF-изображения portfolio.gif
    def gif_starter_portfolio(self):
        self.gif_portfolio.start()

    # Функция запуска GIF-изображения gif_analytics.gif
    def gif_starter_analytics(self):
        self.gif_analytics.start()

    # Функция остановки GIF-изображения get_token (2).gif
    def gif_stopper(self):
        self.gif.stop()

    # Функция остановки GIF-изображения input_token (2).gif
    def gif_stopper_input_token(self):
        self.gif_input_token.stop()

    # Функция остановки GIF-изображения portfolio.gif
    def gif_stopper_portfolio(self):
        self.gif_portfolio.stop()

    # Функция остановки GIF-изображения gif_analytics.gif
    def gif_stopper_analytics(self):
        self.gif_analytics.stop()

    def createGetTokenFrame(self):
        """
        Создание заголовка 'Получение токена': QLabel

        Создание блока с гиф-инструкцией по получению токена: QLabel
        """
        self.items_scroll_area.setAlignment(Qt.AlignTop)
        label_container = QFrame(self.ui.scrollAreaWidgetContents)
        label_container.setObjectName('label_container')
        label_container.setGeometry(QRect(45, 0, 830, 550))
        label_container.setFrameShape(QFrame.StyledPanel)
        label_container.setFrameShadow(QFrame.Raised)
        label_container_layout = QVBoxLayout(label_container)
        label_container_layout.setAlignment(Qt.AlignHCenter)
        label_container.setStyleSheet('''
            background-color: #222226;
            padding-left: 0px;
        ''')
        label_name = QLabel('Получение токена')
        label_name.setObjectName('label_name')
        label_name.setGeometry(QRect(0, 0, 150, 20))
        label_name.setStyleSheet('''
            font-size : 16px; 
            font-family : Open Sans;
            color: #F9F9FB;
        ''')
        label_name.setAlignment(Qt.AlignCenter)
        label_container_layout.addWidget(label_name)
        self.items_scroll_area.addWidget(label_container)

        self.label_gif.setObjectName('label_gif')
        self.label_gif.setFixedSize(750, 500)
        self.label_gif.setAlignment(Qt.AlignCenter)
        self.label_gif.adjustSize()
        label_container_layout.addWidget(self.label_gif)
        icon = QPixmap(resource_path('images/placeholder_gif.png'))
        self.label_gif.setPixmap(icon)
        self.gif.setSpeed(70)
        self.label_gif.setMovie(self.gif)
        self.label_gif.installEventFilter(self)
        # Вызывается для начальной отрисовки GIF
        self.gif.start()
        self.gif.stop()

    def createInputTokenInstruction(self):
        """
        Создание заголовка 'Ввод токена и выбор счёта': QLabel

        Создание блока с гиф-инструкцией по вводу токена и получению счёта: QLabel
        """
        self.items_scroll_area.setAlignment(Qt.AlignTop)
        about_token_input_container = QFrame(self.ui.scrollAreaWidgetContents)
        about_token_input_container.setObjectName('about_token_input_container')
        about_token_input_container.setGeometry(QRect(45, 0, 830, 330))
        about_token_input_container.setFrameShape(QFrame.StyledPanel)
        about_token_input_container.setFrameShadow(QFrame.Raised)
        about_layout = QVBoxLayout(about_token_input_container)
        about_layout.setAlignment(Qt.AlignCenter)
        about_token_input_container.setStyleSheet('''
            background-color: #222226;
            padding-left: 0px;
        ''')

        label_about = QLabel('Ввод токена и выбор счёта')
        label_about.setObjectName('label_about')
        label_about.setGeometry(QRect(0, 0, 150, 200))
        label_about.setStyleSheet('''
            font-size : 16px; 
            font-family : Open Sans;
            color: #F9F9FB;
        ''')
        label_about.setAlignment(Qt.AlignCenter)
        about_layout.addWidget(label_about)

        self.items_scroll_area.addWidget(about_token_input_container)

        self.label_gif_input_token.setObjectName('label_gif_input_token')
        self.label_gif_input_token.setAlignment(Qt.AlignCenter)
        self.label_gif_input_token.adjustSize()
        self.label_gif_input_token.setFixedSize(450, 370)
        self.gif_input_token.setSpeed(150)
        self.label_gif_input_token.setMovie(self.gif_input_token)
        self.label_gif_input_token.installEventFilter(self)
        about_layout.addWidget(self.label_gif_input_token)
        # Вызывается для начальной отрисовки GIF
        self.gif_input_token.start()
        self.gif_input_token.stop()

    def createMainPortfolioInstruction(self):
        """
        Создание заголовка 'Обзор страницы Портфель': QLabel

        Создание блока с гиф-инструкцией по действиям, выполняемым на странице Портфель: QLabel
        """
        self.items_scroll_area.setAlignment(Qt.AlignTop)
        label_container_portfolio = QFrame(self.ui.scrollAreaWidgetContents)
        label_container_portfolio.setObjectName('portfolio_label_container')
        label_container_portfolio.setGeometry(QRect(45, 0, 830, 330))
        label_container_portfolio.setFrameShape(QFrame.StyledPanel)
        label_container_portfolio.setFrameShadow(QFrame.Raised)
        portfolio_layout = QVBoxLayout(label_container_portfolio)
        portfolio_layout.setAlignment(Qt.AlignCenter)
        label_container_portfolio.setStyleSheet('''
            background-color: #222226;
            padding-left: 0px;
        ''')

        label_portfolio = QLabel('Обзор страницы "Портфель"')
        label_portfolio.setGeometry(QRect(0, 0, 150, 200))
        label_portfolio.setObjectName('label_portfolio')
        label_portfolio.setStyleSheet('''
            font-size : 16px; 
            font-family : Open Sans;
            color: #F9F9FB;
        ''')
        label_portfolio.setAlignment(Qt.AlignCenter)
        portfolio_layout.addWidget(label_portfolio)

        self.label_gif_portfolio.setObjectName('label_gif_portfolio')
        self.label_gif_portfolio.setAlignment(Qt.AlignCenter)
        self.label_gif_portfolio.adjustSize()
        self.label_gif_portfolio.setFixedSize(470, 370)
        self.gif_portfolio.setSpeed(200)
        self.label_gif_portfolio.setMovie(self.gif_portfolio)
        self.label_gif_portfolio.installEventFilter(self)
        portfolio_layout.addWidget(self.label_gif_portfolio)
        # Вызывается для начальной отрисовки GIF
        self.gif_portfolio.start()
        self.gif_portfolio.stop()

        self.items_scroll_area.addWidget(label_container_portfolio)

    def createAnalyticsInstruction(self):
        """
        Создание заголовка 'Обзор страницы Аналитика': QLabel

        Создание блока с гиф-инструкцией по действиям, выполняемым на странице Аналитика: QLabel
        """
        self.items_scroll_area.setAlignment(Qt.AlignTop)
        label_analytics_container = QFrame(self.ui.scrollAreaWidgetContents)
        label_analytics_container.setObjectName('analytics_container')
        label_analytics_container.setGeometry(QRect(45, 0, 830, 550))
        label_analytics_container.setFrameShape(QFrame.StyledPanel)
        label_analytics_container.setFrameShadow(QFrame.Raised)
        analytics_container = QVBoxLayout(label_analytics_container)
        analytics_container.setAlignment(Qt.AlignHCenter)
        label_analytics_container.setStyleSheet('''
            background-color: #222226;
            padding-left: 0px;
        ''')
        label_an = QLabel('Обзор страницы "Аналитика"')
        label_an.setObjectName('label_analytics')
        label_an.setGeometry(QRect(0, 0, 150, 20))
        label_an.setStyleSheet('''
            font-size : 16px; 
            font-family : Open Sans;
            color: #F9F9FB;
        ''')
        label_an.setAlignment(Qt.AlignCenter)
        analytics_container.addWidget(label_an)
        self.items_scroll_area.addWidget(label_analytics_container)

        self.label_gif_analytics.setObjectName('label_gif')
        self.label_gif_analytics.setFixedSize(470, 370)
        self.label_gif_analytics.setAlignment(Qt.AlignCenter)
        self.label_gif_analytics.adjustSize()
        analytics_container.addWidget(self.label_gif_analytics)
        self.gif_analytics.setSpeed(150)
        self.label_gif_analytics.setMovie(self.gif_analytics)
        self.label_gif_analytics.installEventFilter(self)
        # Вызывается для начальной отрисовки GIF
        self.gif_analytics.start()
        self.gif_analytics.stop()
