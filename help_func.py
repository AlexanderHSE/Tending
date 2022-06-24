import random
import pandas as pd
# Словарь HEX-кодов цветов к секторам экономики у Акций
dict_sector_color_not_etfs = {"Государственные бумаги": "#D4CE26", 'Энергетика': "#0B73AD", 'Промышленность': "#42418C",
                              'Зелёная энергетика': "#3A6234", 'Финансы': '#48BB36', 'Коммунальные услуги': '#DBD496',
                              'Материалы': '#387975',
                              'Муниципальные бумаги': '#5B7512', 'Другое': '#190E27', 'IT': '#89C7EA',
                              'Здравоохранение': '#AF2A32', 'Услуги связи': '#532469',
                              'Потребительский сектор': '#C58019', 'Недвижимость': '#545659', 'Валюта': '#806B2A',
                              'ETF': '#D736C7', 'Облигация': '#14473B'}
# Словарь HEX-кодов цветов к секторам Фондов
dict_sector_color_etfs = {"Акции": "#C58019", 'Облигации': "#D4CE26", 'Смешанные': "#D736C7",
                          'Денежный рынок': "#48BB36", 'Недвижимость': '#545659', 'Товары': '#0B73AD',
                          'Специальный': '#AF2A32', 'PE-фонд': '#DBD496', 'Альтернативные инвестиции': '#532469'}


# Проверка - является ли число целым
def check_float(number):
    return int(number) - number == 0


# Генерация случайных цветов
def generate_random_color(set_colors):
    while True:
        color = "#"
        for i in range(6):
            color = color + random.choice('0123456789ABCDEF')
        if color not in set_colors and color != '#2A2A2C':
            set_colors.add(color)
            return color


# Генерация цветов для активов
def generate_color_column(df):
    len_col = len(df.index)
    set_colors = set()
    for color_index in range(len_col):
        generate_random_color(set_colors)
    color_column = pd.Series(list(set_colors))
    df['color'] = color_column


# Генерация цветов для секторов - акции
def generate_color_by_sectors_column_not_etfs(df):
    sectors_sequence = df['sector'].tolist()
    secotrs_colors = list()
    for sector in sectors_sequence:
        secotrs_colors.append(dict_sector_color_not_etfs[sector])
    df['color'] = pd.Series(secotrs_colors)


# Генерация цветов для секторов - Фонды
def generate_color_by_sectors_column_etfs(df):
    sectors_sequence = df['sector'].tolist()
    secotrs_colors = list()
    for sector in sectors_sequence:
        secotrs_colors.append(dict_sector_color_etfs[sector])
    df['color'] = pd.Series(secotrs_colors)


# Доля активов
def add_column_percantages(df):
    total_cost_all = df['cost'].sum()
    total_cost_by_condition = df['cost'].tolist()
    total_cost_percentage = list()
    for total_cost_by_condition_one_type in total_cost_by_condition:
        total_cost_percentage.append(round((total_cost_by_condition_one_type / total_cost_all * 100), 2))
    df['total_cost_percentage'] = pd.Series(total_cost_percentage)


# Запись диаграммы в HTML-файл
def write_html(graph, file_name):
    graph_html = graph.to_html(include_plotlyjs='cdn')
    style = " <style> body{ margin: 0; background-color: #2A2A2C;} </style>"
    with open(file_name, 'w+') as file_graph_html:
        index = graph_html.find('<head><meta charset="utf-8" />')
        new_html = graph_html[:index] + style + graph_html[index:]
        file_graph_html.write(new_html)


# Проверка того, что данные присутствуют
def check_dt_is_empty(dt):
    return len(dt.index) == 0
