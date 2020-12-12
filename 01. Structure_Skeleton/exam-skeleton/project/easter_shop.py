from factory.chocolate_factory import ChocolateFactory
from factory.egg_factory import EggFactory
from factory.paint_factory import PaintFactory


class EasterShop:
    name: str
    chocolate_factory: ChocolateFactory
    egg_factory: EggFactory
    paint_factory: PaintFactory
    storage: dict

    def __init__(self):
        pass

    def add_chocolate_ingredient(self, type:str, quantity: str):
        pass

    def add_egg_ingredient(self, type: str, quantity: int):
        pass

    def add_paint_ingredient(self, type: str, quantity: int):
        pass

    def make_chocolate(self, recipe: str):
        pass

    def paint_egg(self, color: str, egg_type: str):
        pass

    def __repr__(self):
        pass
