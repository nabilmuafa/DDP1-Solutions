# Tugas Pemrograman 03 DDP 1 - H
# Program akan melakukan simulasi POS (Point of Sales) yang
# bisa digunakan pembeli untuk memesan makanan dan minuman.
#
# Dikerjakan oleh Muhammad Nabil Mu'afa (2206024972) - graded 100/100

def rupiah_formatting(price):
    """Fungsi untuk mengembalikan formatting harga dalam Rupiah"""
    return f"{price:0,.0f}".replace(",", ".")

def print_menu(category, menu):
    """Fungsi untuk mencetak menu"""
    print("Berikut ini adalah menu yang kami sediakan:")
    # Iterasi kategori
    for key in category:
        print(f"{key}:")
        # Iterasi kode menu dalam setiap kategori
        for menus in category[key]:
            menu_name = menu[menus][0]
            menu_price = rupiah_formatting(menu[menus][1])
            # Mencetak kode menu, nama menu, dan harga menu
            print(f"{menus} {menu_name}, Rp{menu_price}")
    print()

def print_orders(menu, orders, table_number):
    """Fungsi untuk mencetak list order berdasarkan nomor meja"""
    # Iterasi pesanan suatu meja
    for order_list in orders[table_number]:
        # Tidak perlu cetak ketika yang di iterasi adalah nama/total harga
        if order_list == "name" or order_list == "total_price":
            continue
        # Menyimpan sementara total harga dalam formatting rupiah
        order_price = rupiah_formatting(orders[table_number][order_list][1])
        # Mencetak nama menu, jumlah pesanan, dan harga
        print(
            f"{menu[order_list][0]} {orders[table_number][order_list][0]} buah, total Rp{order_price}")
    print()

def add_orders(menu, name_to_code, orders, table_number, pesanan):
    """Fungsi untuk menambahkan pesanan pesanan ke orders"""
    # Mengubah nama pesanan menjadi kodenya untuk akses menu
    if pesanan in name_to_code:
        pesanan = name_to_code[pesanan]
    # Jika yang dipesan tidak ada di menu
    if pesanan not in menu:
        print(f"Menu {pesanan} tidak ditemukan!", end=" ")
    else:
        # Menyimpan sementara di variabel
        order_name = menu[pesanan][0]
        order_price = menu[pesanan][1]
        # Menambahkan list [0, 0] ke dictionary dengan key kode pesanan
        # jika pesanan sebelumnya belum pernah dipesan
        if pesanan not in orders[table_number]:
            orders[table_number][pesanan] = [0, 0]
        # Menambahkan jumlah pesanan, harga pesanan, serta total harga keseluruhan
        orders[table_number][pesanan][0] += 1
        orders[table_number][pesanan][1] += order_price
        orders[table_number]["total_price"] += order_price
        print(f"Berhasil memesan {order_name}.", end=" ")
        
def buat_pesanan(category, menu, name_to_code, orders):
    """Fungsi yang dapat membuat pesanan untuk disimpan"""
    # Mencari meja index terkecil yang kosong
    table_number = orders.index(0)
    # Membuat dict kosong untuk pesanan meja tersebut
    orders[table_number] = {}
    # Menginput nama dan deklarasi total harga ke pesanan
    orders[table_number]["name"] = input("Siapa nama Anda? ")
    orders[table_number]["total_price"] = 0
    print()
    print_menu(category, menu)
    # Meminta input pesanan hingga input "SELESAI"
    pesan = input("Masukkan menu yang ingin anda pesan: ")
    while pesan != "SELESAI":
        add_orders(menu, name_to_code, orders, table_number, pesan)
        pesan = input("Masukkan menu yang ingin anda pesan: ")
    print()
    # Mencetak rincian pesanan
    print("Berikut adalah pesanan anda: ")
    print_orders(menu, orders, table_number)
    print(
        f"Total pesanan: Rp{rupiah_formatting(orders[table_number]['total_price'])}")
    print(
        f"Pesanan akan kami proses, Anda bisa menggunakan meja nomor {table_number+1}. Terima kasih.\n")
    print("---")

