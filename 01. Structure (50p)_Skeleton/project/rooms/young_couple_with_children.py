from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children: Child):
        self.room_cost = 30
        self.appliances = [TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]
        super().__init__(family_name, budget=(salary_one + salary_two), members_count=(2 + len(children)))
        self.children = [c for c in children]
        for _ in range(len(self.children)):
            self.appliances.append(TV())
            self.appliances.append(Fridge())
            self.appliances.append(Laptop())
        self.calculate_expenses(self.appliances, self.children)