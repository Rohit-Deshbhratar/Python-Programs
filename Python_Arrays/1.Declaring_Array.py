# How to declare array in Python?
# There are three ways to use array in a program
# First "import array" should be the first line of program,
# then create a variable and store array using following syntax
# variable = array.array(typecode,[array_elements])
# Uncomment each section to study all three declarations.

# import array

# arr = array.array('i', [2, 5, 7, 11])
# printing array
# print(arr)

# Second way of declaring array
# First "import array as arr" should be the first line of program,
# where arr => alias for array.

# import array as arr

# prime = arr.array("i", [2, 3, 5, 7, 11])
# print(prime)

# Third way of using array in a program
# First line of program should be "from array import *"

# from array import *

# even = array("i", [2, 4, 6, 8, 10])
# print(even)