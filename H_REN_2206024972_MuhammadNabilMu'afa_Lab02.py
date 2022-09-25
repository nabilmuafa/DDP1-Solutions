print("Selamat datang ke Dek Depe Holiday Tracker!\n")

# meminta input jumlah tempat wisata
jumlah_wisata = int(input("Masukkan banyak tempat wisata yang kamu kunjungi: "))
while jumlah_wisata <= 0: # akan meminta input ulang jika jumlah_wisata nonpositif
    print("Input tidak valid. Silahkan masukkan input kembali!\n")
    jumlah_wisata = int(input("Masukkan banyak tempat wisata yang kamu kunjungi: "))
print()

rating_tertinggi = 0 # variabel untuk menyimpan rating tertinggi
jumlah_rating = 0 # variabel untuk menyimpan jumlah rating (untuk menghitung skala kebahagiaan)
best_wisata = "" # variabel untuk menyimpan nama tempat wisata paling berkesan

#meminta input nama tempat wisata dan ratingnya
for i in range(1, jumlah_wisata+1):
    tempat_wisata = input(f"Perjalanan {i}: ")
    rating_wisata = int(input(f"Rating perjalanan kamu ke {tempat_wisata} (indeks 1-10): "))
    jumlah_rating += rating_wisata
    if rating_wisata >= rating_tertinggi:
        # rating tertinggi akan diupdate jika rating_wisata > rating_tertinggi
        rating_tertinggi = rating_wisata
        # tempat wisata paling berkesan akan diupdate juga
        best_wisata = tempat_wisata
    print()

skala_happiness = jumlah_rating / jumlah_wisata # menghitung skala kebahagiaan Dek Depe
print("# # # Summary # # #")
print(f"Perjalanan paling mengesankan adalah ketika pergi ke {best_wisata}.")
print(f"Skala kebahagiaan Dek Depe adalah {skala_happiness:.2f}")

# conditionals untuk menghasilkan output sesuai ketentuan
if skala_happiness < 5:
    print("Dek Depe sedih karena pengalamannya buruk.")
elif skala_happiness < 8:
    print("Dek Depe senang karena pengalamannya cukup baik.")
else:
    print("Dek Depe bahagia karena pengalamannya menyenangkan.")

print("\nTerima kasih telah menggunakan Dek Depe Holiday Tracker!")