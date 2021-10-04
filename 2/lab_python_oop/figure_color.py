class figure_color(object):
    """Цвет фигуры"""

    def __init__(self, color = None):
        self._color = color

    def __repr__(self):
        return self.colorproperty

    @property
    def colorproperty(self):
        return self._color

    @colorproperty.setter
    def colorproperty(self, value):
        self._color = value
