# Implement a function findMinimum(lst) which finds the smallest number in the given list.

def find_minimum(lst):
    if (len(lst) <= 0):
        return None
    lst.sort()  # sort list
    return lst[0]  # return first element


print(find_minimum([9, 2, 3, 6]))

# OR. Iterate over the list

def find_minimum(lst):
    if (len(lst) <= 0):
        return None
    minimum = lst[0]
    for ele in lst:
        # update if found a smaller element
        if ele < minimum:
            minimum = ele
    return minimum


print(find_minimum([9, 2, 3, 6]))