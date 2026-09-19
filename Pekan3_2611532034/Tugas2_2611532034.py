print("=== SISTEM TRANSAKSI TOKO ===")
print(" ")
print(" ")

# INPUT DATA PELANGGAN
nama_2034 = input("Masukkan Nama Pelanggan : ")
print(" ")
status_2034 = input("Masukkan Status Pelanggan (member/nonmember) : ")
print(" ")
total_belanja_2034 = float(input("Masukkan Total Belanja : Rp"))
print(" ")
jumlah_barang_2034 = int(input("Masukkan Jumlah Barang : "))
print(" ")
kode_promo_2034 = input("Masukkan Kode Promo : ")

# OPERATOR PERBANDINGAN
syarat_belanja_2034 = total_belanja_2034 >= 200000
syarat_barang_2034 = jumlah_barang_2034 >= 3
status_member_2034 = status_2034 == "member"

# DAFTAR KODE PROMO
daftar_promo_2034 = ["HEMAT10", "MURAH10", "HAPPYSHOP"]

# OPERATOR KEANGGOTAAN
promo_tersedia_2034 = kode_promo_2034 in daftar_promo_2034
promo_tidak_tersedia_2034 = kode_promo_2034 not in daftar_promo_2034

# OPERATOR LOGIKA 
diskon_member_2034 = status_member_2034 and syarat_belanja_2034

promo_didapatkan_2034 = promo_tersedia_2034 and (syarat_belanja_2034 or syarat_barang_2034)

bukan_member_2034 = not status_member_2034

# OPERATOR ARITMATIKA
if diskon_member_2034:
    persentase_diskon_2034 = 0.10
else:
    persentase_diskon_2034 = 0.05 if syarat_belanja_2034 else 0

besar_diskon_2034 = total_belanja_2034 * persentase_diskon_2034

total_pembayaran_2034 = total_belanja_2034 - besar_diskon_2034

if jumlah_barang_2034 > 0:
    rata_rata_barang_2034 = total_belanja_2034 / jumlah_barang_2034
else:
    rata_rata_barang_2034 = 0

sisa_pembagian_2034 = int(total_belanja_2034) % jumlah_barang_2034 if jumlah_barang_2034 > 0 else 0

