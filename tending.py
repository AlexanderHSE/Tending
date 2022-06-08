from tinkoff.invest import Client, MoneyValue, GetAccountsResponse, RequestError
import ApiParsing
import AllPortfolio
import Portfolio
from tinkoff.invest.services import Services
from tinkoff.invest.schemas import PortfolioResponse, Quotation


def cast_money(money_value: MoneyValue):
    """
    Получение стоимости актива в определенной валюте.
    :param money_value: Денежная сумма в определенной валюте.
    :return: Получает стоимость актива в определенной валюте.
    """
    return money_value.units + money_value.nano / 1e9


def cast_yield(quotation: Quotation):
    return quotation.units + quotation.nano / 1e9


def get_invested_money(total_yield_percentage: float, total_cost: float):
    total_cost_percentage = 100 + total_yield_percentage
    return total_cost / total_cost_percentage * 100


def get_total_profit(total_yield_percentage: float, total_cost: float):
    invested_money = get_invested_money(total_yield_percentage, total_cost)
    return round(total_cost - invested_money, 2)


def get_total_cost_portfolio(portfolio: PortfolioResponse):
    total_amount_shares = cast_money(portfolio.total_amount_shares)
    total_amount_bonds = cast_money(portfolio.total_amount_bonds)
    total_amount_etf = cast_money(portfolio.total_amount_etf)
    total_amount_currencies = cast_money(portfolio.total_amount_currencies)
    total_amount_futures = cast_money(portfolio.total_amount_futures)
    return round(total_amount_shares + total_amount_bonds + total_amount_etf +
                 total_amount_currencies + total_amount_futures, 2)


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
token = 't.o0Ddqkri-Cf1Xmm6JsYSPdWFrA50JCU0Jy0HJXN_d1ZTAt3TiQopmfyxI3Rbmg8ltHmwx9GXh9Q1fAGBi8Xu7A'
if __name__ == "__main__":
    # with Client(token) as client:
    #     dic = dict()
    #     other = list()
    #     consumer = list()
    #     it = list()
    #     green_buildings = list()
    #     energy = list()
    #     government = list()
    #     telecom = list()
    #     industrials = list()
    #     health_care = list()
    #     electrocars = list()
    #     ecomaterials = list()
    #     municipal = list()
    #     financial = list()
    #     utilities = list()
    #     green_energy = list()
    #     real_estate = list()
    #     materials = list()
    #     sec = set()
    #     cur = client.instruments.currencies(instrument_status = 2)
    #     shar = client.instruments.shares(instrument_status=2)
    #     bon = client.instruments.bonds(instrument_status=2)
    #     etf = client.instruments.etfs(instrument_status=2)
    #     fut = client.instruments.futures(instrument_status=2)
    #     mun = list()
    #     for x in shar.instruments:
    #         sec.add(x.sector)
    #         if x.sector == 'municipal':
    #             mun.append(x.name)
    #     for x in bon.instruments:
    #         if x.sector == 'other':
    #             other.append(x.name)
    #         if x.sector == 'consumer':
    #             consumer.append(x.name)
    #         if x.sector == 'it':
    #             it.append(x.name)
    #         if x.sector == 'green_buildings':
    #             green_buildings.append(x.name)
    #         if x.sector == 'energy':
    #             energy.append(x.name)
    #         if x.sector == 'government':
    #             government.append(x.name)
    #         if x.sector == 'telecom':
    #             telecom.append(x.name)
    #         if x.sector == 'industrials':
    #             industrials.append(x.name)
    #         if x.sector == 'health_care':
    #             health_care.append(x.name)
    #         if x.sector == 'electrocars':
    #             electrocars.append(x.name)
    #         if x.sector == 'ecomaterials':
    #             ecomaterials.append(x.name)
    #         if x.sector == 'municipal':
    #             municipal.append(x.name)
    #         if x.sector == 'financial':
    #             financial.append(x.name)
    #         if x.sector == 'utilities':
    #             utilities.append(x.name)
    #         if x.sector == 'green_energy':
    #             green_energy.append(x.name)
    #         if x.sector == 'real_estate':
    #             real_estate.append(x.name)
    #         if x.sector == 'materials':
    #             materials.append(x.name)
    #         sec.add(x.sector)
    #         if x.sector == 'municipal':
    #             mun.append(x.name)
    #     for x in etf.instruments:
    #         sec.add(x.sector)
    #         if x.sector == 'municipal':
    #             mun.append(x.name)
    #     for x in fut.instruments:
    #         sec.add(x.sector)
    #         if x.sector == 'municipal':
    #             print(4)
    #             mun.append(x.name)
    #     print(len(other ))
    #     print(len(consumer ))
    #     print(len(it ))
    #     print(len(green_buildings))
    #     print(len(energy ))
    #     print(len(government ))
    #     print(len(telecom ))
    #     print(len(industrials ))
    #     print(len(health_care ))
    #     print(len(electrocars ))
    #     print(len(ecomaterials ))
    #     print(len(municipal ))
    #     print(len(financial ))
    #     print(len(utilities ))
    #     print(len(green_energy ))
    #     print(len(real_estate ))
    #     print(len(materials ))
    #     for x in sec:
    #         print(x)
    #
    #     dic['other'] =   other
    #     dic['consumer'] = consumer
    #     dic['it'] = it
    #     dic['green_buildings'] = green_buildings
    #     dic['energy'] = energy
    #     dic['government'] = government
    #     dic['telecom'] = telecom
    #     dic['industrials'] = industrials
    #     dic['health_care'] = health_care
    #     dic['electrocars'] = electrocars
    #     dic['ecomaterials'] = ecomaterials
    #     dic['municipal'] = municipal
    #     dic['financial'] = financial
    #     dic['utilities'] = utilities
    #     dic['green_energy'] = green_energy
    #     dic[' real_estate'] = real_estate
    #     dic['materials'] = materials
    #     for key in dic.keys():
    #         print(key)
    #         print(dic[key])
    choice_parsing()
    choice = int(input())
    if choice == 1:
        # pars with api
        # получение всех аккаунтов
        api = ApiParsing.ApiParsing()
        api.get_accounts()
        # Получение одного аккаунта
        print(api.accounts.accounts)
        port = Portfolio.Portfolio(api.accounts.accounts, api.token)
        print(port)
        print(1)
        print(type(port))
        print('get_one_acc')
        port.get_one_acc()
        print('port.account')
        print(port.account)
        print(type(port.account))
        print(1)
        # Добавление аккаунта в список аккаунтов
        all_ports = AllPortfolio.AllPortfolio()

        all_ports.add(port.account)
        # Добавление еще одного портфеля
        # Получение одного аккаунта
        port1 = Portfolio.Portfolio(api.accounts.accounts, api.token)
        print(port1)
        print('port1')
        port1.get_one_acc()
        # Добавление аккаунта в список аккаунтов
        all_ports.add(port1.account)
        port.get_analytics()
    else:
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
# 2096003229
# 2095996597
