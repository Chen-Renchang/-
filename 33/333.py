import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

    def compare_area(self, other):
        return self.area() > other.area()

    def compare_perimeter(self, other):
        return self.perimeter() > other.perimeter()


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Вычисление площади по формуле Герона
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Пример использования
square = Square(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)
circle = Circle(7)

print("Square area:", square.area())
print("Rectangle area: ", rectangle.area())
print("Triangle area", triangle.area())
print("Circle area:", circle.area())

print("Square perimeter ", square.perimeter())
print("Rectangle perimeter: ", rectangle.perimeter())
print("Triangle perimeter: ", triangle.perimeter())
print("Circle perimeter:", circle.perimeter())

print("Is square area greater than rectangle? ", square.compare_area(rectangle))
print("Is triangle perimeter greater than circle? ", triangle.compare_perimeter(circle))
