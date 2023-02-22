# Write a program to print multiplication table of a number entered by user.

number = int(input("Please enter a number: "))


for table in range(1, 11):
    print(f"{number}  * {table} = {number * table}")
