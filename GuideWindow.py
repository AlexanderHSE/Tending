from PySide2.QtWidgets import (QDialog, QLabel, QVBoxLayout, QFrame)
from PySide2.QtGui import (QFontDatabase, QMovie, QPixmap)
from PySide2.QtCore import (Qt, QRect)
from PySide2.QtCore import (QEvent)
from ui_guide import Ui_Dialog
import ui_functions


class GuideWindow(QDialog):
    def __init__(self):
        QFontDatabase.addApplicationFont('fonts/Ubuntu-Regular.ttf')
        QFontDatabase.addApplicationFont('fonts/OpenSans-Regular.ttf')
        QDialog.__init__(self)
        self.dragPos = None
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.label_gif = QLabel()
        self.label_gif_input_token = QLabel()
        self.label_gif_portfolio = QLabel()
        self.label_gif_analytics = QLabel()

        self.gif = QMovie('images/get_token (2).gif')
        self.gif_input_token = QMovie('images/input_token (2).gif')
        self.gif_portfolio = QMovie('images/portfolio.gif')
        self.gif_analytics = QMovie('images/gif_analytics.gif')

        self.items_scroll_area = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.ui.scrollArea.verticalScrollBar().setStyleSheet('QScrollBar {width:0px;}')
        self.createGetTokenFrame()
        self.createInputTokenInstruction()
        self.createMainPortfolioInstruction()
        self.createAnalyticsInstruction()

        def moveWindow(event):
            # If left click - move window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.title_bar_guide_window.mouseMoveEvent = moveWindow

        ui_functions.UIFuncsGuide.uiDefinitions(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def enterEvent(self, e):
        # QtWidgets.QLabel.enterEvent(self, e)
        super().enterEvent(e)

    def leaveEvent(self, e):
        # QtWidgets.QLabel.leaveEvent(self, e)
        super().leaveEvent(e)

    def eventFilter(self, obj, event: QEvent):
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

    def gif_starter(self):
        self.gif.start()

    def gif_starter_input_token(self):
        self.gif_input_token.start()

    def gif_starter_portfolio(self):
        self.gif_portfolio.start()

    def gif_starter_analytics(self):
        self.gif_analytics.start()

    def gif_stopper(self):
        self.gif.stop()

    def gif_stopper_input_token(self):
        self.gif_input_token.stop()

    def gif_stopper_portfolio(self):
        self.gif_portfolio.stop()

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
        icon = QPixmap('images/placeholder_gif.png')
        self.label_gif.setPixmap(icon)
        self.gif.setSpeed(70)
        self.label_gif.setMovie(self.gif)
        self.label_gif.installEventFilter(self)
        self.gif.start()
        self.gif.stop()

    def createInputTokenInstruction(self):
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
        self.gif_input_token.start()
        self.gif_input_token.stop()

    def createMainPortfolioInstruction(self):

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

        label_portfolio = QLabel('Текст1')
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
        self.label_gif_portfolio.setFixedSize(670, 370)
        self.gif_portfolio.setSpeed(200)
        self.label_gif_portfolio.setMovie(self.gif_portfolio)
        self.label_gif_portfolio.installEventFilter(self)
        portfolio_layout.addWidget(self.label_gif_portfolio)
        self.gif_portfolio.start()
        self.gif_portfolio.stop()

        self.items_scroll_area.addWidget(label_container_portfolio)

    def createAnalyticsInstruction(self):
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
        label_an = QLabel('Текст 2')
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
        self.gif_analytics.start()
        self.gif_analytics.stop()
