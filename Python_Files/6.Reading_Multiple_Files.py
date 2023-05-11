# reading data from multiple files
import fileinput

path1 = r"C:\Users\rohit\OneDrive\Documents\Text1.txt"
path2 = r"C:\Users\rohit\OneDrive\Documents\Text2.txt"

with fileinput.input(files = (path1, path2)) as f:
    for line in f:
        print(f.filename())
        print(line)
