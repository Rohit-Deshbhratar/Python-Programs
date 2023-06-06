# In this program we are going to add multiple values to the excel sheet.

from openpyxl import *

# Load workbook
wb = load_workbook("sample.xlsx")

# Select worksheet
sheet = wb["Student"]

# Load this data into worksheet
data = [('Roll_No', 'Name', 'Age', 'Stream', 'Percentage'),
        (1, 'Rohit', 34, 'IT', 71.20),
        (2, 'Parag', 40, 'BDS', 74.39),
        (3, 'Viraj', 12, 'School', 69.11),
        (4, 'Richa', 37, 'Ortho', 74.56),
        (5, 'Shruti', 33, 'CS', 76.41)]

# Appending data into selected worksheet
for i in data:
    sheet.append(i)

# Saving workbook
wb.save("sample.xlsx")