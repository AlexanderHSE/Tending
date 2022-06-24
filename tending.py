from tinkoff.invest import Client, MoneyValue
from tinkoff.invest.schemas import PortfolioResponse, Quotation, PortfolioPosition
from Instr import Instr
from help_func import generate_random_color

#    t.o0Ddqkri-Cf1Xmm6JsYSPdWFrA50JCU0Jy0HJXN_d1ZTAt3TiQopmfyxI3Rbmg8ltHmwx9GXh9Q1fAGBi8Xu7A
#   t.r3D-SJY-s37p965fw1Co_UvACNdtrcxUW7rq_xIU4GP5d2Ni2XSLB3NlrHSx21ck6eLoenkmV0LXiIx0_uldUw
#   t.6l6UT2g6HYDf_PNb8BIO4PuWeGajBgfQGPHgtTi-bEIgfiSdTKsyVuN17Yv0T0Umxw-TzPnrVTUIe8g3LkL8bg
#   t.NGGbyn3u0IqCmwDZmjD_uOOjoC1bY3iNdhENnfRO0qGF9O9t0hKRoZbl2Hb-os1gnNwVZ8aZxfgnr4OpC82dlA
dict_sector = dict(government="Государтсвенные бумаги", energy="Энергетика", ecomaterials="Промышленность",
                   green_energy="Зелёная энергетика", financial="Финансы", utilities="Коммунальные услуги",
                   materials="Материалы", green_buildings="Промышленность", municipal="Муниципальные бумаги",
                   other="Другое", industrials="Промышленность", it="IT",
                   health_care="Здравоохранение", telecom="Услуги связи", consumer="Потребительский сектор",
                   real_estate="Недвижимость", electrocars="Промышленность", currency="Валюта", etf="ETF",
                   bond="Облигация", )

dict_instrument_type = dict(share="Акция", bond="Облигация", etf="Фонд", currency="Валюта", future="Фьючерс")

dict_focus_type = dict(equity="Акции", fixed_income="Облигация", mixed_allocation="Смешанные",
                       money_market="Денежный рынок", real_estate="Недвижимость",
                       commodity="Товары", specialty="Специальный", private_equity="PE-фонд",
                       alternative_investment="Альтернативные инвестиции")

dict_countries_correct_names = {'Германия': "Германию", 'Греция': "Грецию", 'Нидерланды': "Нидерланды", 'Швейцария': "Швейцарию",
                        'Дания': "Данию", 'Италия': "Италию", 'Швеция': "Швецию", 'Испания': "Испанию", 'Австрия': "Австрию",
                        'Виргинские Острова, Британские': "Британские Виргинские Острова", 'Камерун': "Камерун",
                        'Гонконг': "Гонконг", 'Казахстан': "Казахстан", 'Финляндия': "Финляндию", 'Словения': "Словению",
                        'Сингапур': "Сингапур", 'Маврикий': "Маврикий", 'Монако': "Монако", 'Маршалловы Острова': "Маршалловы Острова",
                        'Филиппины': "Филиппины", 'Польша': "Польшу", 'Португалия': "Португалию",  'Норвегия': "Норвегию",
                        'Франция': "Францию", 'Индонезия': "Индонезию", 'Китай': "Китай", 'Бразилия': "Бразилию",
                        'Бельгия': "Бельгию", 'Люксембург': "Люксембург", 'Израиль': "Израиль", 'Турция': "Турцию",
                        'Таиланд': "Таиланд", 'Индия': "Индию", 'Корея, Республика': "Республику Корея", 'Чили': "Чили",
                        'Мексика': "Мексику", 'Аргентина': "Аргентину", 'Перу': "Перу", 'Соединенные Штаты': "Соединенные Штаты",
                        'Колумбия': "Колумбию", 'Южная Африка': "Южную Африку", 'Россия': "Россию", 'Уругвай': "Уругвай",
                        'Соединенное Королевство': "Соединенное Королевство"}

dict_sectors_correct_names = {"Государтсвенные бумаги": "государтсвенных бумагах", 'Энергетика': "энергетике",
                              'Промышленность': "промышленности", 'Зелёная энергетика': "зелёной энергетике",
                              'Финансы': 'финансах', 'Коммунальные услуги': 'коммунальных услугах',
                              'Материалы': 'материалах', 'Муниципальные бумаги': 'муниципальных бумагах',
                              'Другое': 'другом', 'IT': 'IT', 'Здравоохранение': 'здравоохранении',
                              'Услуги связи': 'услугах связи', 'Потребительский сектор': 'потребительском секторе',
                              'Недвижимость': 'недвижимости', 'Валюта': 'валюте',
                              'ETF': 'ETF', 'Облигация': 'облигациях'}


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
            'focus_type' : ""
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
            r['sector'] = 'ETF'
            r['ticker'] = instr.ticker
            r['focus_type'] = dict_focus_type[instr.focus_type]
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
        if position.instrument_type != 'etf':
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


def choice_parsing():
    print("Выберите способ парсинга")
    print("1. api")
    print("2. Excel")


'''
            t.o0Ddqkri-Cf1Xmm6JsYSPdWFrA50JCU0Jy0HJXN_d1ZTAt3TiQopmfyxI3Rbmg8ltHmwx9GXh9Q1fAGBi8Xu7A
'''
