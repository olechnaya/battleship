from .point import Point
"""
Класс Ship отвечает за модель судна (корабля) в игре
"""
class Ship:
    def __init__(self, stem_point, position, length):
        # нос судна
        self.stem_point = stem_point
        self.position = position
        self.length = length
        self.lives = length
    """
    
    """
    @property
    def points(self):
        list_points = []

        for i in range(self.length):
            # координаты носа судна
            coord_x = self.stem_point.x
            coord_y = self.stem_point.y

            if self.position == "вертикально":
                coord_x += i
            elif self.position == "горизонтально":
                coord_y += i

            list_points.append(Point(coord_x, coord_y))

        # НЕ ЗАБЫВАЙ ВОЗВРАТ РЕЗУЛЬТАТА ИЗ МЕТОДА
        return list_points
    """
    Метод is_hit используется для определения попадания в судно
    """
    def is_hit(self, shot):
        return shot in self.points
