def print_all_substrings(input_string):
    n = len(input_string)
    for start in range(n):
        for end in range(start + 1, n + 1):
            substring = input_string[start:end]
            print(substring)

# Example string
text = "abcd"

print("All possible substrings:")
print_all_substrings(text)
