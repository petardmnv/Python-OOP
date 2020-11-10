from collections import defaultdict


class Store:
    def __init__(self, naem: str, type:str, capasity: int):
        self.name = naem
        self.type = type
        self.capacity = capasity
        self.items = defaultdict(int)

    @classmethod
    def from_size (cls, name:str, type: str, size:int):
        capacity: int  = size // 2
        return cls(name, type, capacity)

    def add_item(self, item_name:str):
        p_count = sum(self.items.values())
        if p_count < self.capacity:
            self.items[item_name] += 1
            return f"{item_name} added to the store"
        else:
            return "Not enough capacity in the store"

    def remove_item(self, item_name:str, amount:int):
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            return f"{amount} {item_name} removed from the store"
        else:
            return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


first_store = Store("First store", "Fruit and Veg", 20)

second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)

print(second_store)

print(first_store.add_item("potato"))

print(second_store.add_item("jeans"))

print(first_store.remove_item("tomatoes", 1))

print(second_store.remove_item("jeans", 1))

