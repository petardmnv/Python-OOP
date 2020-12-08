from cat import Cat
import unittest


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Peho")

    def test_cat_name(self):
        self.assertEqual(self.cat.name, "Peho")

    def cat_size_is_increased_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 3)

    def test_cat_is_fed_after_eat(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cant_eat_after_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_if_cat_cannot_fall_asleep_if_not_fed(self):
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_not_sleepy_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()

