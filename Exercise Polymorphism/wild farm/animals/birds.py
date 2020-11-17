from project.animals.animal import Bird
from typing import List


class Owl(Bird):
    type_of_food: List[str] = ["Meat"]
    gained_weight: float = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):

    type_of_food: List[str] = ["Meat", "Vegetable", "Fruit", "Seed"]
    gained_weight: float = 0.35

    def make_sound(self):
        return "Cluck"



