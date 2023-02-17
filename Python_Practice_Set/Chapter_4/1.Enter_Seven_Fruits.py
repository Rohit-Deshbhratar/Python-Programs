# Write a program to store seven fruits in a list entered by the user.

# Empty list
fruits = []

# For loop will accept fruit names from user and append each input to the list.
for i in range(7):
    fruitsInput = input("Enter fruits name: ")
    fruits.append(fruitsInput)

# Prints entered inputs in list    
print(fruits)