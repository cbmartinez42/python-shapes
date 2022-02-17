import random
import turtle as t


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "blue", "PaleTurquoise", "green"]
fill_colors = ["yellow", "blue", "green", "IndianRed", "DeepSkyBlue", "honeydew"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return_color = (r, g, b)
    return return_color


def pen_color():
    step_color = random.choice(colors)
    return step_color


def fill_color():
    shape_color = random.choice(fill_colors)
    return shape_color

