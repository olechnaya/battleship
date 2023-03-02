"""
Класс Point отвечает за модель точки (клетки) на поле
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    """
    Метод __eq__ используется для сравнения двух объектов класса Point
    """
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    """
    Метод __repr__ для удобства вывода данных объекта класса Point в консоль
    """
    def __repr__(self):
        return f"Point{self.x, self.y}"
