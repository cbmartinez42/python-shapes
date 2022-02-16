import random
import turtle


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue"]
fillcolors = ["yellow", "blue", "green"]


def pen_color(self):
    return self.color(random.choice(colors))


def fill_color(self):
    return self.fillcolor(random.choice(colors))

