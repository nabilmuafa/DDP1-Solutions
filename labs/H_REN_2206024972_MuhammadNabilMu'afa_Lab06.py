# Lab 06 DDP 1 - H
#
# Dikerjakan oleh Muhammad Nabil Mu'afa - 2206024972

def get_nilai(kunjaw, jawaban):
    """Fungsi untuk mendapatkan jumlah jawaban benar dan nilai yang didapat"""
    # Deklarasi variabel
    banyak_soal = len(kunjaw)
    jawaban_salah = 0

    # Menambahkan jawaban salah jika jawaban berbeda dengan kunci jawaban
    for i in range(banyak_soal):
        if kunjaw[i] != jawaban[i]:
            jawaban_salah += 1

    # Mengambil jumlah jawaban benar
    jawaban_benar = banyak_soal - jawaban_salah
    # Menghitung nilai dalam skala 100, pembulatan ke bawah
    nilai = int((jawaban_benar/banyak_soal) * 100)
    return (nilai, jawaban_benar)

def get_message(nilai):
    "Mencetak pesan sesuai dengan nilai yang didapatkan"
    if nilai >= 85:
        print("Selamat :D")
    elif nilai >= 55:
        print("Semangat :)")
    else:
        print("nt")

def main():
    """Fungsi utama untuk menjalankan program"""
    print("Selamat mencoba Program Pemeriksa Nilai Dek Depe!")
    print("=================================================\n")
    
    kunci_jawaban = []

    # Meminta input kunci jawaban hingga input bernilai "STOP"
    print("Masukkan kunci jawaban: ")
    ask_input = True
    while ask_input:
        jawaban = input()
        if jawaban == "STOP":
            ask_input = False
        else:
            kunci_jawaban.append(jawaban)

    banyak_soal = len(kunci_jawaban)

    # Meminta input nilai menggunakan list comprehension
    print("Masukkan jawaban kamu: ")
    jawaban_kamu = [input() for i in range(banyak_soal)]

    # Mengambil nilai dan jumlah jawaban benar dengan fungsi get_nilai
    nilai, jawaban_benar = get_nilai(kunci_jawaban, jawaban_kamu)

    print()
    # Mencetak pesan nilai dengan fungsi get_message
    get_message(nilai)
    print(f"Total jawaban benar adalah {jawaban_benar} dari {banyak_soal} soal")
    print(f"Nilai yang kamu peroleh adalah {nilai}")

if __name__ == "__main__":
    main()