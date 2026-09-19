# Buatlah file dengan nama lainnya_2611532034.py
# Nama variable ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas dalam Python

print("==================================")
print("1. OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2034 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
input_data_2034 = [int(angka.strip()) for angka in input_data_2034.split(",")]

nilai_dicari_2034 = int(input("Masukkan angka yang ingin dicari: "))

# Operator In
hasil_2034 = nilai_dicari_2034 in input_data_2034
print("\nOperator keanggotaan IN")
print(nilai_dicari_2034, "in", input_data_2034, "=", hasil_2034)

# Operator Not In
hasil_2034 = nilai_dicari_2034 not in input_data_2034
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2034, "not in", input_data_2034, "=", hasil_2034)

print("\n==================================")
print("2. OPERATOR IDENTITAS")
print("==================================")

# objek1 menggunakan list dari input pengguna
objek1_2034 = input_data_2034

# objek2 menggunakan list dari input pengguna
objek2_2034 = objek1_2034

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_2034 = input_data_2034.copy()

print("objek1_2034 =", objek1_2034)
print("objek2_2034 =", objek2_2034)
print("objek3_2034 =", objek3_2034)

# Operator Is
hasil_2034 = objek1_2034 is objek2_2034
print("\nOperator identitas IS")
print("objek1_2034 is objek2_2034 =", hasil_2034)

# Operator Is Not
hasil_2034 = objek1_2034 is not objek3_2034
print("\nOperator identitas IS NOT")
print("objek1_2034 is not objek3_2034 =", hasil_2034)

# Membandingkan identitas dan nilai
print("\nMembandingkan identitas dan nilai:")
print("objek1_2034 is objek3_2034 =", objek1_2034 is objek3_2034)
print("objek1_2034 == objek3_2034 =", objek1_2034 == objek3_2034)