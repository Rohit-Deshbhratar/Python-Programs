# (1) Instance methods: They are associated with an instance and need an instance to be 
# created first before executing them. They accept the first attribute as a reference to 
# the instance (self) and can read and update the state of the instance.

# (2) Class methods: These methods are declared with the @classmethod decorator. These methods 
# don't need a class instance for execution. For this method, the class reference 
# (cls is used as a convention) will be automatically sent as the first argument.

# (3) Static methods: These methods are declared with the @staticmethod decorator. 
# They don't have access to cls or self objects. Static methods are like utility functions that 
# take certain arguments and provide the output based on the arguments' values

class Car:
    # class attribute
    milage = "Mi"

    def __init__(self, color, miles) -> None:
        # instance attributes
        self.color = color
        self.miles = miles
    
    # instance method
    def print_color(self):
        print(f"Color of a car is {self.color}")
    
    @classmethod
    def print_units(cls):
        print(f"milage = {cls.milage}")
        print(f"class name is {cls.__name__}")
    
    @staticmethod
    def print_hello():
        print("Hello from static method")

car = Car("Red", 129)

car.print_color()
car.print_units()
car.print_hello()

Car.print_color(car)
Car.print_units()
Car.print_hello()
