def multiply(num):
    def inner(fn):
        def wrapper(*argc, **kwargs):
            return fn(*argc) * num
        return wrapper
    return inner


@multiply(3)
def add_ten(n):
    return n + 10


print(add_ten(4))