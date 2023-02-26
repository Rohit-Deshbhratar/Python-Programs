# Write a program to convert inches to centimeters.

inch = float(input("Please enter a number in inches to convert it into centimeter: "))
output = 0

def inchToCM(inch):
    global output
    cm = inch * 2.54
    return cm

print(f"{inchToCM(inch)} cm")