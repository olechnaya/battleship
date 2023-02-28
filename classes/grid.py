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

        self.grid = [["□"] * size for _ in range(size)]

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

        for point in ship.points:
            for point_x, point_y in near:
                cursor = Point(point.x + point_x, point.y + point_y)
                #self.grid[cursor.x][cursor.y] = "+"
                # если точка в пределах поля и не в списке занятых точек
                if not (self.out_of_grid(cursor)) and cursor not in self.occupied_points:

                    # verb - нужно ли ставить точки вокруг суден или нет. Во время расстановки False. Во время игры True.
                    if verb:
                        # заменяем символ свободной ячейки на занятую
                        self.grid[cursor.x][cursor.y] = "."
                    # добавляем в список занятых точек
                    self.occupied_points.append(cursor)

    """
    Метод add_ship
    """
    def add_ship(self, ship):
        for point in ship.points:
            # проверка, что каждая точка судна не выходит за границы и не занята
            if self.out_of_grid(point) or point in self.occupied_points:
                raise ShipWrongPlacement()
        # проходим по координатам поля, где стоит судно
        for point in ship.points:
            # заменяем символ свободной ячейки на занятую
            self.grid[point.x][point.y] = "■"
            # добавляем точку в список занятых (точки судна + соседние с ним точки)
            self.occupied_points.append(point)

        self.ships.append(ship)
        self.contour(ship)
    """
    Метод shot используется для моделирования хода игрока (выстрела)
    """
    def shot(self, point):
        # обработка ошибки выстрела за пределы игрового поля
        if self.out_of_grid(point):
            raise OutOfGridExceptions()
        # обработка ошибки выстрела по уже отстреленной ячейке
        if point in self.occupied_points:
            raise PointIsUsedException()

        self.occupied_points.append(point)

        for ship in self.ships:
            if ship.is_hit(point):
                ship.lives -= 1
                self.grid[point.x][point.y] = "x"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.grid[point.x][point.y] = "."
        print("Мимо!")
        return False

    def begin(self):
        self.occupied_points = []

b = Grid()
b.add_ship(Ship(Point(2, 2), "горизонтально", 3))
b.add_ship(Ship(Point(1, 1), "горизонтально", 1))
print(b)