# Count total number prime within the range

def prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num%2==0 and num%3==0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 and num % (i + 2) == 0:
            return False
        i += 6
    return True

def totalPrime(start, end):
    count = 0

    for i in range(start, end + 1):
        if prime(i):
            count+=1
    return count
    
#Taking S and E space seperated input.
S,E = map(int,input().split(' '))
print(totalPrime(S,E))