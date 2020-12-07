def even_parameters(fn):
    def inner(*args, **kwargs):
        for i in args:
            print(i)
            if not isinstance(i, int) or i % 2 != 0:
                return "Please use only even numbers!"
        return fn(*args)

    return inner


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
