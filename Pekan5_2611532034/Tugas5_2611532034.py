print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

n_2034 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Batas Atas

print("#", end="")

for garis_2034 in range(4 * n_2034 + 5):
    print("=", end="")

print("#")

# Fase 1: Jam Pasir Atas

for baris_2034 in range(n_2034, 0, -1):

    print("| ", end="")

    # Spasi penyeimbang kiri
    for spasi_2034 in range(2 * (n_2034 - baris_2034)):
        print(" ", end="")

    # Deret angka menurun
    for angka_2034 in range(baris_2034, 0, -1):
        print(angka_2034, end=" ")

    # Poros kristal
    print("<*>", end="")

    # Deret angka menaik
    print(" ", end="")
    for angka_2034 in range(1, baris_2034 + 1):
        print(angka_2034, end=" ")

    # Spasi penyeimbang kanan
    for spasi_kanan_2034 in range(2 * (n_2034 - baris_2034)):
        print(" ", end="")

    print("|")

# Fase 2: Poros Titik Pusat Jam Pasir

print("|", end="")

for spasi_tengah_2034 in range(2 * n_2034 + 1):
    print(" ", end="")

print("<*>", end="")

for spasi_tengah_kanan_2034 in range(2 * n_2034 + 1):
    print(" ", end="")

print("|")

# Fase 3: Jam Pasir Bawah

for baris_bawah_2034 in range(1, n_2034 + 1):

    print("| ", end="")

    # Spasi penyeimbang kiri
    for spasi_bawah_2034 in range(2 * (n_2034 - baris_bawah_2034)):
        print(" ", end="")

    # Deret angka menurun
    for angka_bawah_2034 in range(baris_bawah_2034, 0, -1):
        print(angka_bawah_2034, end=" ")

    # Poros kristal
    print("<*>", end="")

    # Deret angka menaik
    print(" ", end="")
    for angka_naik_2034 in range(1, baris_bawah_2034 + 1):
        print(angka_naik_2034, end=" ")

    # Spasi penyeimbang kanan
    for spasi_kanan_bawah_2034 in range(2 * (n_2034 - baris_bawah_2034)):
        print(" ", end="")

    print("|")

# Batas Bawah

print("#", end="")

for garis_bawah_2034 in range(4 * n_2034 + 5):
    print("=", end="")

print("#")