# Accept marks of 5 subject each. Maximum marks are 100.

print("Please enter marks of 5 subject to find division of a student.")

total = marks = 0
count = 5

while count >= 1:
    marks = int(input("Please enter marks: "))
    if marks > 100:
        print(f"Oh... maximum marks are 100. You entered {marks}. Exiting...")
        break
    else:
        total = marks + total
        count -= 1
print(f"Your total score out of 500 is {total}")

percent = (total / 500) * 100

if percent >= 75:
    print("Distinction.")
elif (percent >= 60 and percent <= 74.99):
    print("First Class.")
elif (percent >= 45 and percent <= 59.99):
    print("Second Class.")
elif (percent >= 35 and percent <= 44.99):
    print("Third Class.")
else:
    print("FAIL.")