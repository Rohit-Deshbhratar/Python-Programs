# Write a program to sum a list with 4 numbers.

sum = []

for i in range(4):
    sumList = int(input("Enter number: "))
    sum.append(sumList)
 
add = 0
for i in sum:
    print(f"Index of {i} is {sum.index(i)}")
    add = add + i

print(f"addition: {add}")