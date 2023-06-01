# In this program we are creating excel file at runtime on a specified location.
# Before running this program make sure that "Runtime-Excel.xlsx" file should be deleted. 

from openpyxl import *

wb = Workbook()
filepath = "D:/Python-Programs/Python_Excel/Runtime-Excel.xlsx"
wb.save(filepath)