""""
Print following pattern
    *
   **
  ***
 ****
*****
"""

rows = int(input("Please enter number of rows: "))

for i in range(0, rows):
    for j in range(0, rows - i):
        print(" ", end="")
    for k in range(0, i + 1):
        print("*",end="")
    print("")
