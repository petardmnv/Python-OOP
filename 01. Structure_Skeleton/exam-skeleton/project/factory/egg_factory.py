from factory.factory import Factory


class EggFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)

    @property
    def products(self):
        return self.ingredients

    @products.setter
    def products(self, d: dict):
        self.products = d

    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        pass

