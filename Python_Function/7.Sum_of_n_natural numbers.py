#Write a program to print addition of first 'N' natural numbers using function

number = int(input("Please enter number to find addition upto the number entered by you: "))

counter = 0
total =0

def addNaturalNumber(num):
    global counter, total
    while (counter <= num):
        total = total + counter
        counter += 1

addNaturalNumber(number)
print(f"Total: {total}")