from restaurant.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    COFFEE_MILLILITERS = 50
    COFFEE_PRICE = 3.5
    __caffeine: float

    def __init__(self, name, caffeine):
        super().__init__(name, self.__class__.COFFEE_PRICE, self.__class__.COFFEE_MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

