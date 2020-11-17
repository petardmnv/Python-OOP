from project.food import Food, Vegetable, Fruit, Seed, Meat
from  project.animals.animal import Animal, Mammal, Bird
from project.animals.mammals import Tiger, Cat, Dog, Mouse
from project.animals.birds import Hen, Owl

meat = Meat(4)
veg = Vegetable(2)
fruit = Fruit(1)
seed = Seed(5)


owl = Owl("Pip", 10, 10)
hen = Hen("Hen", 5, 5)
m = Mouse("Mouse", 1, "B")
c = Cat("Cat", 3, "B")
d = Dog("Dog", 5, "B")
t = Tiger("Tiger", 10, "B")


print(t)
print(t.make_sound())
print(t.feed(meat))

print(t)


print(t.feed(meat))
print(t)