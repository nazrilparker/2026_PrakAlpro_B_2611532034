kalimat = input("Masukkan kalimat: ")

clean = kalimat.lower().replace(" ", "")

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")