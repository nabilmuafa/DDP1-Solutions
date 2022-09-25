# Lab 03 DDP 1-H
#
# Dikerjakan oleh Muhammad Nabil Mu'afa - 2206024972

print("Selamat Datang di Bunker Hacker!\n")

# meminta input banyak konversi yang ingin dilakukan
banyak_konversi = int(input("Masukkan berapa kali konversi yang ingin dilakukan: "))
for i in range(banyak_konversi):
    angka_desimal = int(input(f"\nMasukkan angka ke-{i+1} yang ingin dikonversikan (dalam desimal): "))
    angka_octal = ""
    while angka_desimal > 0: # akan loop selama angka desimal masih belum habis (menjadi 0) dibagi 8
        sisa_bagi = angka_desimal % 8 # mengambil sisa pembagian angka desimal dengan 8
        angka_octal = str(sisa_bagi) + angka_octal # menambahkan str(sisa_bagi) di depan string angka_octal
        angka_desimal //= 8 # melakukan integer division pada angka desimal
    print(f"Hasil konversi desimal ke basis 8 :", angka_octal)

print("\nTerima kasih telah menggunakan Bunker Hacker!")