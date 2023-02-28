"""

"""
class GameExceptions(Exception):
    pass

class  OutOfGridExceptions(GameExceptions):
    def __str__(self):
        return "Вы стреляете за границу поля. Попробуйте ещё."

class PointIsUsedException(GameExceptions):
    def __str__(self):
        return "Вы уже стреляли в эту клетку. Попробуйте ещё."
class ShipWrongPlacement(GameExceptions):
    pass