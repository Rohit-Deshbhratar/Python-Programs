# Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use keys as their names. 
# Assume that the names are unique.

language = dict()

counter = 1
while counter <= 4:
    print("Please enter friends name: ")
    key = str(input())
    print("Please enter favourite language: ")
    value = str(input())
    language[key] = value
    counter += 1

print(language)
print(type(language))

# If the names of 2 friends are the same; what will happen to the program in Program 6?
# Please enter friends name: 
# ricky
# Please enter favourite language: 
# marathi
# Please enter friends name: 
# ricky
# Please enter favourite language: 
# hindi
# Please enter friends name: 
# vinit
# Please enter favourite language: 
# bangla
# Please enter friends name: 
# lata 
# Please enter favourite language: 
# tamil
# Output => {'ricky': 'hindi', 'vinit': 'bangla', 'lata': 'tamil'}
# If the languages of two friends are the same; what will happen to the program in Program 6? => Works fine