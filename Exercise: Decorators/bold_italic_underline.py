def make_bold(fn):
    def wrap(*args):
        return f"<b>{fn(*args)}</b>"
    return wrap


def make_italic(fn):
    def wrap(*args):
        return f"<i>{fn(*args)}</i>"
    return wrap


def make_underline(fn):
    def wrap(*args):
        return f"<u>{fn(*args)}</u>"
    return wrap


@make_bold
@make_italic
@make_underline
def greet(*args):
    return f"Hello, {args[0]}"


print(greet("Peter"))