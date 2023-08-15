import array

n = int(input())
numbers = array.array("i", map(int, input().split()))
k = int(input())

def rotate(num, x):
    if len(num) == 0:
        x = 0
    else:
        x = x % len(num)
    output = num[x:] + num[:x]
    for i in output:
        print(i, end=" ")
    
rotate(numbers, k)
#print(rotate(numbers, k))