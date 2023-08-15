# Convert integer to binary and count number of ones in it

def int_to_binary(num):
    binary = bin(num)[2:]
    count = 0

    for i in binary:
        if i=='1':
            count+=1
    return count

n = int(input())
print(int_to_binary(n))