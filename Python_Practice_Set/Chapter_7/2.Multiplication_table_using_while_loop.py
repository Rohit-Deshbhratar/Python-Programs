# Write a program to print multiplication table of a number entered by user.

number = int(input("Please enter a number: "))
counter = 1

while counter <= 10:
    print(f"{number} * {counter} = {number * counter}")
    counter += 1
