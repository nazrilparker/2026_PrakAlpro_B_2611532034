# Buat file dengan nama nested_for2_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2034 = int(input("Masukkan nilai batas: "))
for i in range(1, batas_2034 + 1):
    for j in range(1, batas_2034 + 1):
        print("*", end=" ")
    print() # pindah ke baris berikutnya 