# def remove_consecutive_duplicates(input_string):
#     result = []
#     prev_char = None

#     for char in input_string:
#         if char != prev_char:
#             result.append(char)
#             prev_char = char

#     return ''.join(result)

# # Example string
# text = "aaabbbcccdddeee"

# new_text = remove_consecutive_duplicates(text)
# print("String with consecutive duplicates removed:", new_text)

from sys import stdin


# def removeConsecutiveDuplicates(str) :
#     #Your code goes here.
#     output = []
#     prev_char = None

#     for cur_char in str:
#         if cur_char != prev_char:
#             output.append(cur_char)
#             prev_char = cur_char
    
#     return ''.join(output)


# #main
# string = stdin.readline().strip()

# ans = removeConsecutiveDuplicates(string)

#print(ans)
