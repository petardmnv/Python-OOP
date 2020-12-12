class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(name=self.name, surname=other.surname)

    def __repr__(self):
        return self.name + " " + self.surname


class Group:

    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __add__(self, other):
        return Group("ASDF", people=self.people + other.people)

    def __len__(self):
        return len(self.people)

    def __str__(self):
        res = ", ".join([str(p) for p in self.people])
        return f"Group {self.name} with members {res}"

    def __getitem__(self, key: int):
        return f"Person {key}: {str(self.people[key])}"
