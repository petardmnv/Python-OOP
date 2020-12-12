import unittest

from project.appliances.fridge import Fridge
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class RoomTests(unittest.TestCase):
    def setUp(self) -> None:
        self.room = Room("Damianov", 1200, 3)

    def test_init(self):
        self.assertEqual(self.room.family_name, "Damianov")
        self.assertEqual(self.room.budget, 1200)
        self.assertEqual(self.room.members_count, 3)
        self.assertEqual(self.room.children, [])
        self.assertEqual(self.room.expenses, 0)

    def check_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -1
            self.assertEqual("Expenses cannot be negative", ex.exception)


if __name__ == '__main__':
    unittest.main()
