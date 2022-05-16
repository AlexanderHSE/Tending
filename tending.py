import tinkoff.invest
from tinkoff.invest import Client, PositionsResponse, MoneyValue, GetAccountsResponse, RequestError, Account
import pandas as pd
import ApiParsing
import AllPortfolio
import Portfolio
import Analytics
from tinkoff.invest.services import Services
from tinkoff.invest.schemas import Share


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

def choice_parsing():
    print("Выберите способ парсинга")
    print("1. api")
    print("2. Excel")


'''
t.o0Ddqkri-Cf1Xmm6JsYSPdWFrA50JCU0Jy0HJXN_d1ZTAt3TiQopmfyxI3Rbmg8ltHmwx9GXh9Q1fAGBi8Xu7A
'''
token  = 't.o0Ddqkri-Cf1Xmm6JsYSPdWFrA50JCU0Jy0HJXN_d1ZTAt3TiQopmfyxI3Rbmg8ltHmwx9GXh9Q1fAGBi8Xu7A'
if __name__ == "__main__":
    with Client(token) as client:
        sec = set()
        cur = client.instruments.currencies(instrument_status = 2)
        shar = client.instruments.shares(instrument_status=2)
        bon = client.instruments.bonds(instrument_status=2)
        etf = client.instruments.etfs(instrument_status=2)
        fut = client.instruments.futures(instrument_status=2)
        mun = list()
        for x in shar.instruments:
            sec.add(x.sector)
            if x.sector == 'municipal':
                print(1)
                mun.append(x.name)
        for x in bon.instruments:
            sec.add(x.sector)
            if x.sector == 'municipal':
                print(2)
                mun.append(x.name)
        for x in etf.instruments:
            sec.add(x.sector)
            if x.sector == 'municipal':
                print(3)
                mun.append(x.name)
        for x in fut.instruments:
            sec.add(x.sector)
            if x.sector == 'municipal':
                print(4)
                mun.append(x.name)
        print(mun)
        print(len(sec))
        for x in sec:
            print(x)

        for x in cur.instruments:
            print(f"{x.name} {x.currency} {x.country_of_risk_name}")
    choice_parsing()
    choice = int(input())
    if choice == 1:
        # pars with api
        # получение всех аккаунтов
        api = ApiParsing.ApiParsing()
        api.get_accounts()
        # Получение одного аккаунта
        port = Portfolio.Portfolio(api.accounts.accounts, api.token)
        port.get_one_acc()
        print(port.account)
        # Добавление аккаунта в список аккаунтов
        all_ports = AllPortfolio.AllPortfolio()
        all_ports.add(port.account)
        # Добавление еще одного портфеля
        # Получение одного аккаунта
        port1 = Portfolio.Portfolio(api.accounts.accounts, api.token)
        port1.get_one_acc()
        # Добавление аккаунта в список аккаунтов
        all_ports.add(port1.account)
        port.get_analytics()
    else :
        # pars with xlsx
        pass
    # print("************************")
    #  with Client(TOKEN) as client:
    #     print(type(client))
    #     x = client.users.get_accounts()
    #     print(type(x))
    #     y = x.accounts[0]
    #     r: PositionsResponse = client.operations.get_portfolio(account_id=y.id)
    #     df = pd.DataFrame([{
    #         'figi': p.figi,
    #         'quantity': int(p.quantity),
    #         'expected_yield': float(p.expected_yield),
    #         'instrument_type': p.instrument_type,
    #         'average_buy_price': cast_money(p.average_position_price),
    #         'currency': p.average_position_price.currency,
    #         'nkd': cast_money(r.current_nkd)
    #     } for p in r.positions])
    #     print(df.head(2))
