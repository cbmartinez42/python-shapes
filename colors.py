import random
import turtle


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "BlanchedAlmond", "PaleTurquoise", "honeydew"]
fillcolors = ["yellow", "blue", "green", "IndianRed", "DeepSkyBlue", "honeydew"]


def pen_color(self):
    return self.color(random.choice(colors))


def fill_color(self):
    return self.fillcolor(random.choice(colors))

