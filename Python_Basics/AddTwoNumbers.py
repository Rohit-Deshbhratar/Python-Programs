import operator
# Addition of two numbers
###################################################################################################

# Simple addition
num1 = 5
num2 = 7

print(f"Addition of {num1} and {num2} is: {num1 + num2}")
###################################################################################################

# Using user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition of {num1} and {num2} is: {num1 + num2}")
###################################################################################################

# Using function
def add(a, b):
    return a + b

num1 = 4
num2 = 3
sum = add(num1, num2)
print("Addition of {0} and {1} is {2}" .format(num1, num2, sum))
###################################################################################################

# Using "operator.add()" method

num1 = 8
num2 = 56

sum = operator.add(num1, num2)
print("Sum of {0} and {1} is {2}" .format(num1, num2, sum))
###################################################################################################

# Using Lambda function
addition= lambda x, y: x + y

num1 = 9
num2 = 6

sum = addition(num1, num2)
print("Addition of {0} and {1} is {2}." .format(num1, num2, sum))
###################################################################################################

# Using recursive function
def recursive_add(x, y):
    if y == 0:
        return x
    else:
        return recursive_add(x + 1, y - 1)

num1 = 11
num2 = 23

result = recursive_add(num1, num2)
print("Sum of ", num1, "and ", num2, "is ", result)
###################################################################################################
