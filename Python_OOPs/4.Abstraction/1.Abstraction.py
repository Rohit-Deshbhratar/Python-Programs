# Basic abstraction

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def hello(self):
        print("Hello from abstract class.")
    
    @abstractmethod
    def print_me():
        pass

class Bike(Vehicle):
    def __init__(self, color, engine) -> None:
        self.color = color
        self.engine = engine
    
    def print_me(self):
        print(f"Color is {self.color} and engine {self.engine} CC")

# vehicle =Vehicle()
# vehicle.hello()
bike = Bike("Black", 250)
bike.print_me()
bike.hello()