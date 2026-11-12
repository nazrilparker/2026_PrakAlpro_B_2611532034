# Name: Muhammad Nazril Fandhi
# NIM: 2611532034
# Question 3

#bagian a
text = "Informatika"
print(text[10])
text = text.upper()
print(len(text))
print(text[0:11])

#bagian b
text = "Muhammad Nazril Fandhi"
text = text.lower()
count = 0
for char in text:
    if char in "aiueo":
        count += 1
print("Vowels:", count)
