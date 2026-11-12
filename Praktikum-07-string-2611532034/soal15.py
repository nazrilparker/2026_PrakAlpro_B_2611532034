# Name: Muhammad Nazril Fandhi
# NIM: 2611532034
# Question 5

username = input("Username: ")
 
# Check the rules in a safe order and print the first rule that fails.
# Messages:
#   "Invalid: at least 5 characters"
#   "Invalid: letters and digits only"
#   "Invalid: must start with a letter"
#   "Valid"

if len(username) < 5:            #memeriksa index apakah panjang username kurang dari 5 karakter
    print("Invalid: at least 5 characters")
elif not username.isalnum():     #memeriksa apakah username hanya terdiri dari huruf dan angka
    print("Invalid: letters and digits only")
elif not username[0].isalpha():  #memeriksa apakah index pertama username dimulai dengan huruf
    print("Invalid: must start with a letter")
else:
    print("Valid")