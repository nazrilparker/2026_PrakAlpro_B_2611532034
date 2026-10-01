# Buat file dengan nama perulangan_for2_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2034 = int(input("Masukkan jumlah perulangan: "))
print("perulangan ke-0 sampai ke-", ulang_2034-1)
for i in range(ulang_2034):
    print(i, end=" ")
print()
print("perulangan ke-1 sampai ke-", ulang_2034)
for i in range(1, ulang_2034+1):
    print(i, end=" ")