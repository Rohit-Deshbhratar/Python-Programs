from typing import List
# def printDivisors(n: int) -> List[int]:
#     # Write your code here
#     divisors = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             divisors.append(i)
#             divisors.sort()
#     print(divisors)

def printDivisors(n: int) -> List[int]:
    ans = []
    for i in range(1, int(n**(0.5))+1):
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
    ans.sort()
    return ans

number = int(input())
print(printDivisors(number))