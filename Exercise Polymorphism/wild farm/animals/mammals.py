from project.animals.animal import Mammal
from typing import List


class Mouse(Mammal):
    type_of_food: List[str] = ["Vegetable", "Fruit"]
    gained_weight: float = 0.1

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    type_of_food: List[str] = ["Meat"]
    gained_weight: float = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    type_of_food: List[str] = ["Meat", "Vegetable"]
    gained_weight: float = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    type_of_food: List[str] = ["Meat"]
    gained_weight: float = 1.00

    def make_sound(self):
        return "ROAR!!!"