# Write a program to find factorial of a number entered by user.

number = int(input("Please enter number to find it's factorial: "))

def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num * factorial(num - 1)        

print(f"Factorial is: {factorial(number)}")