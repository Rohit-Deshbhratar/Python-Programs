# In this program we are going to add and delete columns in worksheet.
# Make sure that no column is inserted before column 8.
# To delete inserted column uncomment line number 17 & 19.

from openpyxl import *

# Load workbook, select worksheet
wb = load_workbook("sample.xlsx")
sheet = wb["Insert Row"]

# Insert 3 columns before 8th column in a worksheet
sheet.insert_cols(8, 3)
# Save workbook
wb.save("sample.xlsx")

# Delete 3 columns from position 8 i.e. H:J
#sheet.delete_cols(8, 3)
# Save workbook
#wb.save("sample.xlsx")