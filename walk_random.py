import random as rand
from colors import pen_color
directions = [0, 90, 180, 270]


def random(self):
    """Random walk function with new color every step"""
    timmy = self
    timmy.pensize(10)
    timmy.speed(0)
    for _ in range(1000):
        timmy.forward(10)
        turtle_color = pen_color()
        turtle_heading = rand.choice(directions)
        timmy.setheading(turtle_heading)
        timmy.color(turtle_color)
    
    
#     self.pensize(width=5)
#     while True:
#         step = random.choice(directions)
#         if step == "l":
#             self.left()
#             self.forward(100)
