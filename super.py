
# super - function use in child class to call the constructor of the super class

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width


circle = Circle("red", False, 5)
square = Square("blue", True, 6)

print(circle.color)


# ***** overriding *****

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print("hi")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print("hello")
        super().describe()