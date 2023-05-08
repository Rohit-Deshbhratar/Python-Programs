# Class with object
# Initializing values in constructor
class Employee:
    def __init__(self) -> None:
        self.name = 'Rohit'
        self.id = 1749
        self.city = 'Chandrapur'

    # methods
    def getInfo(self):
        print(f'Employee info \n Name: {self.name} \n ID: {self.id} \n City: {self.city}')
    
# creating class object
emp = Employee()
# calling class method using object
emp.getInfo()
#####################################################################

# Passing values to constructor
class Employee:
    def __init__(self, name, id, city) -> None:
        self.name = name
        self.id = id
        self.city = city

    # methods
    def getInfo(self):
        print(f'Employee info \n Name: {self.name} \n ID: {self.id} \n City: {self.city}')
    
# creating class object
emp = Employee('Rohit', 1749, 'Chandrapur')
# calling class method using object
emp.getInfo()
#####################################################################

# Updating/Modifying class attributes
class Employee:
    def __init__(self) -> None:
        self.name = 'Rohit'
        self.city = 'Chandrapur'
    
    def getInfo(self):
        print(f'Employee info \n Name: {self.name} \n City: {self.city}')

emp = Employee()
emp.getInfo()

# Updating class attribute values
emp.name = 'Vinit'
emp.city = 'Chicago'

print("Updated attributes: ")
emp.getInfo()

