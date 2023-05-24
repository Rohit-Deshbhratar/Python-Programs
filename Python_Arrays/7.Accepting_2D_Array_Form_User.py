# Creating 2D array from user input

row = int(input("Please enter number of rows: "))
column = int(input("Please enter number of columns: "))

td_arr = []

print("\nPlease enter data row wise.")
for i in range(row):
    row_data = []
    for j in range(column):
        row_data.append(int(input()))
    td_arr.append(row_data)

print("\nYour entered data is...")
for row in range(row):
    for col in range(column):
        print(td_arr[row][col], end=" ")
    print()    