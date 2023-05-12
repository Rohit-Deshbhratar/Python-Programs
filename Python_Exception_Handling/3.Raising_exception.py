# Raising exception in a program
# Comment any of the "print()" in try block to see the raised exceptions
import math

def sqrt(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Only numbers are allowed")
    if num < 0:
        raise Exception ("Negative numbers not supported")
    return math.sqrt(num)

try:
    print(sqrt(9))
    print(sqrt('s'))
    print(sqrt(-9))
except Exception as e:
    print(e)