# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input ()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_2034 = int(input("Masukkan angka-1: "))
angka2_2034 = int(input("Masukkan angka-2: "))

# Lebih besar dari
hasil = angka1_2034 > angka2_2034
print("\nOperator lebih besar dari")
print("angka1_2034 > angka2_2034 =", hasil)

# Lebih kecil dari
hasil = angka1_2034 < angka2_2034
print("\nOperator lebih kecil dari")
print("angka1_2034 < angka2_2034 =", hasil)

# Lebih besar dari atau sama dengan
hasil = angka1_2034 >= angka2_2034
print("\nOperator lebih besar dari atau sama dengan")
print("angka1_2034 >= angka2_2034 =", hasil)

# Lebih kecil dari atau sama dengan
hasil = angka1_2034 <= angka2_2034
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1_2034 <= angka2_2034 =", hasil)

# Sama dengan
hasil = angka1_2034 == angka2_2034
print("\nOperator sama dengan")
print("angka1_2034 == angka2_2034 =", hasil)

# Tidak sama dengan
hasil = angka1_2034 != angka2_2034
print("\nOperator tidak sama dengan")
print("angka1_2034 != angka2_2034 =", hasil)

# Tambahan: perbandingan berantai dalam Python
hasil = 0 < angka1_2034 < 100
print("\nPerbandingan berantai")
print("0 < angka1_2034 < 100 =", hasil)

hasil = 0 < angka2_2034 < 100
print("0 < angka2_2034 < 100 =", hasil)
