# Updating class attributes using instance variable or class name
# If updated using ->
# instance variable = it will be updated for particular instance
# class name = updated for all the instance of a class

class Car:
    milage = "Mi"

    def __init__(self, color, miles) -> None:
        self.color = color
        self.miles = miles
    
car1 = Car("Red", 100)
car2 = Car("Pink", 325)
# Printing class attributes using instance and class name
print(f"using car1: {car1.milage}")
print(f"using car2: {car2.milage}")
print(f"using Class Car: {Car.milage}")

# Updating class attribute using class instance
car1.milage = "Km"

print(f"using car1: {car1.milage}")
print(f"using car2: {car2.milage}")
print(f"using Class Car: {Car.milage}")

# Updating class attribute using class name
Car.milage = "Km"

print(f"using car1: {car1.milage}")
print(f"using car2: {car2.milage}")
print(f"using Class Car: {Car.milage}")
