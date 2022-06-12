import pandas as pd
from tinkoff.invest import Client, MoneyValue, GetAccountsResponse, RequestError
import ApiParsing
import AllPortfolio
import Portfolio
from tinkoff.invest.services import Services
from tinkoff.invest.schemas import PortfolioResponse, Quotation, PortfolioPosition
from Instr import Instr
from help_func import generate_random_color

#   t.o0Ddqkri-Cf1Xmm6JsYSPdWFrA50JCU0Jy0HJXN_d1ZTAt3TiQopmfyxI3Rbmg8ltHmwx9GXh9Q1fAGBi8Xu7A
#   t.r3D-SJY-s37p965fw1Co_UvACNdtrcxUW7rq_xIU4GP5d2Ni2XSLB3NlrHSx21ck6eLoenkmV0LXiIx0_uldUw
#   t.6l6UT2g6HYDf_PNb8BIO4PuWeGajBgfQGPHgtTi-bEIgfiSdTKsyVuN17Yv0T0Umxw-TzPnrVTUIe8g3LkL8bg
dict_sector = dict(government="Государтсвенные бумаги", energy="Энергетика", ecomaterials="Промышленность",
                   green_energy="Зелёная энергетика", financial="Финансы", utilities="Коммунальные услуги",
                   materials="Материалы", green_buildings="Промышленность", municipal="Муниципальные бумаги",
                   other="Другое", industrials="Промышленность", it="IT",
                   health_care="Здравоохранение", telecom="Услуги связи", consumer="Потребительский сектор",
                   real_estate="Недвижимость", electrocars="Промышленность", currency="Валюта", etf="ETF",
                   bond="Облигация")

dict_instrument_type = dict(share="Акция", bond="Облигация", etf="Фонд", currency="Валюта", future="Фьючерс")

countries_codes = {}


def cast_money(money_value: MoneyValue):
    return money_value.units + money_value.nano / 1e9


def cast_yield(quotation: Quotation):
    return quotation.units + quotation.nano / 1e9


def get_invested_money(total_yield_percentage: float, total_cost: float):
    total_cost_percentage = 100 + total_yield_percentage
    return total_cost / total_cost_percentage * 100


def get_total_profit(total_yield_percentage: float, total_cost: float):
    invested_money = get_invested_money(total_yield_percentage, total_cost)
    return round(total_cost - invested_money, 2)


def get_total_cost_portfolio(df, portfolio: PortfolioResponse):
    if df.empty:
        return 0
    total_amount_shares = cast_money(portfolio.total_amount_shares)
    total_amount_bonds = cast_money(portfolio.total_amount_bonds)
    total_amount_etf = cast_money(portfolio.total_amount_etf)
    total_amount_currencies = df[df['instrument_type'] == 'Валюта'].agg('sum')['cost']
    total_amount_futures = cast_money(portfolio.total_amount_futures)
    return round(total_amount_shares + total_amount_bonds + total_amount_etf +
                 total_amount_currencies + total_amount_futures, 2)


def get_instrument(token, position):
    ins = Instr(token, position.figi, position.instrument_type)
    return ins.instr


