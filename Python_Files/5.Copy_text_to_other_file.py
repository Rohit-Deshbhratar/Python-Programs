# Copy text from one file to another file.

path1 = r"C:\Users\rohit\OneDrive\Documents\Text1.txt"
path2 = r"C:\Users\rohit\OneDrive\Documents\Text3.txt"

with open(path1, "r") as file1, open(path2, "w+") as file3:
    for data in file1.readlines():
        file3.writelines(data)