def ganti_jumlah(menu, name_to_code, orders, table_number):
    """Fungsi yang dapat mengubah jumlah dari menu yang sudah dipesan"""
    change = input("Menu apa yang ingin anda ganti jumlahnya? ")
    # Mengubah nama pesanan jadi kodenya
    if change in name_to_code:
        code_change = name_to_code[change]
    else:
        code_change = change[:]
    # Print pesan jika pesanan tidak terdapat di menu
    # atau malah mengakses key name/total_price dari orders
    if code_change not in menu or change == "name" or change == "total_price":
        print(f"Menu {change} tidak ditemukan!", end=" ")
    # Print pesan jika pesanan belum dipesan sebelumnya
    elif code_change not in orders[table_number]:
        print(f"Menu {change} tidak Anda pesan sebelumnya.", end=" ")
    else:
        # Meminta input jumlah pesanan yang baru
        new_quantity = input("Masukkan jumlah pesanan yang baru: ")
        if not new_quantity.isdigit(): # Memeriksa jika jumlah baru adalah integer
            print("Jumlah harus bilangan positif!", end=" ")
        else:
            new_quantity = int(new_quantity)
            if new_quantity <= 0: # Memeriksa jika jumlah baru lebih dari nol
                print("Jumlah harus bilangan positif!", end=" ")
            else:
                # Mengubah jumlah pesanan, harga pesanan, dan total harga
                orders[table_number][code_change][0] = new_quantity
                orders[table_number]["total_price"] -= orders[table_number][code_change][1]
                orders[table_number][code_change][1] = new_quantity * menu[code_change][1]
                orders[table_number]["total_price"] += orders[table_number][code_change][1]
                print(
                    f"Berhasil mengubah pesanan {menu[code_change][0]} {new_quantity} buah.", end=" ")

def hapus_order(menu, name_to_code, orders, table_number):
    """Fungsi yang dapat menghapus pesanan yang sudah dipesan"""
    delete = input("Menu apa yang ingin Anda hapus dari pesanan: ")
    # Mengubah nama pesanan yang ingin dihapus menjadi kodenya
    if delete in name_to_code:
        code_delete = name_to_code[delete]
    else:
        code_delete = delete[:]
    # Print pesan jika pesanan tidak terdapat di menu
    # atau malah mengakses key name/total_price dari orders
    if code_delete not in menu or delete == "name" or delete == "total_price":
        print(f"Menu {delete} tidak ditemukan!", end=" ")
    # Print pesan jika pesanan belum pernah dipesan sebelumnya
    elif code_delete not in orders[table_number]:
        print(f"Menu {delete} tidak Anda pesan sebelumnya.", end=" ")
    else:
        # Menghapus pesanan dan mengurangi total price
        orders[table_number]["total_price"] -= orders[table_number][code_delete][1]
        deleted = orders[table_number].pop(code_delete)
        print(
            f"{deleted[0]} buah {menu[code_delete][0]} dihapus dari pesanan.", end=" ")

def tambah_pesanan(menu, name_to_code, orders, table_number):
    """Fungsi yang dapat menambahkan pesanan setelah 'BUAT PESANAN'"""
    add = input("Menu apa yang ingin anda pesan: ")
    add_orders(menu, name_to_code, orders, table_number, add)

