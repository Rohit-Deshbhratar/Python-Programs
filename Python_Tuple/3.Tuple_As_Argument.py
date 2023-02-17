def tupleFunction(myTuple, a, b):
    print(f"tuple of first parameter: {type(myTuple)}")
    print(f"tuple of second parameter: {type(a)}")
    print(f"tuple of third parameter: {type(b)}")
    print("\n Passed parameters are: \n")
    print(f"tuple first parameter: {myTuple}")
    print(f"tuple second parameter: {a}")
    print(f"tuple third parameter: {b}")

tupleFunction((1, 3, 7), 15, 99)

# Passing only TUPLE as parameter

def onlyTuple(a, b):                
    print(f"Type of parameter: {type(a)}")
    print(f"Type of parameter: {type(b)}")

onlyTuple((0, 2), 17)