from point import Point
from exceptions import *
from ship import Ship
"""
Класс Grid отвечает за модель игрового поля
"""

class Grid:
    def __init__(self, is_hid=False, size=6):
        self.is_hid = is_hid
        self.size = size

        self.count_hits = []

        self.grid = ["□" * size for _ in range(size)]

        self.occupied_points = []
        self.ships = []

    def __str__(self):
        drawing_grid = ""

        # именуем колонки
        drawing_grid += "  | 1 | 2 | 3 | 4 | 5 | 6 |"  # TODO: переделать на буквы

        # enumerate возвращает кортеж из двух значений (индекс, значение)
        # enumerate(_последовательность_, start = _начальное значение индекса(по умолчанию 0)_)
        for i, row in enumerate(self.grid, 1):
            drawing_grid += f"\n{i} | " + " | ".join(row)+" |"
        return drawing_grid

        # скрывать ли корабли на доске
        if self.hid:
            drawing_grid = drawing_grid.replace("■", "□")
            return drawing_grid
    """
    Метод out_of_grid используется для проверки: точка за пределами?
    """
    def out_of_grid(self, point):
        return not ((0 <= point.x < self.size) and (0 <= point.y < self.size))

    """
    Метод contour используется для определения точек (клеток), на которые уже нельзя размещать судна
    """
    def contour(self, ship, verb=False):

        """
        near - список сдвигов
        | 1 |    2    |    3   |    4    | 5 | 6 |
      1 | □ | (-1,-1) | (0,-1) |  (-1,1) | □ | □ |
      2 | □ |  (0,-1) |    ■   |  (0, 1) | □ | □ | # (0,0) - сама точка
      3 | □ |  (1,-1) | (0, 1) |  (1, 1) | □ | □ |
      4 | □ |    □    |    □   |    □    | □ | □ |
      5 | □ |    □    |    □   |    □    | □ | □ |
      6 | □ |    □    |    □   |    □    | □ | □ |
        """
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for d in ship.points:
            for dx, dy in near:
                cursor = Point(d.x + dx, d.y + dy)
                print(cursor.x, cursor.y)
                self.grid[cursor.x][cursor.y] = "+"
                # if not (self.out(cursor)) and cursor not in self.occupied_points:
                #     if verb:
                #         self.field[cursor.x][cursor.y] = "."
                #     self.busy.append(cursor)
b = Grid()
b.contour(Ship((2, 2), "вертикально", 1))
print(b)