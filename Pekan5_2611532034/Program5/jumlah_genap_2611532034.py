# Buat file dengan nama jumlah_genap_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2034 = int(input("Masukkan nilai batas: "))

jumlah_2034 = 0
for i in range(1, ulang_2034 + 1):
    if i % 2 == 0:
        print(i, end=" ")
        jumlah_2034 = jumlah_2034 + i

        if i < ulang_2034:
            print(" + ", end=" ")
        else:
            print(" = ", jumlah_2034, end=" ")
print()
print("jumlah = ", jumlah_2034)