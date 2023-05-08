# Write a program to find text "twinkle" in a file.

filePath = r"C:\Users\rohit\OneDrive\Documents\poems.txt"
with open(filePath, 'r') as file:
    fileContent = file.read()
    if ('Twinkle' or 'twinkle') in fileContent:
        print("Text is present.")
    else:
        print("Text is not present.")


# OR

