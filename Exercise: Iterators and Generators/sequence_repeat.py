class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.i = 0
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.number:
            self.index += 1
            self.i += 1
            if self.index > (len(self.sequence) - 1):
                self.index = 0
            return self.sequence[self.index]
        raise StopIteration


result = sequence_repeat('abc', 7)
for item in result:
    print(item, end='')