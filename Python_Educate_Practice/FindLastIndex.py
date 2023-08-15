def last_occurance(num_list, num_find):
    index = -1
    for i in range(len(num_list)):
        if num_list[i] == x:
            index = i
    return index

size = int(input())
numbers = list(map(int, input().split()))
x = int(input())

print(last_occurance(numbers, x))