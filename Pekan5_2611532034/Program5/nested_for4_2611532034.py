# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2034 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2034 % 2 != 0:
    print("Tinggi pola harus bilangan genap!")
else:
    a_2034 = tinggi_2034
    c_2034 = a_2034
    lebar_2034 = (2 * tinggi_2034) - 2

    for i_2034 in range(1, tinggi_2034 + 1):
        b_2034 = c_2034 + 1

        for j_2034 in range(1, lebar_2034 + 1):

            # Baris atas dan bawah
            if i_2034 == 1 or i_2034 == tinggi_2034:
                if j_2034 == 1 or j_2034 == lebar_2034:
                    print("#", end="")
                else:
                    print("=", end="")
            # Baris isi
            else:
                if j_2034 == 1 or j_2034 == lebar_2034:
                    print("|", end="")
                else:
                    if j_2034 == c_2034:
                        print("<", end="")
                    elif j_2034 == b_2034:
                        print(">", end="")
                    elif j_2034 == (lebar_2034 - c_2034):
                        print("<", end="")
                    elif j_2034 == (lebar_2034 - c_2034 + 1):
                        print(">", end="")
                    elif j_2034 > b_2034 and j_2034 < (lebar_2034 - c_2034):
                        print(".", end="")
                    else:
                        print(" ", end="")
        print()

        # Logika asli Java
        a_2034 -= 2

        if a_2034 <= 0:
            c_2034 = (-a_2034) + 2
        else:
            c_2034 = a_2034