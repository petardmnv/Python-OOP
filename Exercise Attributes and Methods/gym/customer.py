from typing import ClassVar


class Customer:
    _id: ClassVar[int] = 0

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        Customer._id +=1
        self.id = Customer._id

    def __repr__(self):
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'

    @classmethod
    def get_next_id(cls):
        return cls._id + 1


