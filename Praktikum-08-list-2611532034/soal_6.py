LAST_DIGIT = 4 # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
#Write your code below

total = 0

for day in range(1, 8):
    expense = int(input(f"Day {day}: "))
    expenses.append(expense)
    total += expense

average = total / 7

highest = expenses[0]
highest_day = 1

for i in range(1, len(expenses)):
    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1

above_limit = 0

for expense in expenses:
    if expense > daily_limit:
        above_limit += 1

print("Daily limit:", daily_limit)
print("Total:", total)
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest})")
print("Days above limit:", above_limit)
