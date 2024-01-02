# Find max of two.
###################################################################################################
# Simple comparison

num1 = 7
num2 = 9

if num1 > num2:
    print(f"{num1} is greater.")
else:
    print(f"{num2} is greater.")
###################################################################################################

# Using function
num1 = 48
num2 = 65

def maximum(a, b):
    if a > b:
        return a
    else:
        return b

result = maximum(num1, num2)
print(f"{result} is greater.")
###################################################################################################

# Using "max()" function

num1 = 8
num2 = 6

result = max(num1, num2)
print(f"{result} is greater.")
###################################################################################################

# Using ternary operator

num1, num2 = 5, 7

print(num1 if num1 > num2 else num2, "is greater.")
###################################################################################################

# Using lambda function

a = 3
b = 6
maximum = lambda a, b: a if a > b else b
print(f"{maximum(a, b)} is greater.")
###################################################################################################

# Using list comprehension

a = 5; b = 7
x = [a if a > b else b]
print(f"{x} is greater.")
###################################################################################################

# Using sort()

a = 9; b = 6

x = [a, b]
x.sort()
print(f"{x[-1]} is greater.")