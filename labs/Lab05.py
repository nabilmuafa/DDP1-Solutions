# Lab 05 DDP 1 - H
#
# Dikerjakan oleh Muhammad Nabil Mu'afa - 2206024972

from math import pi as PI

def volume_balok():
    """Meminta input dimensi balok dan mengembalikan nilai volumenya"""
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))
    return panjang * lebar * tinggi

def volume_kerucut():
    """Meminta input dimensi kerucut dan mengembalikan nilai volumenya"""
    jari_jari = float(input("Masukkan jari-jari kerucut: "))
    tinggi = float(input("Masukkan tinggi kerucut: "))
    return (1/3) * PI * jari_jari * jari_jari * tinggi

def main():
    """Fungsi utama"""
    print("Selamat datang di Depot Minuman Dek Depe!")
    print("="*42)

    # Initialisasi variabel total volume dan boolean berlangsung untuk while loop
    total_volume = 0.0
    berlangsung = True

    while berlangsung:
        bentuk_galon = input(
            "Masukkan bentuk galon yang diinginkan (STOP untuk berhenti): ")
        # Akan mengubah nilai boolean berlangsung jadi False jika input yang diterima adalah "STOP"
        if bentuk_galon == "STOP":
            berlangsung = False
            print()
            continue
        # Akan memanggil fungsi volume balok jika input adalah "BALOK"
        elif bentuk_galon == "BALOK":
            volume_galon = volume_balok()
            total_volume += volume_galon
        # Akan memanggil fungsi volume kerucut jika input adalah "KERUCUT"
        elif bentuk_galon == "KERUCUT":
            volume_galon = volume_kerucut()
            total_volume += volume_galon
        # Akan mencetak pesan error jika input tidak sesuai format
        else:
            print("Input tidak benar, masukkan kembali")
        print()

    # Menghitung total harga
    total_harga = total_volume*700
    print("="*52)

    # Mencetak total volume dan harga
    if total_harga > 0 and total_volume > 0:
        print(
            f"Total volume air yang dikeluarkan adalah : {total_volume:.2f}")
        print(f"Total harga yang harus dibayar adalah : Rp{total_harga:.2f}")
    # Mencetak pesan jika tidak ada input yang valid yang dimasukkan hingga "STOP"
    else:
        print("Anda tidak memasukkan input satupun :(")

    print("="*52)
    print()
    print("Terima kasih telah menggunakan Depot Air Minum Dek Depe")

if __name__ == "__main__":
    main()
