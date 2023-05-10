# Adding class attributes and instance attributes using __init__() method

class Car:
    # class attribute
    milage = "Mi"

    def __init__(self, color, miles) -> None:
        # instance variable
        self.color = color
        self.miles = miles
    
# creating instance of Car class
car = Car("Red", 1749)
# Printing instance attributes using instance variable "car" 
print(car.color)
print(car.miles)
# Printing class attributes using instance of a class
print(car.milage)
# Printing class attributes using class name
print(Car.milage)
