n = int(input("Masukkan jumlah perulangan: "))
kas ={}

for i in range (n):
    nama, nominal = input().split()
    kas[nama] = kas.get(nama, 0) + int(nominal)

donatur = ""
terbesar = 0

for nama, total in kas.items():
    print(f"{nama}: {total}")
    if total > terbesar:
        terbesar = total
        donatur = nama
print(f"Total cash: ", {sum(kas.values())})
print(f"Top contributor", donatur, terbesar)