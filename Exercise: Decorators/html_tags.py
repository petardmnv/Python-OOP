def tags(tag):
    def inner(fn):
        def wrap(*args):
            return f"<{tag}>{fn(*args)}</{tag}>"
        return wrap
    return inner


@tags('p')
def smth(*args):
    return "".join(args)


print(smth("aagrgr", "lmao"))