# Use of else block
# Correct path = "C:\Users\rohit\OneDrive\Documents\Text3.txt"

try:
    path = r"C:\Users\rohit\OneDrive\Documents"

    file_handle = open(path, "w")
except Exception as e:
    print(f"Writing failed because exception occured: {e}")
else:
    file_handle.writelines("Writing because, no exception occured. :)")
finally:
    file_handle.close()