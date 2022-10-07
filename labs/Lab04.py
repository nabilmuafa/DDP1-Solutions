# Lab 04 DDP 1 - H
#
# Dikerjakan oleh Muhammad Nabil Mu'afa - 2206024972

print("Selamat datang di Pacil Mart!\n")

file = input("Masukkan nama file input: ")
# try-except block untuk memeriksa keberadaan file
# print error jika file tidak ada
try:
    masukan = open(file, "r")
except FileNotFoundError:
    print("File tidak tersedia.")
    exit()

# menyimpan isi file per baris di variabel baris
baris = masukan.readlines()

# memeriksa jika isi file kosong, akan exit jika ya
if len(baris)==0:
    print("File input ada tapi kosong.")
    exit()

print("\nBerikut adalah daftar belanjaanmu: \n")
# print baris nama barang, jumlah, kembalian dengan string formatting align
print(f"{'Nama Barang'.ljust(12)}|{'Jumlah'.rjust(8)}|{'Kembalian'.rjust(10)}")
print("-"*32)

# iterasi tiap baris dari input
for item in baris:
    # memisahkan kata tiap baris
    barang = item.split()

    # menyimpan masing-masing nama barang, uang alokasi, dan harga barang
    nama_barang = barang[0].strip() 
    uang_alokasi = int(barang[1].strip()) 
    harga_per_barang = int(barang[2].strip())

    # mencetak nama barang dengan string formatting
    print(f"{nama_barang.ljust(12)}|", end="")

    # menghitung jumlah maksimal yang bisa dibeli dan mencetak
    # dengan string formatting 
    jumlah_max = uang_alokasi//harga_per_barang
    print(f"{str(jumlah_max).rjust(8)}|", end="")

    # kembalian akan 0 jika tidak ada barang yang bisa dibeli
    if jumlah_max == 0:
        kembalian = 0
    else:
        kembalian = uang_alokasi - jumlah_max*harga_per_barang
    # mencetak jumlah kembalian dengan string formatting
    print(str(kembalian).rjust(10))

print("\nTerima kasih sudah belanja di Pacil Mart!")
masukan.close()
