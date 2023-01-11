# Append, Insert, Pop values in a list.

appendList = [12, 35, 56, 74, 61, 33, 11, 42]

print(f"Original list: {appendList}")
print(f"Length before appending value: {len(appendList)}")
# Append 99
appendList.append(99)
print(f"Length after appending value: {len(appendList)}")
print(f"List after appending: {appendList}")

# Inserting new value in a specified index of list
print(f"List before inserting value: {appendList}")
appendList.insert(3, 0)
print(f"List after inserting value: {appendList}")

# Pop a value from list
print(f"List before pop: {appendList}")
appendList.pop(5)
print(f"List after pop: {appendList}")