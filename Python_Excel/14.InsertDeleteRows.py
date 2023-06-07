# In this program we are going to add row in an excel sheet at runtime.
# Please take a note that in worksheet "Insert Rows" a rectangle is formed B3:T3 To B16:T16.
# Make sure that you should restore worksheet to this condition before running this program
# Uncomment code at line number 19,20,21 one by one to see the effect.

from openpyxl import *

# Load workbook, select worksheet
wb = load_workbook("sample.xlsx")
sheet = wb["Insert Row"]

# Insert rows at row number 8,9,10
sheet.insert_rows(8)
sheet.insert_rows(9)
sheet.insert_rows(10)

wb.save("sample.xlsx")

# Delete rows numbers 8,9,10
# sheet.delete_rows(8)
# sheet.delete_rows(9)
# sheet.delete_rows(10)
wb.save("sample.xlsx")