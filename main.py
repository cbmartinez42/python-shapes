from turtle import *
import random

timmy = Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue"]


def draw_shape(num_sides):
    """Accepts int of degrees for angle to draw shape"""
    angle = (360 / num_sides)
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)
    
    
for shape_side_n in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)






screen = Screen()
screen.exitonclick()
