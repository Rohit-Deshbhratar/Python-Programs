# Rename the existing sheet in excel file.
# In this program we are going to rename sheet "DEPT" to "Department".

from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")

sheet = wb["DEPT"]
print(f"Sheet to be renamed: {sheet}")
# Renaming thr sheet
sheet.title = "Department"
print(f"Sheet after rename: {sheet}")
# Save workbook
wb.save("sample.xlsx")