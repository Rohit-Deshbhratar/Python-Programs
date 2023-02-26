# File basics in Python

try:
    filePath = r"C:\Users\rohit\OneDrive\Documents\poems.txt"
    file = open(filePath,'r')
    fileContent = file.read()
    print(f"File contents are:\n {fileContent}")
except Exception as e:
    print(e)
finally:
    file.close()


# Opening a file using WITH statement

filePath = r"C:\Users\rohit\OneDrive\Documents\poems.txt"
with open(filePath,'r') as file:
    fileContent = file.read()
    print(f"\nContents of a file:\n{fileContent}")
    