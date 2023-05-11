
path1 = r"C:\Users\rohit\OneDrive\Documents\Text1.txt"
path2 = r"C:\Users\rohit\OneDrive\Documents\Text2.txt"

with open(path1) as file1, open(path2) as file2:
    print(file1.readlines())
    print(file2.readlines())
