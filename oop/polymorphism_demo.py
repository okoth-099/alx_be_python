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
    # Create instances of Rectangle and Circle
    rectangle = Rectangle(10, 5)  # Rectangle with length 10 and width 5
    circle = Circle(7)            # Circle with radius 7

    # Print the areas
    print(f"The area of the Rectangle is: {rectangle.area()}")
    print(f"The area of the Circle is: {circle.area()}")

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

