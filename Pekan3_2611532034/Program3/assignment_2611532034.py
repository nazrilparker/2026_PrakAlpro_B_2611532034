# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input ()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_2034 = int(input("Masukkan angka-1: "))
angka2_2034 = int(input("Masukkan angka-2: "))

print("\nNilai awal angka1_2034 =", angka1_2034)
print("Nilai awal angka2_2034 =", angka2_2034)

# Assignment biasa
hasil = angka1_2034
print("\nAssignment biasa (=)")
print("Hasil =", hasil)

# Assignment penambahan
hasil = angka1_2034
hasil += angka2_2034
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil)

# Assignment pengurangan
hasil = angka1_2034
hasil -= angka2_2034
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil)

# Assignment perkalian
hasil = angka1_2034
hasil *= angka2_2034
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2034 != 0:
    hasil = angka1_2034
    hasil /= angka2_2034
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil)

    #Operator tambahan
    hasil = angka1_2034
    hasil //= angka1_2034
    print("\nAssignment pembagian bulat (//=)")
    print("hasil =", angka1_2034)
    hasil = angka1_2034
    hasil %= angka2_2034
    print("\nAssignment sisa bagi (%=)")
    print ("hasil =", hasil)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0")

# Operator tambahan: assignment perpangkatan
hasil = angka1_2034
hasil **= angka2_2034
print("\nAssignment perpangkatan (**=)")
print("hasil =", hasil)