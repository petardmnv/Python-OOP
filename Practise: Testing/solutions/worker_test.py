from worker import Worker
import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Peho", 12000, 100)

    def test_is_worker_name_initialized_properly(self):
        self.assertEqual(self.worker.name, "Peho")

    def test_if_energy_is_incremented_after_rest(self):
        curr_e = self.worker.energy
        self.worker.rest()
        self.assertEqual(curr_e + 1, self.worker.energy)

    def test_if_error_is_raised_when_worker_try_to_work_with_negative_energy(self):
        self.worker.energy = -1
        with self.assertRaises(Exception):
            self.worker.work()

    def test_if_error_is_raised_when_worker_try_to_work_with_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_if_worker_money_increased_by_his_salary_after_work_method_called(self):
        curr_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money - self.worker.salary, curr_money)

    def test_if_energy_deceased_after_work_method_called(self):
        curr_e = self.worker.energy
        self.worker.work()
        self.assertEqual(self.worker.energy - curr_e, -1)

    def test_if_get_info_method_returns_proper_string(self):
        name = self.worker.name
        money = self.worker.money
        self.assertEqual(self.worker.get_info(),f'{name} has saved {money} money.')


if __name__ == "__main__":
    unittest.main()