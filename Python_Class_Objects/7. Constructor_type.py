# The purpose of having constructors in a class is initialize or assign values to the class
# or instance-level attributes (mainly instance attributes) whenever an instance of a class is being created.
# Types => (1) Default Constructor, (2) Non parameterized Constructor, (3) Parameterized Constructor

# (1) Default constructor: When we do not include any constructor (the __init__ method) 
# in a class or forget to declare it, then that class will use a default constructor that is empty.

# (2) Non-parameterized constructor: This type of constructor does not take any arguments 
# except a reference to the instance being created

class NonParameterizred:
    def __init__(self) -> None:
        print("The constructor is initialized when object is created of class NonParameterizred")

np = NonParameterizred()

# (3) Parameterized constructor: A parametrized constructor can take one or more 
# arguments, and the state of the instance can be set as per the input arguments 
# provided through the constructor method.

class Name:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last

name = Name("Rohit", "Deshbhratar")
print(f"{name.first} {name.last}")
