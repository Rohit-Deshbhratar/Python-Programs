# Program to print numbers in following pattern
"""
1
22
333
4444
55555
"""

row = int(input("Please enter number of rows you want: "))

for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()