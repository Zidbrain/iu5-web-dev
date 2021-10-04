from lab_python_oop.rect import rect

class square(rect):
    
    FIGURE_TYPE = 'Квадрат'

    def __init__(self, length: float, color):
        super().__init__(length, length, color)
        self.length = length

    def __repr__(self):
        return '{}, длина стороны: {}, цвет: {}, площадь:{}'.format(self.get_figure_type(), self.length, self.color, self.area())