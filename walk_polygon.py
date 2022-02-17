from colors import pen_color, random_color
from turtle import *


def polygon(self):
    def draw_shape(num_sides):
        """Accepts int of degrees for angle to draw shape"""
        begin_fill()
        angle = (360 / num_sides)
        for _ in range(num_sides):
            self.forward(100)
            self.right(angle)
        end_fill()
    
    for shape_side_n in range(3, 11):
        # pen_color()
        t_color = random_color()
        self.color(t_color)
        draw_shape(shape_side_n)
