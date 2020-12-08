import time


def exec_time(fn):
    def wrap(*args, **kwargs):
        now = time.time()
        fn(*args, **kwargs)
        end = time.time()
        return end - now
    return wrap


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))