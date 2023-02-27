class Grid:
    def __init__(self, is_hid=False, size=6):
        self.is_hid = is_hid
        self.size = size

        self.count_hits = []

        self.grid = ["□ " * self.size for _ in range(self.size)]

        self.occupied_points = []
        self.ships = []

    def __str__(self):
        drawing_grid = ""

        # именуем колонки
        drawing_grid += "  | 1 | 2 | 3 | 4 | 5 | 6 |"

        # enumerate возвращает кортеж из двух значений (индекс, значение)
        # enumerate(_последовательность_, start = _начальное значение индекса(по умолчанию 0)_)
        for i, row in enumerate(self.grid, 1):
            drawing_grid += f"\n{i} | " + " | ".join(row) + " |"
        return drawing_grid

        if self.hid:
            drawing_grid = drawing_grid.replace("■", "□")
            return drawing_grid

test = Grid()
print(test)
