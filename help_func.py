import random


def generate_random_color(set_colors: set()):
    while True:
        color = "#"
        for i in range(6):
            color = color + random.choice('0123456789ABCDEF')
        if color not in set_colors:
            set_colors.add(color)
            return color
