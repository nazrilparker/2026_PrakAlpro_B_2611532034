print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# 1. Input Data Pengunjung

nama_pengunjung_2034 = input("Masukkan Nama Pengunjung            : ")
umur_2034 = int(input("Input Umur Anda                     : "))
sim_2034 = input("Apakah Anda Sudah Punya SIM C (y/t) : ").strip().lower()

# 2. Pemilihan Wahana Menggunakan match-case

print("\nPilihan Paket Wahana (1-5):")
print(" 1. Safari Rimba         (Rp 50,000)")
print(" 2. Arung Jeram          (Rp 75,000)")
print(" 3. Motor ATV Ekstrim    (Rp 120,000)")
print(" 4. Roller Coaster Kilat (Rp 100,000)")
print(" 5. All-Access VIP       (Rp 220,000)")

paket_2034 = int(input("Masukkan nomor paket(1-5)      : "))
match paket_2034:
    case 1:
        nama_wahana_2034 = "Wahana Safari Rimba"
        harga_satuan_2034 = 50000
    case 2:
        nama_wahana_2034 = "Wahana Arung Jeram"
        harga_satuan_2034 = 75000
    case 3:
        nama_wahana_2034 = "Wahana Motor ATV Ekstrim"
        harga_satuan_2034 = 120000
    case 4:
        nama_wahana_2034 = "Wahana Roller Coaster Kilat"
        harga_satuan_2034 = 100000
    case 5:
        nama_wahana_2034 = "Wahana All-Access VIP"
        harga_satuan_2034 = 220000
    case _:
        print("Paket tidak valid")
        raise SystemExit

jumlah_tiket_2034 = int(input("Masukkan jumlah tiket          : "))
if jumlah_tiket_2034 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")

member_2034 = input("Apakah anda member? (y/t)      : ").strip().lower()
is_member_2034 = member_2034 in ["y","ya","yes"]

promo_2034 = input("Apakah kode promo valid? (y/t) : ").strip().lower()
kode_promo_valid_2034 = promo_2034 in ["y","ya","yes"]

# 3. Validasi Izin Kendali Wahana Menggunakan if - elif - else dan Operator Logika (and, !=)

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_2034 == 3 and umur_2034 >= 17 and sim_2034 == 'y':
    status_akses_2034 = "Anda sudah dewasa dan boleh mengendarai ATV sendiri."
elif paket_2034 == 3 and umur_2034 >= 17 and sim_2034 != 'y':
    status_akses_2034 = "Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)."
elif paket_2034 == 3 and umur_2034 < 17 and sim_2034 == 'y':
    status_akses_2034 = "Identitas tidak valid: Belum cukup umur memiliki SIM"
else:
    status_akses_2034 = "Anda belum cukup umur dan tidak boleh bawa motor ATV"

print(f"Status Akses: {status_akses_2034}")

# 4. Akumulasi Diskon Bertingkat Menggunakan Multi-IF Terpisah

subtotal_2034 = harga_satuan_2034 * jumlah_tiket_2034

total_diskon_persen_2034 = 0

# Diskon belanja besar
if subtotal_2034 >= 200000:
   total_diskon_persen_2034 += 10

# Diskon member
if is_member_2034:
   total_diskon_persen_2034 += 5

# Diskon voucher promo
if kode_promo_valid_2034:
   total_diskon_persen_2034 += 15

# Diskon tambahan rombongan
if jumlah_tiket_2034 >= 5:
   total_diskon_persen_2034 += 5

# 5. Evaluasi Kelulusan Audit Menggunakan if - else

# Perhitungan nominal diskon dan total bayar
nominal_diskon_2034 = subtotal_2034 * (total_diskon_persen_2034 / 100)

total_bayar_2034 = subtotal_2034 - nominal_diskon_2034

# Evaluasi total bayar
if total_bayar_2034 > 300000:
    catatan_layanan_2034 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_2034 = "Terima kasih telah berkunjung."

# 6. Rincian Pembayaran dengan f-string format desimal (:,.0f).

print("\n--- RINCIAN PEMBAYARAN ---")
print(f"Nama Pengunjung   : {nama_pengunjung_2034}")
print(f"Wahana            : {nama_wahana_2034}")
print(f"Harga Satuan      : Rp{harga_satuan_2034:,.0f}")
print(f"Jumlah Tiket      : {jumlah_tiket_2034}")
print(f"Subtotal Belanja  : Rp{subtotal_2034:,.0f}")
print(f"Total Diskon      : {total_diskon_persen_2034}% " f"(Rp{nominal_diskon_2034:,.0f})")
print(f"Total Bayar       : Rp{total_bayar_2034:,.0f}")
print(f"Catatan Layanan   : {catatan_layanan_2034}")

print("\nProgram Selesai")