import math

# Base Class: Shape
class Shape:
    def area(self):
        """Method to be overridden by derived classes."""
        raise NotImplementedError("Subclasses must implement this method")

# Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override area method to calculate rectangle area."""
        return self.length * self.width

# Derived Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize the circle with radius."""
        self.radius = radius

    def area(self):
        """Override area method to calculate circle area."""
        return math.pi * (self.radius ** 2)

# Example of polymorphic behavior
if __name__ == "__main__":
    # Create a list of different shapes
    shapes = [
        Rectangle(4, 5),  # Rectangle with length 4 and width 5
        Circle(3)         # Circle with radius 3
    ]

    # Loop through each shape and print the area
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is {shape.area()}")

~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
polymorphism_demo.py [unix] (02:59 01/01/1970)                                                                                                                                          0,1 All
-- INSERT --

