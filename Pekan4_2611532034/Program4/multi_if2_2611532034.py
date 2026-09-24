# Buat file dengan nama multi_if2_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: total_belanja_1234
# Program ini menggunakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_2034 = float(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_2034 = input("Apakah anda meber? (y/t): ").strip().lower()
is_member_2034 = input_member_2034 in ["y","ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_2034 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_2034 = input_promo_2034 in ["ya","ya"]

total_diskon_persen_2034 = 0

# Multi-IF terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_2034 > 1000000:
    total_diskon_persen_2034 += 10 # Diskon belanja besar

if is_member_2034:
    total_diskon_persen_2034 += 5 # Diskon member

if kode_promo_valid_2034:
    total_diskon_persen_2034 += 15 # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_2034 = total_belanja_2034 * (total_diskon_persen_2034 / 100)
total_bayar_2034 = total_belanja_2034 - nominal_diskon_2034

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_2034}% (Rp {nominal_diskon_2034:,.0f})")
print(f"Total Bayar : Rp {total_bayar_2034:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_2034}%")
# Output: Total diskon yang anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promosi valid