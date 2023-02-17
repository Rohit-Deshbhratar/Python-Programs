# Write a program to accept the marks of 6 students and display them in a sorted manner.

marks = []

for i in range(6):
    acceptMarks = int(input("Enter marks: "))
    marks.append(acceptMarks)
    marks.sort()

print(f"Sorted Marks: {marks}")
