# Write a program to input eight numbers from the user and display all the unique numbers (once).

unique = set()

count = 1
while count <= 8:
    print("Please enter number: ")
    number = int(input())
    unique.add(number)
    count += 1

print(unique)
