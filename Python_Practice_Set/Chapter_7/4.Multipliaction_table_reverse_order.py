# Multiplucation table in reverse order using for loop

table = int(input("Please enter number for multiplication table: "))
stop = int(input("Please enter where to stop: "))

for i in range(stop, 0, -1):
    print(f"{table} * {i} = {table * i}")