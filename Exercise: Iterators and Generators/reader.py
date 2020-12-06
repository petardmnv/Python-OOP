def read_next(*argc):
    for item in argc:
        for i in item:
            yield i


for i in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3}):
    print(i, end="")
