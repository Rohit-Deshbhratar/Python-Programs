# Accessing individual items in an array.

import array

arr = array.array("i", [10, 2, 65, 79])
# Printing values using array index.
print(f"Value at index 0: {arr[0]}")
print(f"Value at index 1: {arr[1]}")
print(f"Value at index 2: {arr[2]}")
print(f"Value at index 3: {arr[3]}")

# Negative indexing
print("\nNegative indexing...")
print(f"Value at index -1: {arr[-1]}")
print(f"Value at index -3: {arr[-2]}")
print(f"Value at index -3: {arr[-3]}")
print(f"Value at index -4: {arr[-4]}")

# Searching in an array using index() method
print("\nSerach using index() method...")
print(f"Value {arr[1]} present at index: {arr.index(2)}")
print(f"Value {arr[3]} present at index: {arr.index(79)}")

# Printing array using for loop
print("\nLooping through array...")
for i in arr:
    print(i, end=" ")
print()

# Printing array using for loop, range(), len()
print("\nLooping through array with range() and len()...")
for i in range(len(arr)):
    print(arr[i], end=" ")
print()

# Slicing an array
print("\nArray Slicing...")
print(f"First two numbers: {arr[:2]}")
print(f"Reversing array: {arr[::-1]}")

# Changing the value at particular index in an array
print("\nChanging the value at particular index in an array...")
print(f"Original array: {arr}")
arr[1] = 97
print(f"Updated array: {arr}")
