n = int(input())

even = 0
odd = 0
while n>0:
    num=n%10
    if num%2==0:
        even+=num
    else:
        odd+=num
    n//=10
print(even, odd)