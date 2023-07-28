# Implement a function that removes all the even elements from a given list. Name it remove_even(lst).


def remove_even(lst):
    odd_list = []
    for i in lst:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_even(my_list)
print(result)

# OR. Using LIST comprehension

def remove_even(lst):
    # List comprehension to iter aover List and add to new list if not even
    return [number for number in lst if number % 2 != 0]

print(remove_even([3, 2, 41, 3, 34]))