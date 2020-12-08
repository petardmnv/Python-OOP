import unittest
from solution import Person


class PersonTests(unittest.TestCase):
    def test_is_person_properly_initiated(self):
        person = Person("Jordan")
        self.assertEqual(person.name, "Jordan")


if __name__ == '__main__':
    unittest.main()