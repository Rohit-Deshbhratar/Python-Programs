# Function body
def hello():
    print("Hello, inside function.")
#Function call
hello()

# Parameterized function
def favouriteFruit(fruit):
    print(f"My favourite fruit is {fruit}")

favouriteFruit("Mango")

# Default parameterized function
def favouriteFruit(fruit = "Water Melon"):
    print(f"My favourite fruit is {fruit}")

favouriteFruit()
favouriteFruit("Mango")

# Return statement
def square(number):
    return number * number
    
print(square(9))

# Arbitrary arguments, *args
def unlimitedArgs(*args):
    print(f"Printing all arguments: {args}")
    print(f"Printing specific argument at zero location: {args[0]}")
    print(f"Printing specific argument at first location: {args[1]}")
    print(f"Printing specific argument at second location: {args[2]}")

unlimitedArgs("Rohit", 1989, "Sanu")

# Keyword argument
def keyword(nick_name, name="NA"):
    print(f"Nick name is '{nick_name}', real name is '{name}'")

keyword(nick_name="ricky", name="rohit")
keyword(nick_name="Ashwin")

# Arbitrary keyword arguments, **kwargs
def countries(**country):
    print(f'I want to visit: {country["capital"]}')
    print(f'I want to visit: {country["country"]}')
    print(f'I want to visit: {country["place"]}')
    print(f'I want to visit: {country}')

countries(country="UK", capital = "London", place = "Zoo")