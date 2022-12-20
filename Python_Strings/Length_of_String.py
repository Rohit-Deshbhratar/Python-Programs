# Count length of a string

# Method 1
# Using in-built function

string = "Lorem ipsum dolor sit amet"
print(f"Length of '{string}' is {len(string)}")

# Method 2
# Using for loop
counter = 0
for i in string:
    counter += 1
print(f"Length of string using for loop: {counter}")

# Method 3
# Using while loop

while string[counter:]:
    counter += 1
print(f"Length of string using while loop: {counter}")    