class Circle:
    def __init__(self):
        self.radius = 0
        self.pi = 3.14
    
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14
    
    def area(self):
        return self.pi * self.radius * self.radius
    
    def perimeter(self):
        return 2 * self.pi * self.radius
    
def main():
    circle = Circle(5)
    print(f"Area: {circle.area():.2f}")
    print(f"Area: {circle.perimeter():.2f}")

if __name__ == "__main__":
    main()
