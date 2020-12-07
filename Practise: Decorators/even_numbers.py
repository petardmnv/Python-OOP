def even_numbers(fn):
    def wrapper(*args, **kwargs):
        res = fn(*args)
        return [n for n in res if n % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(num):
    return num


print(get_numbers([1, 3, 4, 6]))