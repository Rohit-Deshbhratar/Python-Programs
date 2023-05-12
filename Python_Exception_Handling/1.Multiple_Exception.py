# Program for handling multiple exceptions
# Try to change the sequence of "except"
# Comment atleast one statement which is raising exception to see correct working of program.

try:
    print(x)

    x = 5
    y = 0
    z = x / y
    print(f"Division = {z}")
except NameError as ne:
    print(f"Exception occured: {ne}")
except ZeroDivisionError as zde:
    print(f"Exception occured: {zde}")
except Exception as e:
    print(f"An runtime error occured: {e}")
