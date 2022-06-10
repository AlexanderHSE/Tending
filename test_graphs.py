from tending import get_set_positions
from tinkoff.invest import Client
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.io as pio
import plotly
import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QDir, QUrl


from PySide2 import QtCore, QtWidgets, QtWebEngineWidgets
import plotly.express as px


import plotly
import plotly.graph_objs as go
token = "t.o0Ddqkri-Cf1Xmm6JsYSPdWFrA50JCU0Jy0HJXN_d1ZTAt3TiQopmfyxI3Rbmg8ltHmwx9GXh9Q1fAGBi8Xu7A"





class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QtWidgets.QPushButton('Plot', self)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)

        vlayout = QtWidgets.QVBoxLayout(self)
        vlayout.addWidget(self.button, alignment=QtCore.Qt.AlignHCenter)
        vlayout.addWidget(self.browser)

        self.button.clicked.connect(self.show_graph)
        self.resize(1000, 1000)

    def show_graph(self):
        with Client(token) as client:
            accounts = client.users.get_accounts()
            account = accounts.accounts[0]
            portfolio = client.operations.get_portfolio(account_id=account.id)
            q = get_set_positions(token, client, portfolio)
            print(q)
            df = pd.DataFrame(q)
            print(df)

            # color_discrete_map если цвета будут в другом порядке
            pie_chart = px.pie(data_frame=df, values='portfolio_share', names='name', color='name',
                               color_discrete_sequence=list(df['color']), custom_data=['ticker'],
                               hole=0.3)
            #labels = {"name": "Название", "ticker": "Тикер"},
            hovertemp = "%{label} \n"
            hovertemp += "%{value}%\n\n"
            pie_chart.update_traces(hovertemplate=hovertemp)
            pie_chart.update_traces(textposition='inside', textinfo='percent+label', showlegend=False)
            pie_chart.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            pie_chart.show()



if __name__ == "__main__":
        sys.argv.append("--disable-web-security")
        app = QApplication(sys.argv)
        widget = Widget()
        widget.show()
        sys.exit(app.exec_())