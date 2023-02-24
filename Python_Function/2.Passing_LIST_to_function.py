# Program to pass LIST as an argument to a function

# Passing a LIST in function as an argument
def passList(fruits):
    for i in fruits:
        print(i, end=", ")

fruits = ["Mango", "Apple", "Grapes", "Watermelon", "Orange"]
passList(fruits)
