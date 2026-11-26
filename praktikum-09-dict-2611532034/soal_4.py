absen_kelas = input().split()
pengumpulan = input().split()

set_absen_kelas = set(absen_kelas)
set_pengumpulan = set(pengumpulan) 

belum_ngumpul = set_absen_kelas - set_pengumpulan

print(f"Submitted: {len(set_pengumpulan)} students")
print(f"Not submitted: {len(belum_ngumpul)} students")

for nomor in absen_kelas:
    if nomor not in set_pengumpulan:
        print(nomor)