class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people: int):
        if self.is_taken or people > self.capacity:
            return f"Room number {self.number} cannot be taken"
        self.is_taken = True
        self.guests += people
        return None

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
            return None
        return f"Room number {self.number} is not taken"

