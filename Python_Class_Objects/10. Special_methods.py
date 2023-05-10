# Special methods in Python is known as "DUNDERS"

class Car:
    # class attribute
    milage = "Mi"

    def __init__(self, color, miles) -> None:
        # instance attributes
        self.color = color
        self.miles = miles
    
    # special method
    def __str__(self) -> str:
        return f"Color of a car is {self.color} and milage is {self.miles}"

car = Car("Black", 128)
print(car)