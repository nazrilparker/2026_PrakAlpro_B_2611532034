# Buatlah file dengan nama bitwise_2611533002.py
# Nama variable ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator bitwise dalam Python

print("\n==================================")
print("3. OPERATOR BITWISE")
print("==================================")

angka1_2034 = int(input("Masukkan angka bitwise-1: "))
angka2_2034 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner:")
print("Angka 1:", angka1_2034, "-| biner", bin(angka1_2034))
print("Angka 2:", angka2_2034, "-| biner", bin(angka2_2034))

# Bitwise AND
hasil_2034 = angka1_2034 & angka2_2034
print("\nBitwise AND (&)")
print(angka1_2034, "&", angka2_2034, "=", hasil_2034)
print("Biner hasil =", bin(hasil_2034))
print("Biner hasil (8 bit) =", format(hasil_2034, '08b'))

# Bitwise OR
hasil_2034 = angka1_2034 | angka2_2034
print("\nBitwise OR (|)")
print(angka1_2034, "|", angka2_2034, "=", hasil_2034)
print("Biner hasil =", bin(hasil_2034))
print("Biner hasil (8 bit) =", format(hasil_2034, '08b'))

# Bitwise XOR
hasil_2034 = angka1_2034 ^ angka2_2034
print("\nBitwise XOR (^)")
print(angka1_2034, "^", angka2_2034, "=", hasil_2034)
print("Biner hasil =", bin(hasil_2034))
print("Biner hasil (8 bit) =", format(hasil_2034, '08b'))

# Bitwise NOT
hasil_2034 = ~angka1_2034
print("\nBitwise NOT (~)")
print("~", angka1_2034, "=", hasil_2034)
print("Biner hasil =", bin(hasil_2034))
print("Biner hasil (8 bit) =", format(hasil_2034, '08b'))

# Bitwise geser kiri
jumlah_geser_2034 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_2034 = angka1_2034 << jumlah_geser_2034
print("\nBitwise Geser Kiri (<<)")
print(angka1_2034, "<<", jumlah_geser_2034, "=", hasil_2034)
print("Biner hasil =", bin(hasil_2034))
print("Biner hasil (8 bit) =", format(hasil_2034, '08b'))

# Bitwise geser kanan
hasil_2034 = angka1_2034 >> jumlah_geser_2034
print("\nBitwise Geser Kanan (>>)")
print(angka1_2034, ">>", jumlah_geser_2034, "=", hasil_2034)
print("Biner hasil =", bin(hasil_2034))
print("Biner hasil (8 bit) =", format(hasil_2034, '08b'))