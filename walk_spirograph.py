from turtle import *
from colors import random_color

def spirograph(self):
    for _ in range(300):
        t_color = random_color()
        self.color(t_color)
        self.circle(100)
        new_heading = self.heading() + 5
        self.setheading(new_heading)