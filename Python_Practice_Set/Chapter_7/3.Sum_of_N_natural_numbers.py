# Sum of "N" natural numbers.

limit = int(input("Please enter  number: "))
counter = 0
total = 0
while (counter <= limit):
    total = counter + total
    counter += 1

print(f"Sum of {limit} natural numbers is: {total}")