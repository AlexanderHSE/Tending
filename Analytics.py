from tinkoff.invest import Client, PortfolioPosition, InstrumentIdType, InstrumentStatus
import pandas as pd
import Instr

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


class Analytics:
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

        # Получаем client

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

    # Получаем дату открытия
    @property
    def opened_date(self):
        return self.__opened_date

    @opened_date.setter
    def opened_date(self, _opened_date):
        self.__opened_date = _opened_date

    # Получаем дата фрэйм
    @property
    def df(self):
        return self.__dt

    @df.setter
    def df(self, _dt):
        self.__dt = _dt

        # Получаем дату открытия

    @property
    def usdrur(self):
        return self.__usdrur

    @usdrur.setter
    def usdrur(self, _usdrur):
        self.__usdrur = _usdrur

    # @staticmethod
    # def get_name(figi, instrument_type):
    #     if instrument_type == 'bond':
    #     elif instrument_type == 'share':
    #     elif instrument_type == 'currency':
    #     elif instrument_type == 'etf':

    def get_instrument(self, p):
        ins = Instr.Instr(self.token, p.figi, p.instrument_type)
        return ins.instr

    def portfolio_pose_todict(self, p: PortfolioPosition, usdrur):
        instr = self.get_instrument(p)
        r = {
            'name': instr.name,
            'trading_status': instr.trading_status,
            'buy_available_flag': instr.buy_available_flag,
            "sell_available_flag": instr.sell_available_flag,
            'ticker': "",
            'country': instr.country_of_risk_name,
            'sector': "",
            'quantity': Analytics.cast_money(p.quantity),
            'expected_yield': Analytics.cast_money(p.expected_yield),
            'instrument_type': p.instrument_type,
            'average_buy_price': Analytics.cast_money(p.average_position_price),
            'currency': p.average_position_price.currency,
            'nkd': Analytics.cast_money(p.current_nkd),
        }
        if p.instrument_type == 'currency' or p.instrument_type == 'bond':
            r['ticker'] = ""
            if p.instrument_type == 'currency':
                r['sector'] = "currency"
            else:
                r['sector'] = "bond"
        elif p.instrument_type == 'etf':
            r['sector'] = 'etf'
            r['ticker'] = instr.ticker
        else:
            r['ticker'] = instr.ticker
            r['sector'] = instr.sector
        if r['currency'] != 'rub':
            # если бы expected_yield быk бы тоже MoneyValue,
            # то конвертацию валюты можно было бы вынести в cast_money
            r['expected_yield'] *= usdrur
            r['average_buy_price'] *= usdrur
            r['nkd'] *= usdrur
        r['currency'] = 'Рубль'
        r['sell_sum'] = (r['average_buy_price'] * r['quantity']) + r['expected_yield'] + (r['nkd'] * r['quantity'])
        r['comissixon'] = r['sell_sum'] * 0.003
        r['tax'] = r['expected_yield'] * 0.013 if r['expected_yield'] > 0 else 0
        if len(r['sector']) != 0:
            r['sector'] = Analytics.dict_sector[r['sector']]
        r['instrument_type']  =  Analytics.dict_instrument_type[r['instrument_type']]
        return r

    @staticmethod
    def cast_money(v):
        return v.units + v.nano / 1e9

    def create_df(self):
        self.df = pd.DataFrame(
            [Analytics.portfolio_pose_todict(self, p, self.usdrur) for p in self.portfolio.positions])
        print(self.df.head(100))
        print("bonds", Analytics.cast_money(self.portfolio.total_amount_bonds),
              self.df.query("instrument_type == 'bond'")['sell_sum'].sum(),
              sep=" : ")
        print("etfs", Analytics.cast_money(self.portfolio.total_amount_etf),
              self.df.query("instrument_type == 'etf'")['sell_sum'].sum(), sep=" : ")
        print(self.df['comission'].sum())
