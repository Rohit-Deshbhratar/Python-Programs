# Write a program to create a dictionary of Hindi words with values as their English translation. 
# Provide the user with an option to look it up!

hindi = {"Namaste":"Hello", "Asman":"Sky", "Aenak":"Spects", "Kalam":"Pen","Akhabar":"News Paper"}

print(f"Available Hindi word in dictionary:\n")
for key in hindi:
    print(key, end = ' ')

word = input(str("\nEnter a word to find it's meaning: "))
if (word in hindi.keys()):
    print(f"{word} = {hindi.get(word)}")
else:
    print(f"Word not found: '{word}'. Please check for spelling.")