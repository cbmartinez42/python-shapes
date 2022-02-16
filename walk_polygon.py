from colors import pen_color


def polygon(self):
    def draw_shape(num_sides):
        """Accepts int of degrees for angle to draw shape"""
        angle = (360 / num_sides)
        for _ in range(num_sides):
            self.forward(100)
            self.right(angle)
    
    for shape_side_n in range(3, 11):
        pen_color(self)
        draw_shape(shape_side_n)
