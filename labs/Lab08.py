# Lab 08 DDP 1 - H
#
# Dikerjakan oleh Muhammad Nabil Mu'afa - 2206024972

def count_total_dist(arah_kenalan, name, final_name):
    """Fungsi rekursif untuk menghitung total jarak"""
    if name not in arah_kenalan:
        # Akan return False jika tidak ditemukan arah
        return False
    elif arah_kenalan[name][0] == final_name:
        # Akan return jarak jika yang dikenal oleh name sama seperti nama tujuan
        return arah_kenalan[name][1]
    else:
        # Rekursi
        dist = count_total_dist(
            arah_kenalan, arah_kenalan[name][0], final_name)
        if not dist:
            # Return False jika tidak ditemukan arah
            return False
        else:
            # Return penjumlahan antara jarak name dengan yang dikenal dan variabel dist
            return arah_kenalan[name][1] + dist


def print_dist(name1, name2, distance):
    """Fungsi untuk mencetak pesan sesuai jarak"""
    if distance > 1000:
        print(f"{name1} dan {name2} tidak saling kenal.")
    elif distance > 100:
        print(f"{name1} dan {name2} mungkin saling kenal.")
    else:
        print(f"{name1} dan {name2} kenalan dekat.")


def main():
    """Fungsi utama"""
    # Deklarasi dictionary kosong
    arah_kenalan = dict()

    # Meminta input hingga input "SELESAI"
    print("Masukkan data hubungan:")
    data_kenalan = input()
    while data_kenalan != "SELESAI":
        # Memisahkan data kenalan
        data_kenalan = data_kenalan.split()
        first_name = data_kenalan[0]
        second_name = data_kenalan[1]
        distance = float(data_kenalan[2])
        # Menambahkan data kenalan dan jaraknya ke dalam dictionary
        arah_kenalan[first_name] = [second_name, distance]
        data_kenalan = input()
    print()
    # Input nama awal dan akhir
    nama_awal = input("Masukkan nama awal: ")
    nama_akhir = input("Masukkan nama tujuan: ")
    # Menghitung jarak dengan fungsi rekursi
    distance_between = count_total_dist(arah_kenalan, nama_awal, nama_akhir)
    # Jika jarak False, artinya tidak ditemukan hubungan
    if distance_between == False:
        print(f"Tidak ada hubungan antara {nama_awal} dan {nama_akhir}.")
    else:
        # Mencetak pesan jarak sesuai fungsi print_dist
        total_dist = int(distance_between*10)
        print(f"Jarak total: {total_dist}")
        print_dist(nama_awal, nama_akhir, total_dist)


if __name__ == "__main__":
    main()
