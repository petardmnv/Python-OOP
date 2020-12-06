def fibonacci():
    prev_num = 0
    num = 1
    yield 0
    yield 1
    while True:
        new_num = num + prev_num
        yield new_num
        prev_num = num
        num = new_num
