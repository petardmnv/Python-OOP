def number_increment(number):
    def incerace():
        return [i + 1 for i in number]
    return incerace()

print(number_increment([1, 2, 3]))