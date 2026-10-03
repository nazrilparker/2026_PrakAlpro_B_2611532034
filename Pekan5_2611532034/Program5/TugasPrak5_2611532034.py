# Buatlah program untuk menampilkan pola bintang

tinggi_2034 = int(input("Masukkan tinggi segitiga: "))

for i_2034 in range(1, tinggi_2034 + 1):
    print(" " * (tinggi_2034 - i_2034), end="")

    for j_2034 in range(i_2034):
        print("*", end=" ")
    print()