def ubah_pesanan(category, menu, name_to_code, orders, table_number):
    """Fungsi yang dapat mengubah isi pesanan"""
    # Input nomor meja berupa integer
    if 1 <= table_number <= 10:
        if orders[table_number-1] == 0:
            # Tidak valid jika order pada meja tsb kosong
            print("Nomor meja kosong atau tidak sesuai!")
        else:
            table_number -= 1
            print()
            print_menu(category, menu)
            print("Berikut adalah pesanan Anda:")
            print_orders(menu, orders, table_number)
            # Meminta input fitur hingga input "SELESAI"
            sec_query = input("Apakah anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
            while sec_query != "SELESAI":
                # If statements yang menjalankan fitur sesuai input
                if sec_query == "GANTI JUMLAH":
                    ganti_jumlah(menu, name_to_code, orders, table_number)
                elif sec_query == "HAPUS":
                    hapus_order(menu, name_to_code, orders, table_number)
                elif sec_query == "TAMBAH PESANAN":
                    tambah_pesanan(menu, name_to_code, orders, table_number)
                else:
                    print("Fitur tidak tersedia!", end=" ")
                sec_query = input("Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
            print()
            # Mencetak pesanan yang sudah diubah
            print("Berikut adalah pesanan terbaru Anda:")
            print_orders(menu, orders, table_number)
            print(
                f"Total pesanan: Rp{rupiah_formatting(orders[table_number]['total_price'])}")
    else:
        print("Nomor meja kosong atau tidak sesuai!")
    print("\n---")

def selesai_pesanan(menu, orders, table_number):
    """Fungsi jika meja sudah selesai digunakan/pesanan selesai"""
    # Jika nomor meja diantara 1 hingga 10, valid
    if 1 <= table_number <= 10:
        # Jika tidak terdapat order di nomor meja tsb, tidak valid
        if orders[table_number-1] == 0:
            print("Nomor meja kosong atau tidak sesuai!")
        else:
            # Menyimpan order pada variabel lain (sementara)
            current_order = orders[table_number-1]
            nama = current_order["name"]
            print(
                f"Pelanggan atas nama {nama} selesai menggunakan meja {table_number}.")

            # Menuliskan pesanan ke file receipt, dengan tambahan no. meja
            # untuk handle kasus nama sama beda meja
            with open(f"receipt_{nama}_table{table_number:02d}.txt", "w") as file:
                for order in current_order:
                    # Hanya menuliskan pesanan, tidak menulis nama dan total harga
                    if order == "name" or order == "total_price":
                        continue
                    orderlist = f"{order};{menu[order][0]};{current_order[order][0]};{menu[order][1]};{current_order[order][1]}"
                    file.write(orderlist+"\n")
                file.write(f"\nTotal {current_order['total_price']}")
            # Mengosongkan meja order setelah pesanan selesai
            orders[table_number-1] = 0
    else:
        print("Nomor meja kosong atau tidak sesuai!")
    print("\n---")

def read_menu(category, menu, names_and_codes, name_to_code):
    with open("menu.txt", "r") as file:
        content = file.readlines()
        if len(content)==0:
            print("Daftar menu tidak valid, cek kembali menu.txt!")
            exit()
        current_key = ""
        for line in range(len(content)):
            # Jika baris adalah 'kategori', akan dibuat kategori baru di
            # dict category dengan key kategori tsb dan value list kosong
            if content[line].strip()[:3] == "===":
                current_key = content[line].strip()[3:]
                if current_key not in menu:
                    category[current_key] = []
            # Jika baris pertama dari menu.txt bukan kategori, maka error
            elif line == 0:
                print("Daftar menu tidak valid, cek kembali menu.txt!")
                exit()
            # Jika baris menuliskan menu sesuai format, tambahkan ke
            # menu dan masukkan sesuai current key (current category)
            elif content[line].strip().count(";") == 2:
                key_content = content[line].strip().split(";")
                if (
                    all(key_content) # Tidak ada menu yang kosong
                    and key_content[0] not in names_and_codes # Belum ada di set
                    and key_content[1] not in names_and_codes # Belum ada di set
                    and key_content[2].isdigit() # Merupakan integer
                ):
                    key_content[2] = int(key_content[2])
                    # Memeriksa jika key_content[2] bilangan non negatif
                    if key_content[2] >= 0:
                        names_and_codes.update(key_content[:2]) # Tambahkan ke set
                        menu[key_content[0]] = tuple(key_content[1:]) # Tambahkan ke menu
                        name_to_code[key_content[1]] = key_content[0] # Tambahkan mapping
                        category[current_key].append(key_content[0]) # Masukkan ke kategori
                else:
                    print("Daftar menu tidak valid, cek kembali menu.txt!")
                    exit()
            else:
                print("Daftar menu tidak valid, cek kembali menu.txt!")
                exit()

def main():
    """Fungsi utama"""
    # Deklarasi variabel
    names_and_codes = set()     # Untuk memastikan tidak ada menu dobel
    category = {}               # Mengkategorikan menu sesuai menu.txt
    menu = {}
    # menu adalah dict of lists, dimana key adalah kode dagangan,
    # value[0] adalah nama dagangan, dan value[1] adalah harga.
    name_to_code = {}           # Untuk mapping kode menu dari nama menu
    # Membaca menu
    read_menu(category, menu, names_and_codes, name_to_code)
    # Membuat list kosong untuk order
    orders = [0 for _ in range(10)]
    table_counter = 0
    running = True
    while running:
        print("Selamat datang di Kafe Daun Daun Pacilkom")
        # Meminta input untuk fitur
        query = input("Apa yang ingin anda lakukan? ")
        if query == "BUAT PESANAN":
            # Jika meja sudah penuh (>=10), tidak buat pesanan
            if table_counter >= 10:
                print("Mohon maaf meja sudah penuh, silakan kembali nanti.")
                print("\n---")
            # Otherwise, membuat pesanan
            else:
                buat_pesanan(category, menu, name_to_code, orders)
                table_counter += 1
        elif query == "UBAH PESANAN":
            try:
                table_number = int(input("Nomor meja berapa? "))
                ubah_pesanan(category, menu, name_to_code, orders, table_number)
            except:
                print("Nomor meja kosong atau tidak sesuai!")
                print("\n---")
        elif query == "SELESAI MENGGUNAKAN MEJA":
            try:
                table_number = int(input("Nomor meja berapa? "))
                selesai_pesanan(menu, orders, table_number)
                table_counter -= 1
            except:
                print("Nomor meja kosong atau tidak sesuai!")
                print("\n---")
        else:
            print("Fitur tidak tersedia!")
            print("\n---")

if __name__ == "__main__":
    main()
