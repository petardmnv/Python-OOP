from typing import List
from movieworld.dvd import DVD
from movieworld.customer import Customer


class MovieWorld:
    customers = List[Customer]
    dvds = List[DVD]

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        curr_c = self.get_customer(customer_id)
        curr_d = self.get_dvd(dvd_id)
        ids = [d.id for d in curr_c.rented_dvds]
        if dvd_id in ids:
            return f"{curr_c.name} has already rented {curr_d.name}"

        elif curr_d.is_rented:
            return "DVD is already rented"

        elif curr_d.age_restriction > curr_c.age:
            return f"{curr_c.name} should be at least {curr_d.age_restriction} to rent this movie"

        else:
            curr_d.is_rented = True
            curr_c.rented_dvds.append(curr_d)
            return f"{curr_c.name} has successfully rented {curr_d.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        curr_c = self.get_customer(customer_id)
        curr_d = self.get_dvd(dvd_id)
        ids = [d.id for d in curr_c.rented_dvds]
        if dvd_id in ids:
            curr_d.is_rented = False
            curr_c.rented_dvds.remove(curr_d)
            return f"{curr_c.name} has successfully returned {curr_d.name}"

        else:
            return f"{curr_c.name} does not have that DVD"

    def __repr__(self):
        res = []
        for c in self.customers:
            res.append(c.__repr__())

        for d in self.dvds:
            res.append(d.__repr__())

        return '\n'.join(res)

    def get_customer(self, customer_id: int):
        for c in self.customers:
            if customer_id == c.id:
                return c

    def get_dvd(self, dvd_id: int):
        for d in self.dvds:
            if d.id == dvd_id:
                return d

