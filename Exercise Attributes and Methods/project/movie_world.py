from typing import List
from project.dvd import DVD
from project.customer import Customer


class MovieWorld:
    customers = List[Customer]
    dvds = List[DVD]

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        pass

    @staticmethod
    def customer_capacity():
        pass

    def add_customer(self, customer: Customer):
        pass

    def add_dvd(self, dvd: DVD):
        pass

    def rent_dvd(self, customer_id: int, dvd_id: int):
        pass

    def return_dvd(self, customer_id: int, dvd_id: int):
        pass

    def __repr__(self):
        return 