# OPERATOR PENUGASAN
poin_2034 = 0
if status_member_2034:
    poin_2034 += int(total_pembayaran_2034 // 10000)

jumlah_barang_tersisa_2034 = jumlah_barang_2034
if promo_didapatkan_2034:
    jumlah_barang_tersisa_2034 -= 1

# OPERATOR IDENTITY (IDENTITAS)
kode_1_2034 = ["HEMAT10"]
kode_2_2034 = ["MURAH10"]

nilai_sama_2034 = kode_1_2034 == kode_2_2034
objek_sama_2034 = kode_1_2034 is kode_2_2034
objek_berbeda_2034 = kode_1_2034 is not kode_2_2034

# OPERATOR BITWISE
kode_member_2034 = 1 if status_member_2034 else 0
kode_belanja_2034 = 2 if syarat_belanja_2034 else 0
kode_barang_2034 = 4 if syarat_barang_2034 else 0
kode_promo_2034 = 8 if promo_tersedia_2034 else 0

kode_status_2034 = (
    kode_member_2034
    | kode_belanja_2034
    | kode_barang_2034
    | kode_promo_2034
)

cek_member_2034 = kode_status_2034 & 1
cek_belanja_2034 = kode_status_2034 & 2
cek_barang_2034 = kode_status_2034 & 4
cek_promo_2034 = kode_status_2034 & 8

kode_referensi_2034 = 11
perbandingan_status_2034 = kode_status_2034 ^ kode_referensi_2034

kode_shift_2034 = kode_status_2034 << 1


member_access_2034 = bool(cek_member_2034)
promo_access_2034 = bool(cek_promo_2034)
free_shipping_access_2034 = syarat_belanja_2034 and syarat_barang_2034

# OUTPUT
print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan       : ", nama_2034)
print(" ")
print("Status Pelanggan     : ", status_2034)
print(" ")
print("Total Belanja        : Rp", total_belanja_2034)
print(" ")
print("Jumlah Barang        : ", jumlah_barang_2034)
print(" ")
print("Kode Promo           : ", kode_promo_2034)
print(" ")

print("\n=== HASIL VALIDASI ===")
print(" ")
print("Belanja >= Rp200000  :", syarat_belanja_2034)
print(" ")
print("Jumlah Barang >= 3   :", syarat_barang_2034)
print(" ")
print("Status Member        :", status_member_2034)
print(" ")
print("Kode Promo Tersedia  :", promo_tersedia_2034)
print(" ")
print("Mendapatkan Diskon   :", diskon_member_2034)
print(" ")
print("Mendapatkan Promo    :", promo_didapatkan_2034)
print(" ")

print("\n=== HASIL PERHITUNGAN ===")
print(" ")
print("Besarnya Diskon      : Rp", besar_diskon_2034)
print(" ")
print("Total Pembayaran     : Rp", total_pembayaran_2034)
print(" ")
print("Rata-rata Harga      : Rp", rata_rata_barang_2034)
print(" ")
print("Sisa Pembagian       :", sisa_pembagian_2034)
print(" ")

print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses       :", format(kode_status_2034, "04b"))
print("Member Access        :", member_access_2034)
print("Promo Access         :", promo_access_2034)
print("Free Shipping Access :", free_shipping_access_2034)
print("Poin Pelanggan       :", poin_2034)

print("\n=== OPERATOR IDENTITAS ===")
print("kode_1 == kode_2     :", nilai_sama_2034)
print("kode_1 is kode_2     :", objek_sama_2034)
print("kode_1 is not kode_2 :", objek_berbeda_2034)

print("\n=== OPERASI BITWISE ===")
print("Kode Status Transaksi")
print("0001 | 0010 | 0100 | 1000")

print("Kode Biner           :", format(kode_status_2034, "04b"))
print("Kode Desimal         :", kode_status_2034)

print("\n=== PEMERIKSAAN STATUS ===")

print("\nCek Member")
print(format(kode_status_2034, "04b"), "& 0001")
print("Hasil Biner         :", format(cek_member_2034, "04b"))
print("Hasil Desimal       :", cek_member_2034)

print("\nCek Belanja")
print(format(kode_status_2034, "04b"), "& 0010")
print("Hasil Biner         :", format(cek_belanja_2034, "04b"))
print("Hasil Desimal       :", cek_belanja_2034)

print("\nCek Jumlah Barang")
print(format(kode_status_2034, "04b"), "& 0100")
print("Hasil Biner         :", format(cek_barang_2034, "04b"))
print("Hasil Desimal       :", cek_barang_2034)

print("\nCek Promo")
print(format(kode_status_2034, "04b"), "& 1000")
print("Hasil Biner         :", format(cek_promo_2034, "04b"))
print("Hasil Desimal       :", cek_promo_2034)

print("\n=== PERBANDINGAN STATUS (XOR) ===")
print("Kode Transaksi   :", format(kode_status_2034, "04b"))
print("Kode Referensi      :", format(kode_referensi_2034, "04b"))
print(format(kode_status_2034, "04b"), "^",
    format(kode_referensi_2034, "04b"))
print("Hasil Biner         :", format(perbandingan_status_2034, "04b"))
print("Hasil Desimal       :", perbandingan_status_2034)

print("\n=== SHIFT ===")
print(format(kode_status_2034, "04b"), "<< 1")
print("Hasil Biner         :", format(kode_shift_2034, "b"))
print("Hasil Desimal       :", kode_shift_2034)
print(" ")
print(" ")

print("=== SELESAI ===")