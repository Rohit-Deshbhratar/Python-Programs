# The base class

class Vehicle():
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def get_name(self):
        print(f"The car is a {self.name}, model is {self.model}", end = ", ")

# Implementing single inheritance

class FuelCar(Vehicle):
    def __init__(self, name, model, combust_type):
        self.combust_type = combust_type
        Vehicle.__init__(self, name, model)

    def get_fuel_car(self):
        super().get_name()
        print(f"combust type is {self.combust_type}")

# Implementing hierarchical inheritance

class ElectricCar(Vehicle):
    def __init__(self, name, model, battery_power):
        self.battery_power = battery_power
        super().__init__(name, model)
    
    def get_electric_car(self):
        super().get_name()
        print(f"battery power is {self.battery_power}")

# Implementing multi-level inheritance

class GasolineCar(Vehicle):
    def __init__(self, name, model, combust_type, gas_capacity):
        self.gas_capacity = gas_capacity
        FuelCar.__init__(self, name, model, combust_type)
    
    def get_gasoline_car(self):
        super().get_name()
        print(f"gas capacity is {self.gas_capacity}")

# Implementing multiple inheritance

class HybridCar(FuelCar, ElectricCar):
    def __init__(self, name, model, combust_type, battery_power):
        FuelCar.__init__(self, name, model, combust_type)
        ElectricCar.__init__(self, name, model, battery_power)
        self.battery_power = battery_power

    def get_hybrid_car(self):
        self.get_fuel_car()        
        print(f"battery power is {self.battery_power}")
        print()

def main():
    print("Single Inheritance.")
    fuel = FuelCar("Honda", "Accord", "Petrol")
    fuel.get_fuel_car()
    print()

    print("Hierarchical inheritance.")
    electric_car = ElectricCar("Tesla", "ModelX", "200MWH")
    electric_car.get_electric_car()
    print()

    print(f"Multi-level inheritance.")
    gasoline_car = GasolineCar("Toyota", "Corolla", "Gasoline", "50Liters")
    gasoline_car.get_gasoline_car()
    print()

    print("Multiple Inheritance")
    hybrid_car = HybridCar("Toyota", "Prius", "Hybrid", "100MWH")
    hybrid_car.get_hybrid_car() 

main()
