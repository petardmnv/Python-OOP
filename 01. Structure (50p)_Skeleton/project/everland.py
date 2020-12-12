from project.rooms.room import Room


class Everland:
    rooms: list

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for r in self.rooms:
            total_consumption += r.expenses * 30
            total_consumption += r.room_cost
        return f"Monthly consumption: {total_consumption: .2f}$."

    def pay(self):
        result = []
        for r in self.rooms:
            if r.budget >= (r.expenses * 30 + r.room_cost):
                r.budget -= (r.expenses * 30 + r.room_cost)
                result.append(f"{r.family_name} paid {(r.expenses * 30 + r.room_cost): .2f}$ and have {r.budget: .2f}$ left.")
            else:
                self.rooms.remove(r)
                result.append(f"{r.family_name} does not have enough budget and must leave the hotel.")

        return '\n'.join(result)

    def status(self):
        result = []
        result.append(f"Total population: {sum(r.members_count for r in self.rooms)}")
        for r in self.rooms:
            print(len(r.children))
            result.append(f"{r.family_name} with {r.members_count} members. Budget: {r.budget: .2f}$, Expenses: {(r.expenses * 30): .2f}$")
            for i in range(len(r.children)):
                result.append(f"--- Child {i + 1} monthly cost: {(r.children[i].cost * 30): .2f}$")
            result.append(f"--- Appliances monthly cost: {(r.expenses * 30): .2f}$")

        return '\n'.join(result)
