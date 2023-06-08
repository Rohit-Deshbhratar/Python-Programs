# In this program we are going to apply a formula on cell and selecting range of cells.
# Make sure that cell must be empty (i.e. cell do nit contain any formula) 
# in worksheet refer line number 8, 9, 12.

from openpyxl import *

# Load workbook, select worksheet
wb = load_workbook("sample.xlsx")
sheet = wb["Formula"]

# Select row and column to display output of formula
sum = sheet.cell(row=12, column=3)

# Selecting range and applyong formula on that range.
sum.value = "=SUM(B5:B11)"

# Save workbook
wb.save("sample.xlsx")