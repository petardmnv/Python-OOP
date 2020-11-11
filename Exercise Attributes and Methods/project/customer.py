from typing import List
from project.dvd import DVD


class Customer:
    rented_dvds = List[DVD]

    def __init__(self, name: str, age: int, id: int):
        self.id = id
        self.name = name
        self.age = age
        self.rented_dvds = []

    def __repr__(self):
        names = [d.name for d in self.rented_dvds]
        res = ", ".join(names)
        return f"{id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({res})"