def convert_position_to_dict(token, position: PortfolioPosition, usdrur, eurrur):
    instr = get_instrument(token, position)
    if instr is not None:
        r = {
            'name': instr.name,
            'ticker': "",
            'country': instr.country_of_risk_name,
            'sector': "",
            'quantity': cast_money(position.quantity),
            'expected_yield': cast_money(position.expected_yield),
            'instrument_type': position.instrument_type,
            'average_buy_price': cast_money(position.average_position_price),
            'current_buy_price': cast_money(position.average_position_price) + cast_money(
                position.expected_yield) / cast_money(position.quantity),
            'currency': position.average_position_price.currency,
            'nkd': cast_money(position.current_nkd),
        }

        if int(r['quantity']) - r['quantity'] == 0:
            r['quantity'] = int(r['quantity'])
        if position.instrument_type == 'currency' or position.instrument_type == 'bond':
            r['ticker'] = ""
            if position.instrument_type == 'currency':
                r['sector'] = "currency"
            else:
                r['sector'] = "bond"
        elif position.instrument_type == 'etf':
            r['sector'] = 'etf'
            r['ticker'] = instr.ticker
        else:
            r['ticker'] = instr.ticker
            r['sector'] = instr.sector
        if r['currency'] != 'rub':
            if r['currency'] == 'usd':
                r['current_buy_price'] *= usdrur
                r['expected_yield'] *= usdrur
                r['average_buy_price'] *= usdrur
                r['nkd'] *= usdrur
                r['original_currency'] = 'Доллар США'
            elif r['currency'] == 'eur':
                r['current_buy_price'] *= eurrur
                r['expected_yield'] *= eurrur
                r['average_buy_price'] *= eurrur
                r['original_currency'] = 'Евро'
                r['nkd'] *= eurrur
        else:
            r['original_currency'] = 'Рубль'
        if r['average_buy_price'] != 0:
            r['expected_yield_percentage'] = (r['current_buy_price'] - r['average_buy_price']) / r[
                'average_buy_price'] * 100
        else:
            r['expected_yield_percentage'] = -100
        r['currency'] = '₽'
        r['sell_sum'] = (r['average_buy_price'] * r['quantity']) + r['expected_yield'] + (r['nkd'] * r['quantity'])
        r['comissixon'] = r['sell_sum'] * 0.003
        r['tax'] = r['expected_yield'] * 0.013 if r['expected_yield'] > 0 else 0
        if len(r['sector']) != 0:
            r['sector'] = dict_sector[r['sector']]
        r['instrument_type'] = dict_instrument_type[r['instrument_type']]
        r['cost'] = round(r['quantity'] * r['current_buy_price'], 2)
        return r
    return None


def set_name_brief_contry(dict_pose):
    global countries_codes
    count = list()
    lens = list()
    for country in countries_codes:
        count.append(country.name)
        lens.append(len(country.name_brief))
        if dict_pose['country'] == country.name or dict_pose['country'] == country.name_brief:
            if dict_pose['country'] == 'Виргинские Острова, Британские':
                dict_pose['short_country_name'] = "Соединенное Королевство"
            dict_pose['short_country_name'] = country.name_brief


def set_counrties(token):
    with Client(token) as client:
        global countries_codes
        countries_codes = client.instruments.get_countries().countries


