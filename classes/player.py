from random import randint

from exceptions import *
from point import Point
"""
Класс Player отвечает за модель игрока
"""
class Player:
    def __init__(self, grid, opponent):
        self.grid = grid
        self.opponent = opponent

    def ask(self):
        # метод должен быть реализован у потомков класса Player
        raise NotImplementedError()

    def call_out(self):
        while True:
            try:
                target_cell = self.ask()
                repeat = self.opponent.shot(target_cell)
                return repeat
            except GameExceptions as e:
                print(e)

class AI(Player):
    def ask(self):
        point = Point(randint(0,5),randint(0,5))
        print(f"Ход компьютера: {point.x + 1} {point.y + 1}")
        return point

class User(Player):

    def ask(self):
        pass
