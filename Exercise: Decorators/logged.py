def logged(fn):
    def inner(*args):
        return f"you called {fn.__name__}{args}\nit returned {fn(*args)}"
    return inner


@logged
def func(*args):
    return 3 + len(args)


print(func(1, 2, 3))
