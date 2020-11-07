class Point:
    def __init__(self, x: int , y: int):
        self.x = x
        self.y = y

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    def distance(self, x: int, y: int):
        return pow(pow(abs(self.x - x), 2) + pow(abs(self.y - y), 2), 0.5)


p = Point(2, 4)

p.set_x(3)

p.set_y(5)

print(p.distance(10, 2))
