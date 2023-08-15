def find_first_occurrence(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Take size
size = int(input())

# Taking user input for array
arr = list(map(int, input().split()))

# Taking user input for element to find
x = int(input())

print(find_first_occurrence(arr, x))
# index = find_first_occurrence(arr, x)
# if index != -1:
#     print(index)
# # else:
# #     print(-1)