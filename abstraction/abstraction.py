from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Concrete subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Creating instances of the subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calling methods on the instances
print("Circle Area:", circle.area())           # Output: Circle Area: 78.5
print("Circle Perimeter:", circle.perimeter()) # Output: Circle Perimeter: 31.400000000000002
print("Rectangle Area:", rectangle.area())     # Output: Rectangle Area: 24
print("Rectangle Perimeter:", rectangle.perimeter()) # Output: Rectangle Perimeter: 20
