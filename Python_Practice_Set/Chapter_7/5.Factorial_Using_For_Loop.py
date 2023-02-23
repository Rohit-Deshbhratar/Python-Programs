# Write a program to find factorial of a number using for loop.

number = int(input("Please enter a number to find it's factirial: "))
factorial = 1

if number == 0:
    print(f"Factorial of {0} is {1}.")
elif number < 0:
    print("Sorry, a number should not be less than zero.")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print(f"Factorial of {number} is {factorial}")
