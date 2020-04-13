"""
 prototype
    会减少类内部方法签名的数量，并提高代码的可读性和可维护性。
"""


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    @property
    def width(self):
        return self.x2 - self.x1

    @width.setter
    def width(self, value):
        self.x2 = self.x1 + value

    @property
    def height(self):
        return self.y2 - self.y1

    @height.setter
    def height(self, value):
        self.y2 = self.y1 + value


if __name__ == '__main__':
    rectangle = Rectangle(10, 10, 25, 34)
    print(rectangle.width)
    print(rectangle.height)

    rectangle.width = 100
    print(rectangle)