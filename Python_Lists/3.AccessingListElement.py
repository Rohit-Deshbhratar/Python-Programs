# Accessing elements in the LIST.

tempList = ['w', 't', 'v', 'm', "X", "P", 5, 9, 0, 3, 4]

print("Accessing list manually")
print(f"Index of 'w' is: {tempList.index('w')}")
print(f"Index of 't' is: {tempList.index('t')}")
print(f"Index of 'v' is: {tempList.index('v')}")
print(f"Index of 'm' is: {tempList.index('m')}")
print(f"Index of 'X' is: {tempList.index('X')}")
print(f"Index of 'P' is: {tempList.index('P')}")
print(f"Index of 5 is: {tempList.index(5)}")
print(f"Index of 9 is: {tempList.index(9)}")
print(f"Index of 0 is: {tempList.index(0)}")
print(f"Index of 3 is: {tempList.index(3)}")
print(f"Index of 4 is: {tempList.index(4)}")


print("\nAccessing list by loop")

for i in tempList:
    print(f"Index of {i} is {tempList.index(i)}")