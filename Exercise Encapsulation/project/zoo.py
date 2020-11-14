from project.keeper import Keeper
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from typing import Union
Animals = Union[Cheetah, Lion, Tiger]
Workers = Union[Keeper, Vet, Caretaker]


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animals, price: int):
        if self.__budget < price:
            return "Not enough budget"
        elif self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        else:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.get_type()} added to the zoo"

    def hire_worker(self, worker: Workers):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        else:
            self.workers.append(worker)
            return f"{worker.name} the {worker.get_type()} hired successfully"

    def fire_worker(self, worker_name: str):
        worker_names = [w.name for w in self.workers]
        if worker_name in worker_names:
            worker = self.get_worker_by_name(worker_name)
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum([w.salary for w in self.workers])
        if salaries <= self.__budget:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tend_cost = sum([a.get_needs() for a in self.animals])
        if tend_cost <= self.__budget:
            self.__budget -= tend_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        result = list()
        result.append(f"You have {len(self.animals)} animals")
        lions = [l for l in self.animals if l.get_type() == "Lion"]
        result.append(f"----- {len(lions)} Lions:")
        for l in lions:
            result.append(repr(l))

        tigers = [t for t in self.animals if t.get_type() == "Tiger"]
        result.append(f"----- {len(tigers)} Tigers:")
        for t in tigers:
            result.append(repr(t))

        cheetah = [c for c in self.animals if c.get_type() == "Cheetah"]
        result.append(f"----- {len(cheetah)} Cheetahs:")
        for c in cheetah:
            result.append(repr(c))

        return '\n'.join(result)

    def workers_status(self):
        result = list()
        result.append(f"You have {len(self.workers)} workers")

        keepers = [k for k in self.workers if k.get_type() == "Keeper"]
        result.append(f"----- {len(keepers)} Keepers:")
        for k in keepers:
            result.append(repr(k))

        caretakers = [c for c in self.workers if c.get_type() == "Caretaker"]
        result.append(f"----- {len(caretakers)} Caretakers:")
        for c in caretakers:
            result.append(repr(c))

        vets = [v for v in self.workers if v.get_type() == "Vet"]
        result.append(f"----- {len(vets)} Vets:")
        for v in vets:
            result.append(repr(v))

        return '\n'.join(result)

    def get_worker_by_name(self, worker_name: str):
        for w in self.workers:
            if w.name == worker_name:
                return w
        return
