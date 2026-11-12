# Name: Muhammad Nazril Fandhi
# NIM: 2611532034
# Question 6

# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().
full_name = " Muhammad Nazril Fandhi "
nim = "261****034"

clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first_name = clean
else:
    first_name = clean[:space]

username = first_name.lower() + nim[-3:]

print(username)