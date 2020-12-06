class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.number = 0
        self.c = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.c < self.count:
            self.c += 1
            res = self.number
            self.number += self.step
            return res
        raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)