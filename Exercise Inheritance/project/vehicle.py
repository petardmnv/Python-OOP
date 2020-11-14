from typing import ClassVar


class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: ClassVar[float] = 1.25
    fuel_consumption: float
    fuel: float
    horse_power: int

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.__class__.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        if self.fuel < kilometers * self.fuel_consumption:
            return
        self.fuel -= kilometers * self.fuel_consumption
