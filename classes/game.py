from random import randint, choice

from point import Point
from exceptions import *
from ship import Ship
from grid import Grid
from player import User, AI

"""
Класс Game
"""


class Game:
    def __init__(self, size = 6):
        self.size = size
        self.list_of_ships = [3, 2, 2, 1, 1, 1, 1]
        self.list_of_positions = ["горизонтально", "вертикально"]
        user_grid = self.random_grid()
        ai_grid = self.random_grid()
        ai_grid_hidden = True

        self.ai = AI(ai_grid, user_grid)
        self.user = User(user_grid, ai_grid)

    def try_grid(self):
        grid = Grid(size = self.size)
        attempts = 0

        #в бесконечном циекле размещаем каждый корабль из списка
        for ship_elem in self.list_of_ships:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Point(randint(0, self.size), randint(0, self.size)), choice(self.list_of_positions), ship_elem)
                try:
                    grid.add_ship(ship)
                    break
                except ShipWrongPlacement:
                    pass
        grid.begin()
        return grid

    def random_grid(self):
        grid = None
        while grid is None:
            grid = self.try_grid()
        return grid

    def greet(self):
        print("-------------------")
        print("  Приветсвуем вас  ")
        print("      в игре       ")
        print("    морской бой    ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def print_grids(self):
        print("-" * 20)
        print("Доска пользователя:")
        print(self.user.grid)
        print("-" * 20)
        print("Доска компьютера:")
        print(self.ai.grid)
        print("-" * 20)

    def loop(self):
        num = 0

        while True:
            self.print_grids()
            if num % 2 == 0:
                print("Ходит пользователь!")
                repeat = self.user.call_out()
            else:
                print("Ходит компьютер!")
                repeat = self.ai.call_out()
            if repeat:
                num -= 1

            if self.ai.grid.fleet_size:
                self.print_grids()
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.user.grid.fleet_size:
                self.print_grids()
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()

g = Game()
g.start()