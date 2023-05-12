# Custom exception

import math

class NegativeNumberError(Exception):
    def __init__(self) -> None:
        super().__init__("Negative numbers are not supported")

def sqrt(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Only numbers are allowed")
    if num < 0:
        raise NegativeNumberError
    return math.sqrt(num)

try:
    print(sqrt(49))
    print(sqrt('a'))
    print(sqrt(-5))
except NegativeNumberError as ne:
    print(ne)
except Exception as e:
    print(e)
        