import array

size = int(input())
numbers = array.array("i", map(int, input().split()))

start = 0
end = len(numbers) - 1

while start<end:
    numbers[start], numbers[end] = numbers[end], numbers[start]
    start+=1
    end+=-1

#numbers.reverse()
for i in numbers:
    print(i, end=" ")

