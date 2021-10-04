from abc import ABC
from abc import abstractmethod

class figure(ABC):
    """
    Класс фигуры
    """
    FIGURE_TYPE: str = None

    @abstractmethod
    def area(self) -> float:
        """Вычисление площади фигуры"""
        pass

    @classmethod
    def get_figure_type(cls) -> str:
        return cls.FIGURE_TYPE