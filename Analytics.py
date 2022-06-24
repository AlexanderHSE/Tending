from tinkoff.invest import Client, PortfolioPosition
import pandas as pd
import Instr

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


class Analytics:
    """
    Класс, реализующий анализ данных портфеля
    """
    __slots__ = (
        '__account', '__token', '__portfolio', '__opened_date', '__dt', '__usdrur', '__client', '__instruments')

    dict_sector = dict(government="Государтсвенные бумаги", energy="Энергетика", ecomaterials="Промышленность",
                       green_energy="Зелёная энергетика", financial="Финансы", utilities="Коммунальные услуги",
                       materials="Материалы", green_buildings="Промышленность", municipal="Муниципальные бумаги",
                       other="Другое", industrials="Промышленность", it="Информационные технологии",
                       health_care="Здравоохранение", telecom="Услуги связи", consumer="Потребительский сектор",
                       real_estate="Недвижимость", electrocars="Промышленность", currency="Валюта", etf="ETF",
                       bond="Облигация")
    dict_instrument_type = dict(share="Акция", bond="Облигация", etf="Фонд", currency="Валюта", future="Фьючерс")

    def __init__(self, account, token):
        self.account = account
        self.opened_date = account.opened_date
        with Client(token) as client:
            self.token = token
            self.portfolio = client.operations.get_portfolio(account_id=self.account.id)
            self.__instruments = client.instruments
            u = client.market_data.get_last_prices(figi=['USD000UTSTOM'])
            self.usdrur = Analytics.cast_money(u.last_prices[0].price)
            self.client = client

    # Получаем client
    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, _client):
        self.__client = _client

    # Получаем token
    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, _token):
        self.__token = _token

    # Получаем instruments
    @property
    def instruments(self):
        return self.__instruments

    @instruments.setter
    def instruments(self, _instruments):
        self.__instruments = _instruments

    # Получаем счет аккаунта
    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, _account):
        self.__account = _account

    # Получаем портфель
    @property
    def portfolio(self):
        return self.__portfolio

    @portfolio.setter
    def portfolio(self, _portfolio):
        self.__portfolio = _portfolio


    @property
    def usdrur(self):
        return self.__usdrur

    @usdrur.setter
    def usdrur(self, _usdrur):
        self.__usdrur = _usdrur

    # Получение инструментов портфеля
    def get_instrument(self, p):
        ins = Instr.Instr(self.token, p.figi, p.instrument_type)
        return ins.instr

