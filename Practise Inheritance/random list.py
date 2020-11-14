import random


class RandomList(list):
    def get_random_element(self):
        r_element = random.choice(self)
        self.pop(self.index(r_element))
        return r_element


r = RandomList([1, 2, 3])
r.get_random_element()
print(r)