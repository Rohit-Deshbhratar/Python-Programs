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