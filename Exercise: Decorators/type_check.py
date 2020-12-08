def type_check(n):
    def dec(fn):
        def inner(arg):
            if not isinstance(arg, n):
                return "Bad Type"
            return fn(arg)
        return inner
    return dec


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter("asdfg"))