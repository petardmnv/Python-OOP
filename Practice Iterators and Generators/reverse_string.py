def reverse_text(s: str):
    index = len(s)
    while index > 0:
        index -= 1
        yield s[index]


for char in reverse_text("step"):
    print(char, end='')