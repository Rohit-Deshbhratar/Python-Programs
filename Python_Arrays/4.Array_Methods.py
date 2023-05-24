# Implementing array methods

import array

arr = array.array("i", [51, 61, 12, 47, 31])

# Adding new value to the array
print(f"Array before:{arr}")
arr.append(48)
print(f"Array after:{arr}")

# Extending array
print("\nExtending an array...")
print(f"Before exetnding array: {arr}")
arr.extend([41,89,63])
print(f"After extending array: {arr}")

# inserting an item at particular index
print("\nInserting an item at particular index...")
print(f"Original array: {arr}")
arr.insert(2, 39)
print(f"Value {arr[2]} inserted at index {arr.index(39)}")
print(f"Updated array: {arr}")

# Removing an item from array using remove()
print("\nRemoving an item from array using remove()...")
print(f"Original array: {arr}")
print(f"Removing item {arr[1]} from array {arr.remove(61)}")
print(f"Updated array: {arr}")

# Removing an item from array using pop()
print("\nRemoving an item from array using pop()...")
print(f"Original array: {arr}")
print(f"Removing item {arr[0]} from array")
arr.pop(0)
print(f"Updated array: {arr}")

# Count number of occurances of an item in an array
print("\nCount number of occurances of an item in an array...")
arr.extend([39, 31, 89, 89])
print(f"Array: {arr}")
print(f"Item {arr[0]} is repeated {arr.count(39)} times.")
print(f"Item {arr[3]} is repeated {arr.count(31)} times.")
print(f"Item {arr[6]} is repeated {arr.count(89)} times.")

# Searching an item with start and stop parameter in index()
print("\nSearching an item with start and stop parameter in index()...")
print(f"Array: {arr}")
print(f"{arr.index(89, 0, 11)}")

# Array to list
print("\nArray to list...")
print(f"Array: {arr}, List: {arr.tolist()}")

# Appending list to array
print("\nAppending list to array...")
list_arr = [10, 30, 56, 74, 11]
arr = array.array("i", [1, 5, 9, 43, 32])
arr.fromlist(list_arr)
print(f"List: {list_arr}, Array: {arr}")
