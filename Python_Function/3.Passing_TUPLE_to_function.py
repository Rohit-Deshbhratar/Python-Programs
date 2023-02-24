# Passing TUPLE to a function as an argument

def tupleToFunction(a=None, b=None):
    print(f"Value of 'a' = {a}")
    print(f"Value of 'b' = {b}")

a = 3
b = 6

# Passing as integers
print(f"\nPassing values as integers:")
tupleToFunction(a, b)

# Passing as TUPLE
print(f"Passing values as TUPLE to single variable:")
tupleToFunction((a,b))

# Passing as pack/unpack operator
print(f"Passing as pack/unpack operator:")
tupleToFunction(*(a,b))