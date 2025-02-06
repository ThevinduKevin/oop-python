
# polymorphism - many forms. two type of polymorphism are inheritance and "Duck typing"

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):     # this is an abstract class
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * 2


shapes = [Circle(2), Square(3)]

for shape in shapes:
    print(shape.area())


