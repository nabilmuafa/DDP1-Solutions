from math import *
BIAYA_PER_CM2 = 0.40

nama = input("Masukkan nama anda: ")
panjang_persegi = float(input("Masukkan panjang persegi nametag (dalam cm): "))
panjang_trapesium = float(input("Masukkan panjang trapesium nametag (dalam cm): "))
jumlah_nametag = int(input("Masukkan jumlah nametag yang ingin dibuat: "))

luas_persegi = panjang_persegi * panjang_persegi
luas_setengah_lingkaran = 0.5 * pi * (panjang_persegi/2) * (panjang_persegi/2)
luas_segitiga = 0.5 * panjang_persegi * panjang_persegi
luas_trapesium = (panjang_persegi + panjang_trapesium) * panjang_persegi * 0.5

luas_per_nametag = luas_persegi + luas_segitiga + luas_setengah_lingkaran + luas_trapesium
luas_total_nametag = luas_per_nametag * jumlah_nametag
#menghitung total dengan pembulatan ke ribuan di atas
biaya_total = ceil(BIAYA_PER_CM2 * luas_total_nametag / 1000) * 1000

print(f"\nHalo, {nama}! Berikut adalah informasi mengenai nametag Anda:\n")
print(f"Luas 1 nametag: {luas_per_nametag:.2f} cm^2")
print(f"Luas total nametag ({jumlah_nametag} buah): {luas_total_nametag:.2f} cm^2")
print(f"Biaya yang diperlukan: Rp{int(biaya_total)}")
