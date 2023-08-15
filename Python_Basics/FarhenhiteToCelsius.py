import math 
s = int(input())
e = int(input())
w = int(input())
# °C = (°F - 32) × 5/9
for i in range(s, e+1, w):
    # print(i)
    c = (i-32)*5/9
    print(i,"\t",math.trunc(c))
