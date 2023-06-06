# In this program we are going to create a sheet in a workbook.

from openpyxl import *

# Load workbook
wb = load_workbook("sample.xlsx")

# Creating new sheet
wb.create_sheet(index=3, title="Student")

# Saving workbook
wb.save("sample.xlsx")