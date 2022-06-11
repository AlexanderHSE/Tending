import random
import pandas as pd
from bs4 import BeautifulSoup


def generate_random_color(set_colors: set()):
    while True:
        color = "#"
        for i in range(6):
            color = color + random.choice('0123456789ABCDEF')
        if color not in set_colors and color != '#2A2A2C':
            set_colors.add(color)
            return color


def generate_color_column(df):
    len_col = len(df.index)
    set_colors = set()
    for color_index in range(len_col):

        generate_random_color(set_colors)
    color_column = pd.Series(list(set_colors))
    print("generate_color_column")
    print(list(set_colors))
    df['color'] = color_column


def write_html(graph, file_name):
    graph_html = graph.to_html(include_plotlyjs='cdn')
    print(type(graph_html))
    print(graph_html)
    style = " <style> body{ margin: 0; background-color: #2A2A2C;} </style>"
    with open(file_name, 'w+') as file_graph_html:
        index = graph_html.find('<head><meta charset="utf-8" />')
        new_html = graph_html[:index] + style + graph_html[index:]
        file_graph_html.write(new_html)

        # contents = file_graph_html.read()
        # print(contents)
        # soup = BeautifulSoup(graph_html, 'html.parser')
        # print('soup')
        # print(soup)
        # delete_obj = soup.findAll("div", class_="modebar modebar--hover ease-bg")
        # print("del")
        # print(delete_obj)
    #  delete_obj.decompose()


def check_dt_is_empty(dt):
    return len(dt.index) == 0
