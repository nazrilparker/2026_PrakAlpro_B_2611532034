# Name: Muhammad Nazril Fandhi
# NIM: 2611532034
# Question 7

name = "muhammad nazril fandhi"
nim = "2611532034"

clean = name.strip()
space = clean.find(" ")

if space == -1:
    first_name = clean
else:
    first_name = clean[:space]

username = first_name.lower() + nim[-3:]

print(username)

intake = "20" + nim [:2]

print("=" * 30)
print("STUDENT CARD" .center(30))
print ("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)