import random
from turtle import *


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "blue", "PaleTurquoise", "green"]
fill_colors = ["yellow", "blue", "green", "IndianRed", "DeepSkyBlue", "honeydew"]


def pen_color():
    step_color = random.choice(colors)
    return step_color


def fill_color():
    shape_color = random.choice(fill_colors)
    return shape_color

