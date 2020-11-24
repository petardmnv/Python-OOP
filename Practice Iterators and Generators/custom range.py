class custom_range: #Yes I know.. This is so wrong.
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            self.start += 1
            return self.start - 1
        raise StopIteration


one_ten = custom_range(1, 4)
for i in one_ten:
    print(i)