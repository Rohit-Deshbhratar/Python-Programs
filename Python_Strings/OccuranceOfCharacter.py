# Find occurance of a character

# Method 1
# Using loops

string = "Lorem ipsum dolor sit amet"
counter = 0
charCount = "m"
for i in string:
    if i == charCount:
        counter += 1 
print(f"Count of '{charCount}' is {counter}")