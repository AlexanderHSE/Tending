from tinkoff.invest import Client
from tinkoff.invest.schemas import PortfolioResponse, PortfolioPosition
from Instr import Instr
from help_func import generate_random_color

# Словарь русский названих секторов из библиотеки Tinkoff Invest
dict_sector = dict(government="Государтсвенные бумаги", energy="Энергетика", ecomaterials="Промышленность",
                   green_energy="Зелёная энергетика", financial="Финансы", utilities="Коммунальные услуги",
                   materials="Материалы", green_buildings="Промышленность", municipal="Муниципальные бумаги",
                   other="Другое", industrials="Промышленность", it="IT",
                   health_care="Здравоохранение", telecom="Услуги связи", consumer="Потребительский сектор",
                   real_estate="Недвижимость", electrocars="Промышленность", currency="Валюта", etf="ETF",
                   bond="Облигация", )

# Словарь русских названий типов инструментов из библиотеки Tinkoff Invest
dict_instrument_type = dict(share="Акция", bond="Облигация", etf="Фонд", currency="Валюта", future="Фьючерс")

# Словарь русских названий секторов фондов из библиотеки Tinkoff Invest
dict_focus_type = dict(equity="Акции", fixed_income="Облигация", mixed_allocation="Смешанные",
                       money_market="Денежный рынок", real_estate="Недвижимость",
                       commodity="Товары", specialty="Специальный", private_equity="PE-фонд",
                       alternative_investment="Альтернативные инвестиции")


# Перевод числого представления значения из библиотеки Tinkoff Invest в числовое значение Python
def cast_yield(quotation):
    return quotation.units + quotation.nano / 1e9


# Получение количества инвестированных денег в рублях
def get_invested_money(total_yield_percentage: float, total_cost: float):
    total_cost_percentage = 100 + total_yield_percentage
    return total_cost / total_cost_percentage * 100


# Получение прибыли/убыли портфеля в рублях
def get_total_profit(total_yield_percentage: float, total_cost: float):
    invested_money = get_invested_money(total_yield_percentage, total_cost)
    return round(total_cost - invested_money, 2)


# Получение стоимости портфеля в рублях
def get_total_cost_portfolio(df, portfolio: PortfolioResponse):
    # Если в портфеле нет активов, то его стоимасть равна нулю
    if df.empty:
        return 0
    # Если в портфеле есть активы, считаем стоимость портфеля
    total_amount_shares = cast_yield(portfolio.total_amount_shares)
    total_amount_bonds = cast_yield(portfolio.total_amount_bonds)
    total_amount_etf = cast_yield(portfolio.total_amount_etf)
    total_amount_currencies = df[df['instrument_type'] == 'Валюта'].agg('sum')['cost']
    total_amount_futures = cast_yield(portfolio.total_amount_futures)
    return round(total_amount_shares + total_amount_bonds + total_amount_etf +
                 total_amount_currencies + total_amount_futures, 2)


# Получение данных об инструменте
def get_instrument(token, position):
    ins = Instr(token, position.figi, position.instrument_type)
    return ins.instr


