import unittest
from solutions.worker import Worker


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Peho", 12000, 100)


    def test_is_worker_name_initialized_properly(self):
        self.assertEqual(self.worker.name, "Peho")

if __name__ == "__main__":
    unittest.main()

