from tinkoff.invest import Client, PositionsResponse, MoneyValue, GetAccountsResponse, RequestError, Account
import pandas as pd
import Portfolio
from tinkoff.invest.services import Services


def cast_money(money_value: MoneyValue):
    """
    Получение стоимости актива в определенной валюте.
    :param money_value: Денежная сумма в определенной валюте.
    :return: Получает стоимость актива в определенной валюте.
    """
    return money_value.units + money_value.nano / 1e9


def get_accounts(self: str) -> GetAccountsResponse:
    client: Services
    try:
        with Client(self) as client:
            return client.users.get_accounts()
    except RequestError:
        print("error!")


TOKEN = 't.o0Ddqkri-Cf1Xmm6JsYSPdWFrA50JCU0Jy0HJXN_d1ZTAt3TiQopmfyxI3Rbmg8ltHmwx9GXh9Q1fAGBi8Xu7A'
if __name__ == "__main__":
    port = Portfolio.Portfolio()
    print(port.token)
    print()
    print(port.accounts)
    print("************************")
    portfolio = Portfolio.Portfolio()
    token = portfolio.__get_token()
    print(token)
    accounts = get_accounts(token)
    print(accounts)
    ''' with Client(TOKEN) as client:
        print(type(client))
        x = client.users.get_accounts()
        print(type(x))
        y = x.accounts[0]
        r: PositionsResponse = client.operations.get_portfolio(account_id=y.id)
        df = pd.DataFrame([{
            'figi': p.figi,
            'quantity': int(p.quantity),
            'expected_yield': float(p.expected_yield),
            'instrument_type': p.instrument_type,
            'average_buy_price': cast_money(p.average_position_price),
            'currency': p.average_position_price.currency,
            'nkd': cast_money(r.current_nkd)
        } for p in r.positions])
        print(df.head(2))'''
