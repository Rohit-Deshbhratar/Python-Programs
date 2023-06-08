# In this program we are going to add logo in excel sheet
# Make sure that worksheet "Logo" should be blank before running this program.

from openpyxl import *
from openpyxl.drawing.image import Image

# Load workbook, select worksheet, pass the path of image.
wb = load_workbook("sample.xlsx")
sheet = wb['Logo']
logo = Image('google_logo.png')

# Set height and width of image
logo.height = 150
logo.width = 150

# Add image to the worksheet
sheet.add_image(logo, "E10")

# Save workbook
wb.save("sample.xlsx")