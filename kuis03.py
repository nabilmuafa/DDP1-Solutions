import random as rd
jumlah_lemparan = int(input("nilai N: "))
angka_dicari = int(input("nilai K: "))
print()

jawaban = 0

for urutan_loop in range(1, jumlah_lemparan+1):
    lemparan_dadu = rd.randrange(1, 7) #mengambil angka random dari 1 - 6
    print(f"nilai dadu loop {urutan_loop} = {lemparan_dadu}")
    if lemparan_dadu == angka_dicari:
        jawaban += 1
print(f"banyaknya kemunculan angka {angka_dicari} = {jawaban}")
