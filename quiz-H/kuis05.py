filename = input("nama file: ")

try:
    file = open(filename, "r")
# menghandle jika baris tidak ditemukan
except FileNotFoundError:
    print("file tidak ditemukan!")
    exit()

# membaca isi file per baris ke variabel isi_file
isi_file = file.readlines()

# iterasi setiap baris
for baris in isi_file:
    # men-strip baris dan memisahnya menjadi per kata
    per_kata = baris.strip().split()
    
    # iterasi tiap kata dalam urutan terbalik
    for word in per_kata[::-1]:
        print(word, end=" ")
    print()
    
    
# was graded 90/100 because I forgot to put close() lmao
