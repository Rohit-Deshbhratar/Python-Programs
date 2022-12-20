# String reverse program

string = "Lorem ipsum dolor sit amet"

# Method 1
# String slicing
print("Using string slicing:")
print(f"Output: {string[::-1]}\n")

# Method 2
# Using function call

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "Lorem ipsum dolor sit amet"

print ("String: ")
print (s)
print ("The reversed string using loops: ")
print (reverse(s))


