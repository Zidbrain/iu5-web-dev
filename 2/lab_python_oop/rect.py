from lab_python_oop.figure import figure
from lab_python_oop.figure_color import figure_color

class rect(figure):
    
    FIGURE_TYPE = 'Прямоугольник'

    color: figure_color = None

    def area(self):
        return self.width * self.heigth

    def __init__(self, width: float, heigth: float, color):
        self.width = width
        self.heigth = heigth
        self.color = figure_color()
        self.color.colorproperty = color

    def __repr__(self):
        return '{}, ширина:{}, высота:{}, цвет:{}, площадь:{}'.format(self.get_figure_type(), self.width, self.heigth, self.color, self.area())