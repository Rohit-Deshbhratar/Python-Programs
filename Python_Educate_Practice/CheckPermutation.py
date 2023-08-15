def are_permutations(str1, str2):
    return sorted(str1) == sorted(str2)

# Example strings
string1 = "abcde"
string2 = "baedc"

if are_permutations(string1, string2):
    print("The strings are permutations of each other.")
else:
    print("The strings are not permutations of each other.")
