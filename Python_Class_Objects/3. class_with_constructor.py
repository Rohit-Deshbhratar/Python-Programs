# Program: A class with parameterized constructor

class Circle:
    def __init__(self, pi, r) -> None:
        self.pi = pi
        self.r = r
    
    def area(self):
        print(f"Area of circle = {self.pi * (self.r * self.r)}")

circle = Circle(3.14, 4)
circle.area()
#####################################################################

class Rectangle:
    def __init__(self) -> None:
        self.length = 20
        self.breadth = 10
    
    def area(self):
        print(f"Area of Rectangle: {self.length * self.breadth}")

rect = Rectangle()
rect.area()
