class dictionary_iter:
    def __init__(self, kwargs):
        self.dictionary = kwargs
        self.zipped = zip(self.dictionary)
        self.keys = [k for k in self.dictionary.keys()]

    def __iter__(self):
        return self

    def __next__(self):
        if self.keys:
            key = self.keys[0]
            del self.keys[0]
            return tuple([key, self.dictionary[key]])
        raise StopIteration

