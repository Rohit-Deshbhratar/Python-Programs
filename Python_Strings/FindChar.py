# Find a character in string

# Method 1
# Using find() method

string = "Lorem ipsum dolor sit amet"
print(f'Position of entered string is: {string.find("m")}')

# Method 2
# Using loop
count = 0
findChar = "s"
for i in string:
    if i == findChar:
        break
    count += 1
print(f"Found {findChar} at position {count}")