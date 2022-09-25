nama = input("Masukkan nama anda: ")
harga_awal = float(input("Masukkan harga buku awal: "))
harga_diskon = float(input("Masukkan harga buku setelah diskon: "))

# harga_diskon = harga_awal - (harga_awal * diskon_desimal)
# harga_awal - harga_diskon = harga_awal * diskon_desimal
# (harga_awal - harga_diskon) / harga_awal = diskon_desimal

diskon_desimal = (harga_awal - harga_diskon) / harga_awal
diskon_persen = diskon_desimal * 100 #agar diskon dalam desimal menjadi persen maka dikali 100
print(f"Halo, {nama}! Anda mendapatkan diskon sebesar {diskon_persen} persen!")