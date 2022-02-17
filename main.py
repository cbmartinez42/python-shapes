import turtle as t
from walk_polygon import polygon
from walk_random import random
from walk_spirograph import spirograph


def init():
    timmy = t.Turtle()
    t.colormode(255)
    timmy.shape('turtle')
    choice = input("Hello. My name is Timmy the Turtle. I can do fun things! Would you like to see me draw a (p)olygon, "
                   "a (s)pirograph, or should I just take a (w)alk? ('p', 's' or 'w') ")
    if choice == "p":
        polygon(timmy)
    elif choice == "s":
        spirograph(timmy)
    elif choice == "w":
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






screen = t.Screen()
sizescreen = screen.screensize()
print("screensize: ", sizescreen)
screen.exitonclick()
