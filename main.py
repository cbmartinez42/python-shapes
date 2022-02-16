from turtle import *
from walk_polygon import polygon
from walk_random import random


def init():
    timmy = Turtle()
    choice = input("Hello. My name is Timmy the Turtle. I can do fun things! Would you like to see me draw a polygon, "
                   "or should I just take a stroll? ('p' or 's') ")
    if choice == "p":
        polygon(timmy)
    elif choice == "s":
        random(timmy)
    else:
        print("Dude. I said 'p' or 's'. Try again.")
        init()


init()

# def draw_shape(num_sides):
#     """Accepts int of degrees for angle to draw shape"""
#     angle = (360 / num_sides)
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)






screen = Screen()
screen.exitonclick()
