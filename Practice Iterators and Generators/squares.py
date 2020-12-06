def squares(c: int):
    for i in range(1, c + 1):
        yield i ** 2


print(list(squares(5)))