from tending import get_set_positions
from tinkoff.invest import Client
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.io as pio
import plotly

token = "t.o0Ddqkri-Cf1Xmm6JsYSPdWFrA50JCU0Jy0HJXN_d1ZTAt3TiQopmfyxI3Rbmg8ltHmwx9GXh9Q1fAGBi8Xu7A"

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
                       color_discrete_sequence=list(df['color']), hover_data=['ticker'],
                       labels={"name": "Название", "ticker": "Тикер"}, hole=0.3)
    pie_chart.update_traces()
    pie_chart.show()
    pie_chart.update_traces(textposition='inside', textinfo='percent+label', showlegend=False )
    pie_chart.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    plotly.offline.plot(pie_chart, filename="MainPieChart.html")