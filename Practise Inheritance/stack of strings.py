class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        return self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        result = ", ".join(reversed(self.data))
        return f"[{result}]"