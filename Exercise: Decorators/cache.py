def cache(fn):
    keys = dict()

    def wrap(num):
        if num not in keys:
            keys[num] = fn(num)
        return keys[num]
    setattr(wrap, 'log', keys)
    return wrap


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)