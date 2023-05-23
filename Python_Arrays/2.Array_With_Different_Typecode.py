# Arrays with different typecode

import array

# Typecode = "b"
signed_char = array.array("b", [0,1,2,5,7])
print(f"Typecode 'b': {signed_char}")

# Typecode = "B"
unsigned_char = array.array("B", [4,10,23,95,79])
print(f"Typecode 'B': {unsigned_char}")

# Typecode = "u"
unicode_char = array.array("u", ["\u0048", "\u0065", "\u006C", "\u006C", "\u006F"])
print(f"Typecode 'B': {unicode_char}")

# Typecode = "h"
signed_short = array.array("h", [-5, 8, 93])
print(f"Typecode 'h': {signed_short}")

# Typecode = "h\H"
signed_short = array.array("H", [41, 12, 87])
print(f"Typecode 'H': {signed_short}")

# Typecode = "i"
signed_int = array.array("i", [10, -79, -126, 47])
print(f"Typecode 'i': {signed_int}")

# Typecode = "I"
unsigned_int = array.array("I", [35, 20, 45])
print(f"Typecode 'I': {unsigned_int}")

# Typecode = "l"
signed_long = array.array("l", [-50479, 88410, 10093])
print(f"Typecode 'l': {signed_long}")

# Typecode = "L"
unsigned_long = array.array("L", [554698, 8208, 948623])
print(f"Typecode 'L': {unsigned_long}")

# Typecode = "q"
signed_long_long = array.array("q", [7841339500, -1396478502, -20136479651])
print(f"Typecode 'q': {signed_long_long}")

# Typecode = "Q"
unsigned_long_long = array.array("Q", [1201547932, 3021479631455, 201489317])
print(f"Typecode 'Q': {unsigned_long_long}")

# Typecode = "f"
float_arr = array.array("f", [4.1, 0.9, 9.87, 11.0])
print(f"Typecode 'f': {float_arr}")

# Typecode = "d"
double_arr = array.array("d", [79.459, 14.153, 99.99])
print(f"Typecode 'd': {double_arr}")
