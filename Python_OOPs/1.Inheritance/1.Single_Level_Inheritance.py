# Single level inheritance
# In this example, we created a Vehicle parent class with one "color" attribute and one 
# print_vehicle_info() method. Both the elements are a candidate for inheritance. 
# Next, we created two child classes, Bike and Truck. Each child class has one additional 
# attribute ("engine" and "capacity") and one additional method "print_me()". In the 
# "print_me()" methods in each child class, we access the parent class instance attribute as 
# well as child class instance attributes

class Vehicle:
    def __init__(self, color) -> None:
        self.color = color
    
    def print_vehile_info(self):
        print(f"This is vehicle, and color is {self.color}")
    
class Bike(Vehicle):
    def __init__(self, color, engine) -> None:
        self.color = color
        self.engine = engine
    
    def print_me(self):
        print(f"Bike with color {self.color} & engine capacity {self.engine}cc")

class Truck(Vehicle):
    def __init__(self, color, capacity) -> None:
        self.color = color
        self.capacity = capacity
    
    def print_me(self):
        print(f"Truck with color {self.color} & capacity {self.capacity}")


bike = Bike("Black", 125)
truck = Truck("Orange", 1200)

bike.print_vehile_info()
bike.print_me()

truck.print_vehile_info()
truck.print_me()
