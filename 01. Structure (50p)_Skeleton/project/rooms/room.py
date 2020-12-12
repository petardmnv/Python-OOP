from project.people.child import Child
from typing import List


class Room:
    children: List[Child]
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, x):
        if x < 0:
            raise ValueError("Expenses cannot be negative")
        else:
            self._expenses = x

    def calculate_expenses(self, *args):
        for a in args:
            for b in a:
                self.expenses += b.cost
