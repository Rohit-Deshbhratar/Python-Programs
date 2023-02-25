# Write a program to print multiplication table using function.

number = int(input("Please enter number to print it's multiplication table: "))

def table(num):
   for i in range(1,11):
      print(f"{num} * {i} = {num * i}")

table(number)