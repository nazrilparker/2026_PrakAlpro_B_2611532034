number_of_rows = 4
seats_per_row = 5
#write your code below

# Membuat denah kursi
seats = [["."] * seats_per_row for _ in range(number_of_rows)]

seats_taken = 0

while True:
    # Menampilkan denah
    for i in range(number_of_rows):
        print(f"Row {i + 1}:", *seats[i])

    row = int(input("Row (0 to stop): "))

    if row == 0:
        break

    if row < 1 or row > number_of_rows:
        print("Invalid seat.")
        continue

    seat = int(input("Seat: "))

    if seat < 1 or seat > seats_per_row:
        print("Invalid seat.")
    elif seats[row - 1][seat - 1] == "X":
        print("Seat already taken.")
    else:
        seats[row - 1][seat - 1] = "X"
        seats_taken += 1
        print("Seat booked.")

print("Seats taken:", seats_taken)
