# Method Overloading
# Example 1
class Sum():
    def add(self, a, b, c = 0):
        return c + a + b

sum = Sum()
print(sum.add(20, 15, 4))
print(sum.add(19, 4))

# Example 2
class Area():
    def calculateArea(sels, length, breadth=-1):
        if breadth !=-1:
            return length * breadth
        else:
            return length * length
area = Area()
print(f"Area of rectangle: {area.calculateArea(4, 6)}")
print(f"Area of square: {area.calculateArea(5)}")

# Operator overloading
class ComplexNumbers():
    def __init__(self):
        self.real = 0
        self.imaginary = 0
    
    def set_value(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    # Overloading "+" operator
    def __add__(self, c): 
        result = ComplexNumbers() 
        result.real = self.real + c.real
        result.imaginary = self.imaginary + c.imaginary 
        return result 
    
    def display(self):
        print(f"({self.real}+{self.imaginary}i)")

complex_number1 = ComplexNumbers()
complex_number1.set_value(10,19)
complex_number2 = ComplexNumbers()
complex_number2.set_value(4, 5)
result = complex_number1 + complex_number2
result.display()


