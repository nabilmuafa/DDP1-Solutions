# Lab 07 DDP 1 - H
#
# Dikerjakan oleh Muhammad Nabil Mu'afa - 2206024972

def print_hasil(bulan):
    """Fungsi mencetak hasil pencarian"""
    exists = False
    print("================= Hasil ================")
    # Mencetak jika key bulan ada di dict nama
    if bulan in name_month:
        exists = True
        print(f"Terdapat {len(name_month[bulan])} nama yang lahir di bulan {bulan}:")
        for names in name_month[bulan]:
            print(f"- {names}")
        print()
    #Mencetak jika key bulan ada di dict npm
    if bulan in npm_month:
        exists = True
        print(f"Terdapat {len(npm_month[bulan])} nama yang lahir di bulan {bulan}:")
        for npm in npm_month[bulan]:
                print(f"- {npm}")
        print()
    # Mencetak pesan jika pencarian tidak menghasilkan apa-apa
    if not exists:
        print(f"Tidak ditemukan mahasiswa dan NPM yang lahir di bulan {bulan}.\n")
                
print("Selamat datang di program Mengenal Angkatan!")
print("===========================================")
print("Masukkan identitas mahasiswa:")

# Deklarasi dict kosong
npm_month = dict()
name_month = dict()

#Meminta input hingga input "STOP"
identities = input()
while identities != "STOP":
    # Memisahkan input string sesuai dengan fungsinya
    details = identities.split()
    name = details[0]
    npm = details[1]
    month = details[4]
    # Menambahkan key month ke dictionary dengan value set kosong
    # jika key month belum ada di dictionary
    if month not in npm_month:
        npm_month[month] = set()
        name_month[month] = set()
    # Menambahkan isi ke set yang ada di key month
    npm_month[month].add(npm)
    name_month[month].add(name)
    identities = input()
    
print()
# Mencari nama dan npm sesuai bulan hingga input "STOP"
search = input("Cari mahasiswa berdasarkan bulan: ")
while search != "STOP":
    print_hasil(search)
    search = input("Cari mahasiswa berdasarkan bulan: ")
    
print("\nTerima kasih telah menggunakan program ini, semangat PMB-nya!")
