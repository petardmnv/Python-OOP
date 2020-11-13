from project.keeper import Keeper
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:

    def __init__(self, name: str, bugdet: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = bugdet
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal , price: int):
        if self.__budget < price:
            return "Not enough budget"
        elif self.__animal_capacity >= len(self.animals):
            return "Not enough space for animal"
        else:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.get_type()} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity >= len(self.workers):
            return "Not enough space for worker"
        else:
            return f"{worker.name} the {worker.get_type()} hired successfully"

    def fire_worker(self, worker_name: str):
        worker_names = [w.name for w in self.workers]
        if worker_name in worker_names:
            worker = self.get_worker_by_name(worker_name)
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def get_worker_by_name(self, worker_name: str):
        for w in self.workers:
            if w.name == worker_name:
                return w
        return
