class reverse_iter: #Yes I know.. This is so wrong.
    def __init__(self, iterator):
        self.iterator = iterator
        self.index = len(self.iterator)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index >= 0:
            return self.iterator[self.index]
        raise StopIteration

