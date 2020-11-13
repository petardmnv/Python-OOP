class Lion:

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    @staticmethod
    def get_needs():
        return 50

    @staticmethod
    def get_type():
        return "Lion"

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

