from math import pi
from lab_python_oop.figure import figure
from lab_python_oop.figure_color import figure_color

class circle(figure):

    FIGURE_TYPE = 'Круг'

    def __init__(self, radius: float, color):
        self.radius = radius
        self.color = figure_color(color)

    def area(self) -> float:
        return pi * self.radius**2

    def __repr__(self):
        return '{}, радиус: {}, цвет:{}, площадь:{}'.format(self.get_figure_type(), self.radius, self.color, self.area())