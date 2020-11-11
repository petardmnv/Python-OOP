from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        c_room = self._find_current_room(room_number)
        res = c_room.take_room(people)
        if res is None:
            self.guests += people
        return res

    def free_room(self, room_number: int):
        c_room = self._find_current_room(room_number)
        res = c_room.free_room()
        if res is None:
            self.guests -= c_room.guests
        return res

    def print_status(self):
        f_rooms = [r.number for r in self.rooms if not r.is_taken]
        t_rooms = [r.number for r in self.rooms if r.is_taken]
        print(f"Hotel {self.name} has {self.guests} total guests")
        res1 = ", ".join(map(str, f_rooms))
        res2 = ", ".join(map(str, t_rooms))
        print(f"Free rooms: {res1}")
        print(f"Taken rooms: {res2}")

    def _find_current_room(self, number: int):
        for r in self.rooms:
            if r.number == number:
                return r


hotel = Hotel.from_stars(5)

first_room = Room(1, 3)

second_room = Room(2, 2)

third_room = Room(3, 1)

hotel.add_room(first_room)

hotel.add_room(second_room)

hotel.add_room(third_room)

hotel.take_room(1, 4)

hotel.take_room(1, 2)

hotel.take_room(3, 1)

hotel.take_room(3, 1)

hotel.print_status()