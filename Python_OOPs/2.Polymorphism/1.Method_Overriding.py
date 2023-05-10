# Method overriding

class Vehicle:
    def __init__(self, color) -> None:
        self.color = color
    
    def print_me(self):
        print(f"This is vehicle and color is {self.color}")

class Bike(Vehicle):
    def __init__(self, color, engine) -> None:
        self.color = color
        self.engine = engine
    
    def print_me(self):
        print(f"Bike with color {self.color} with engine {self.engine}CC")
    
class Truck(Vehicle):
    def __init__(self, color, capacity) -> None:
        self.color = color
        self.capacity = capacity
    
    def print_me(self):
        print(f"Truck with color {self.color} & capacity {self.capacity} ton")

vehicle = Vehicle("Black")
vehicle.print_me()

bike = Bike("Red", 220)
bike.print_me()

truck =Truck("Yellow", 1200)
truck.print_me()