# Привидение данных иснтрумента в словарь
def convert_position_to_dict(token, position: PortfolioPosition, usdrur, eurrur):
    instr = get_instrument(token, position)
    #  Если есть данные по инструменту, конвертируем их в словарь
    if instr is not None:
        # Получение общей информации по активу
        r = {
            'name': instr.name,
            'ticker': "",
            'country': instr.country_of_risk_name,
            'sector': "",
            'quantity': cast_yield(position.quantity),
            'expected_yield': cast_yield(position.expected_yield),
            'instrument_type': position.instrument_type,
            'average_buy_price': cast_yield(position.average_position_price),
            'current_buy_price': cast_yield(position.average_position_price) + cast_yield(
                position.expected_yield) / cast_yield(position.quantity),
            'currency': position.average_position_price.currency,
            'nkd': cast_yield(position.current_nkd),
            'focus_type': ""
        }
        # Если количество активов - целое число, привидение значения к целому типу
        if int(r['quantity']) - r['quantity'] == 0:
            r['quantity'] = int(r['quantity'])
        # Добавление секторов экономику активу, являющемуся валютой или облигацией
        if position.instrument_type == 'currency' or position.instrument_type == 'bond':
            r['ticker'] = ""
            if position.instrument_type == 'currency':
                r['sector'] = "currency"
            else:
                r['sector'] = "bond"
        # Если актив - фонд, добавление тикера, сектора и специализации фонда.
        elif position.instrument_type == 'etf':
            r['sector'] = 'ETF'
            r['ticker'] = instr.ticker
            r['focus_type'] = dict_focus_type[instr.focus_type]
        # Если актив - акция, добавление сектра и тикера
        else:
            r['ticker'] = instr.ticker
            r['sector'] = instr.sector
        # Если актив торгуют в иностранной валюте, то привидение числовых значений в рублевое значение,
        # фиксация этого факта
        if r['currency'] != 'rub':
            # Если актив торгуют в Долларах США
            if r['currency'] == 'usd':
                r['current_buy_price'] *= usdrur
                r['expected_yield'] *= usdrur
                r['average_buy_price'] *= usdrur
                r['nkd'] *= usdrur
                r['original_currency'] = 'Доллар США'
            # Если актив торгуют в ЕВРО
            elif r['currency'] == 'eur':
                r['current_buy_price'] *= eurrur
                r['expected_yield'] *= eurrur
                r['average_buy_price'] *= eurrur
                r['original_currency'] = 'Евро'
                r['nkd'] *= eurrur
        # Если актив торгуется в рублях, фиксация этого факта
        else:
            r['original_currency'] = 'Рубль'
        # Если актив не заморожен, вычисление прибыли актива в процентах
        if r['average_buy_price'] != 0:
            r['expected_yield_percentage'] = (r['current_buy_price'] - r['average_buy_price']) / r[
                'average_buy_price'] * 100
        # Если актив заморожен, то убыток составляет 100 процентов
        else:
            r['expected_yield_percentage'] = -100
        r['currency'] = '₽'
        # Переименование английских значений в русские
        if position.instrument_type != 'etf':
            r['sector'] = dict_sector[r['sector']]
        r['instrument_type'] = dict_instrument_type[r['instrument_type']]
        # Вычисление стоимости актива
        r['cost'] = round(r['quantity'] * r['current_buy_price'], 2)
        return r
    # Если нет данных по активу, возвращаем ничего
    return None


# Переименование значения названия страны актива в сокращенное русское название страны
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


# Получение списка стран, активы которых есть в Тинькофф Инвестициях
def set_counrties(token):
    with Client(token) as client:
        global countries_codes
        countries_codes = client.instruments.get_countries().countries


# Получение списка активов портфеля
def get_set_positions(token, client, portfolio):
    # Получение списка стран, активы которых есть в Тинькофф Инвестициях
    set_counrties(token)
    # Получение курса Доллара США и ЕВРО
    u = client.market_data.get_last_prices(figi=['USD000UTSTOM'])
    usdrur = cast_yield(u.last_prices[0].price)
    e = client.market_data.get_last_prices(figi=['BBG0013HJJ31'])
    eurrur = cast_yield(e.last_prices[0].price)
    list_dict_instruments = list()
    set_colors = set()
    dict_count_instruments = dict()
    instruments_not_once_see = set()
    #  Конвертирование данных актива в словарь и добавление его в список активов
    for pose in portfolio.positions:
        dict_pose = convert_position_to_dict(token, pose, usdrur, eurrur)
        if dict_pose is not None:
            dict_pose['color'] = generate_random_color(set_colors)
            set_name_brief_contry(dict_pose)
            # Если актив заморожен, добавить его в список замороженных активов.
            if dict_pose['name'] in dict_count_instruments:
                dict_count_instruments[dict_pose['name']] = dict_pose['quantity']
                dict_count_instruments[dict_pose['name']] += dict_pose['quantity']
                instruments_not_once_see.add(dict_pose['name'])
            else:
                dict_count_instruments[dict_pose['name']] = dict_pose['quantity']
            if dict_pose['average_buy_price'] != 0:
                list_dict_instruments.append(dict_pose)
    # Если есть активы, часть которых заморожена брокером, добавить данные замороженных активов к незамороженным
    if len(instruments_not_once_see) != 0:
        for pos in list_dict_instruments:
            if pos['name'] in instruments_not_once_see:
                pos['quantity'] = dict_count_instruments[pos['name']]
                pos['current_buy_price'] = pos['average_buy_price'] + pos['expected_yield'] / pos['quantity']
                pos['cost'] = round(pos['quantity'] * pos['current_buy_price'], 2)
    total_cost = 0
    # Получение значения стоимости портфеля в рублях.
    for pos in list_dict_instruments:
        total_cost += pos['cost']
    # Получение значения доли актива от всего портфеля в процентах.
    for pos in list_dict_instruments:
        pos['portfolio_share'] = round(pos['current_buy_price'] * pos['quantity'] / total_cost * 100, 2)
    return list_dict_instruments