def get_set_positions(token, client, portfolio):
    set_counrties(token)
    u = client.market_data.get_last_prices(figi=['USD000UTSTOM'])
    usdrur = cast_money(u.last_prices[0].price)
    e = client.market_data.get_last_prices(figi=['BBG0013HJJ31'])
    eurrur = cast_money(e.last_prices[0].price)
    list_dict_instruments = list()
    set_colors = set()
    dict_count_instruments = dict()
    instruments_not_once_see = set()
    for pose in portfolio.positions:
        dict_pose = convert_position_to_dict(token, pose, usdrur, eurrur)
        if dict_pose is not None:
            dict_pose['color'] = generate_random_color(set_colors)
            set_name_brief_contry(dict_pose)
            if dict_pose['name'] in dict_count_instruments:
                dict_count_instruments[dict_pose['name']] += dict_pose['quantity']
                instruments_not_once_see.add(dict_pose['name'])
            else:
                dict_count_instruments[dict_pose['name']] = dict_pose['quantity']
            if dict_pose['average_buy_price'] != 0:
                list_dict_instruments.append(dict_pose)
    if len(instruments_not_once_see) != 0:
        for pos in list_dict_instruments:
            if pos['name'] in instruments_not_once_see:
                pos['quantity'] = dict_count_instruments[pos['name']]
                pos['current_buy_price'] = pos['average_buy_price'] + pos['expected_yield'] / pos['quantity']
                pos['cost'] = round(pos['quantity'] * pos['current_buy_price'], 2)
    total_cost = 0
    for pos in list_dict_instruments:
        total_cost += pos['cost']
    for pos in list_dict_instruments:
        pos['portfolio_share'] = round(pos['current_buy_price'] * pos['quantity'] / total_cost * 100, 2)
    return list_dict_instruments


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
#
token = 't.o0Ddqkri-Cf1Xmm6JsYSPdWFrA50JCU0Jy0HJXN_d1ZTAt3TiQopmfyxI3Rbmg8ltHmwx9GXh9Q1fAGBi8Xu7A'
if __name__ == "__main__":
    with Client(token) as client:
        print("2")
        print()
        dic = dict()
        other = list()
        consumer = list()
        it = list()
        green_buildings = list()
        energy = list()
        government = list()
        telecom = list()
        industrials = list()
        health_care = list()
        electrocars = list()
        ecomaterials = list()
        municipal = list()
        financial = list()
        utilities = list()
        green_energy = list()
        real_estate = list()
        materials = list()
        sec = set()
        cur = client.instruments.currencies(instrument_status=2)
        shar = client.instruments.shares(instrument_status=2)
        bon = client.instruments.bonds(instrument_status=2)
        etf = client.instruments.etfs(instrument_status=2)
        fut = client.instruments.futures(instrument_status=2)

        set_counrties = set()
        for s in shar.instruments:
            set_counrties.add(s.country_of_risk_name)
        print(set_counrties)
        print("len set" + str(len(set_counrties)))
        c = 0
        count = list()
        lens = list()
        countries_codes = client.instruments.get_countries().countries
        for country in countries_codes:
            if country.name != '' and (country.name in set_counrties or country.name_brief in set_counrties):
                c += 1
                print(str(c) + country.name + "/" + country.name_brief)
                lens.append(len(country.name_brief))
                count.append(country.name_brief)
        print("MAX")
        print("111111111111111")
        dt = pd.DataFrame()
        dt['co'] = pd.Series(count)
        dt['le'] = pd.Series(lens)
        dt = dt.sort_values('le', ascending=False)
        print(dt.head(45))
        print("111111111111111")

        print(set_counrties)
        print(len(set_counrties))
        print(0)
        mun = list()
        print("VSE VALUTI")
        print(cur)
        print("CLIENT")
        u = client.market_data.get_last_prices(figi=['USD000UTSTOM'])
        usdrur = cast_money(u.last_prices[0].price)
        print(u)
        print("TYPE")
        print(type(u))
        for x in shar.instruments:
            sec.add(x.sector)
            if x.sector == 'municipal':
                mun.append(x.name)
        for x in bon.instruments:
            if x.sector == 'other':
                other.append(x.name)
            if x.sector == 'consumer':
                consumer.append(x.name)
            if x.sector == 'it':
                it.append(x.name)
            if x.sector == 'green_buildings':
                green_buildings.append(x.name)
            if x.sector == 'energy':
                energy.append(x.name)
            if x.sector == 'government':
                government.append(x.name)
            if x.sector == 'telecom':
                telecom.append(x.name)
            if x.sector == 'industrials':
                industrials.append(x.name)
            if x.sector == 'health_care':
                health_care.append(x.name)
            if x.sector == 'electrocars':
                electrocars.append(x.name)
            if x.sector == 'ecomaterials':
                ecomaterials.append(x.name)
            if x.sector == 'municipal':
                municipal.append(x.name)
            if x.sector == 'financial':
                financial.append(x.name)
            if x.sector == 'utilities':
                utilities.append(x.name)
            if x.sector == 'green_energy':
                green_energy.append(x.name)
            if x.sector == 'real_estate':
                real_estate.append(x.name)
            if x.sector == 'materials':
                materials.append(x.name)
            sec.add(x.sector)
            if x.sector == 'municipal':
                mun.append(x.name)
        for x in etf.instruments:
            sec.add(x.sector)
            if x.sector == 'municipal':
                mun.append(x.name)
        for x in fut.instruments:
            sec.add(x.sector)
            if x.sector == 'municipal':
                print(4)
                mun.append(x.name)
        print(len(other))
        print(len(consumer))
        print(len(it))
        print(len(green_buildings))
        print(len(energy))
        print(len(government))
        print(len(telecom))
        print(len(industrials))
        print(len(health_care))
        print(len(electrocars))
        print(len(ecomaterials))
        print(len(municipal))
        print(len(financial))
        print(len(utilities))
        print(len(green_energy))
        print(len(real_estate))
        print(len(materials))
        for x in sec:
            print(x)

        dic['other'] = other
        dic['consumer'] = consumer
        dic['it'] = it
        dic['green_buildings'] = green_buildings
        dic['energy'] = energy
        dic['government'] = government
        dic['telecom'] = telecom
        dic['industrials'] = industrials
        dic['health_care'] = health_care
        dic['electrocars'] = electrocars
        dic['ecomaterials'] = ecomaterials
        dic['municipal'] = municipal
        dic['financial'] = financial
        dic['utilities'] = utilities
        dic['green_energy'] = green_energy
        dic[' real_estate'] = real_estate
        dic['materials'] = materials
        for key in dic.keys():
            print(key)
            print(dic[key])
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
