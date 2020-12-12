from factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes: dict = {}
        self.products: dict = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def add_recipe(self, recipe_name: str, recipe: dict):
        if recipe_name not in self.recipes.keys():
            self.recipes[recipe_name] = {}
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        pass
