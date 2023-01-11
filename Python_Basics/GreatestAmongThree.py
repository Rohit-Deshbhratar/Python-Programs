# Program checks greates number among three inputed number.

print("Please enter 3 numbers to find greatest number among them.")
a = int(input("Please input first number: "))
b = int(input("Please input second number: "))
c = int(input("Please input third number: "))

if a > b:
    if a > c:
        print(f"{a} is greater than {b, c}")
    else:
        print(f"{c} is greater than {a, b}")
else:
    if b > c:
        print(f"{b} is greater than {a, c}")
    else:
        print(f"{c} is greater than {a, b}")