from point import Point

class Ship:
    def __init__(self, bow, position, length):
        self.bow = bow
        self.position = position
        self.length = length
        self.lives = length

    @property
    def ship_points(self):
        list_points = []

        for i in range(self.length):
            cur_x = self.bow[0]
            cur_y = self.bow[1]

            if self.position == "вертикально":
                cur_x += i
            elif self.position == "горизонтально":
                cur_y += i

            list_points.append(Point(cur_x, cur_y))

        # НЕ ЗАБЫВАЙ ГРЕБАНЫЙ ВОЗВРАТ РЕЗУЛЬТАТА ИЗ МЕТОДА
        return list_points

    def is_hit(self, shot):
        # if shot in self.ship_points:
        #     return print("HIT")
        # else:
        #     return print("Мазила")
        return shot in self.ship_points

ship1 = Ship((1, 1), "вертикально", 4)

ship1.ship_points
print(ship1.is_hit(Point(5, 1)))

