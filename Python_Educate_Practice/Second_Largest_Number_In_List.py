# Implement a function find_second_maximum(lst) which returns the second largest element in the list.

def find_second_maximum(lst):
    if len(lst) <= 0:
        return None
    else:
        lst.sort()
        return lst[-2]

my_list = [9,2,3,6]
print(find_second_maximum(my_list))

# OR.

def find_second_maximum(lst):
    if len(lst) <= 0:
        return None
    else:
        max = second_max = 0
        for i in lst:
            if i > max:
                max = i
        
        for j in lst:
            if j != max and j > second_max:
                second_max = j
        return second_max


my_list = [9,2,3,6]
print(find_second_maximum(my_list))

