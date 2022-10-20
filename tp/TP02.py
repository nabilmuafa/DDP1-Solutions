# Tugas Pemrograman 02 DDP 1 - H
# Program akan melakukan grep seperti di Linux
#
# Solved by Muhammad Nabil Mu'afa - not yet graded
#
# Known errors:
# >> python TP02.py "olah*ra*a" mydir (forgot to handle more than 2 "*"s in no argument mode)
# >> python TP02.py -w "o*" mydir     (wrongfully handled in this code)
# >> python TP02.py -w "*o" mydir     (same case as "o*")

import os
import sys

def print_line(dirs, line, kalimat):
    """Mencetak barisan yang match dengan pola dicari"""
    print(f"{dirs:<40} line {line:<3} {kalimat}")

def wildcard(baris, pattern):
    """Return True jika pola wildcard match dengan baris"""

    # Asumsi untuk kasus wildcard dengan -w:
    # Jika "*" ada di tengah kata, maka program akan tetap match dengan kata apapun
    # selama kata di sebelah kiri "*" berbatasan dengan whitespace di sebelah kiri
    # dan kata di sebelah kanan "*" berbatasan dengan whitespace di sebelah kanan.

    # Menjalankan block code jika "*" ada di tengah-tengah pola yang dicari
    if "*" in pattern.strip()[1:-1]:
        # Memisahkan pola menjadi dua bagian
        pattern_left, pattern_right = pattern.split("*")
        # Akan return True jika terdapat dua bagian pola di dalam baris,
        # dan jika bagian pola kiri terdapat di sebelah kirinya bagian pola kanan dalam baris
        return (
            pattern_left in baris
            and pattern_right in baris
            and baris.index(pattern_left) + len(pattern_left) - 1 < baris.rindex(pattern_right)
        )

    # Menjalankan block code jika "*" ada di depan/belakang pola yang dicari
    else:
        # Menghilangkan "*" sesuai petunjuk pada soal, karena
        # "[kata]*" sama saja dengan "[kata]"
        pattern_no_wildcard = pattern.replace("*", "")

        # Return True jika pola ditemukan di baris
        return pattern_no_wildcard in baris

def is_in_line(baris, pattern, arg=None):
    """Memanipulasi pattern sesuai argumen dan memeriksa jika pola
    ditemukan pada baris, return True jika iya dan vice versa"""
    if arg == "-w":
        # Menambahkan whitespace di depan dan belakang pola dan baris
        pattern = f" {pattern} "
        baris = f" {baris} "
    elif arg == "-i":
        # Mengubah pola dan baris menjadi lowercase semua
        pattern = pattern.lower()
        baris = baris.lower()
    else:
        # Tidak akan melakukan apa-apa jika tidak ada argumen
        pass
    if "*" in pattern:
        # Memanggil fungsi wildcard jika ada "*" di pola
        return wildcard(baris, pattern)
    else:
        # Return True jika pola ditemukan di baris
        return pattern in baris

def scan_line(file_path, pattern, arg=None):
    """Membaca setiap baris dari file dan akan mencetak baris jika ditemukan pola"""
    with open(file_path, "r") as file_teks:
        isi_teks = file_teks.readlines()
        for index in range(len(isi_teks)):
            # Membersihkan baris dari newline
            baris = isi_teks[index].strip()

            # Menjalankan fungsi is_in_line untuk memeriksa apakah pola ada di baris
            if is_in_line(baris, pattern, arg):
                print_line(file_path, index+1, baris[:40])

def main(arg):
    """Fungsi utama untuk program"""

    # Jika tidak ada argumen -w atau -i
    if len(arg) == 3:
        mode = None
        pola_dicari = arg[1]
        # Just a stupid conditional to handle an error
        if pola_dicari == '-i' or pola_dicari == '-w':
            print("Argumen program tidak benar.")
            exit()
        directory = arg[2]

    # Jika ada argumen opsional
    elif len(arg) == 4:
        mode = arg[1]
        pola_dicari = arg[2]
        directory = arg[3]

        # Jika argumen opsional bukan "-w" atau "-i", atau jika
        # terdapat lebih dari satu "*" di dalam pola
        if (
            mode not in ["-w", "-i"]
            or (pola_dicari.count("*") > 1)
        ):
            print("Argumen program tidak benar.")
            exit()

    # Jika kekurangan/kelebihan argumen
    else:
        print("Argumen program tidak benar.")
        exit()

    # Memeriksa apakah path yang dicari ada, print error jika tidak
    if not os.path.exists(directory):
        print(f"Path {directory} tidak ditemukan")
        exit()

    # Akan langsung menjalankan scan jika directory yang diinput sudah langsung file
    if os.path.isfile(directory):
        scan_line(directory, pola_dicari, mode)

    # Menjalankan scan pada setiap folder
    else:
        for (root, _, files) in os.walk(directory):
            for file in files:
                # Membentuk directory yang lengkap dengan nama file, lalu melakukan scan
                file_path = os.path.join(root, file)
                scan_line(file_path, pola_dicari, mode)

if __name__ == "__main__":
    main(sys.argv)
