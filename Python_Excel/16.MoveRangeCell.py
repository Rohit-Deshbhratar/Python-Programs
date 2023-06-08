# In this program we are going to move cell to other locations in same worksheet.
# Make sure that the data must be in cell "H4:I7".
# Change "rows=" and "cols=" values to see the changes of range.
# Positive values in "rows=" moves down, and in "cols=" move right.
# Simillarly negative values in "rows=" move cells up, and in "cols=" move left.

from openpyxl import *

# Load workbook, select worksheet
wb = load_workbook("sample.xlsx")
sheet = wb["Move Range"]

# Select range to move data, specify new location using "rows=", "cols="
sheet.move_range("H4:I7", rows=6, cols=4)
# Save workbook
wb.save("sample.xlsx")