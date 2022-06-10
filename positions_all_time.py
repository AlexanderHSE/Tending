from tinkoff.invest import Client
from datetime import datetime

token =  "t.o0Ddqkri-Cf1Xmm6JsYSPdWFrA50JCU0Jy0HJXN_d1ZTAt3TiQopmfyxI3Rbmg8ltHmwx9GXh9Q1fAGBi8Xu7A"
with Client(token) as client:
    accounts = client.users.get_accounts()
    account = accounts.accounts[0]
    dt_now = datetime.now()
    operations = client.operations.get_operations(account_id=account.id, from_=account.opened_date, to=dt_now, state=1,figi="USD000UTSTOM")
    print(account.opened_date)
    print(type(account.opened_date))