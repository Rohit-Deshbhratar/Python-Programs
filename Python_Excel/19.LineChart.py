# # In this program we are going to add bar chart on provided data.
# # Make sure that the excel sheet must be empty before runnung the program.

from openpyxl import *
from openpyxl.chart import LineChart, Reference

# # Load workbook, select worksheet
wb = load_workbook("sample.xlsx")
sheet = wb["Line Chart"]

# # Create data for bar chart
data = [["Product", "Online", "Store"],
        [1, 30, 45],
        [2, 40, 30],
        [3, 40, 25],
        [4, 50, 30],
        [5, 30, 25],
        [6, 25, 35],
        [7, 15, 40]]

# # Add data to excel sheet using loop
for i in data:
    sheet.append(i)

# # Create object of class BarChart
chart = LineChart()

# # Create parameterized object of class Reference 
chartData = Reference(worksheet=sheet,
                      min_row=1,
                      min_col=2,
                      max_row=8,
                      max_col=3)

# # Add all data
chart.add_data(chartData, titles_from_data=True)

# # Add chart to excel sheet by giving anchor i.e. place where chart is placed
sheet.add_chart(chart, "E2")

# # Save workbook
wb.save("sample.xlsx")