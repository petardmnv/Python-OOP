class Person:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


p = Person("Peho", 12)
print(p.get_name())
print(p.get_age())