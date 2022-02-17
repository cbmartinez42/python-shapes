from turtle import *
from colors import random_color


def spirograph(self):
    """Accepts turtle object as argument """
    self.speed('fastest')
    for _ in range(300):
        t_color = random_color()
        f_color = random_color()
        self.color(t_color)
        self.fillcolor(f_color)
        self.begin_fill()
        self.circle(100)
        self.end_fill()
        new_heading = self.heading() + 5
        self.setheading(new_heading)