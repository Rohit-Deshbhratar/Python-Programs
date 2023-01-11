# Program checks greatest number among four numbers.

print("Please enter 4 number to find greatest among them.")
a = int(input("Please enter first number: "))
b = int(input("Please enter second number: "))
c = int(input("Please enter third number: "))
d = int(input("Please input fourth number: "))

if (a > b and a > c and a > d):
    print(f"{a} is greater.")
elif (b > c and b > d):
    print(f"{b} is greater.")
elif (c > d):
    print(f"{c} is greater.")
elif (d > c):
    print(f"{d} is greater.")
else:
    print("Either any value or all values are equal.")