# Tugas Pemrograman 04 DDP 1 - H
#
# Basically TP03, but with GUI (and less
# features to implement, thank God)
#
# Dikerjakan oleh Muhammad Nabil Mu'afa (2206024972)
# Kolaborator: Alden Luthfi A. (2206028932)

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkmsg
import random as r

class Menu:
    # Class untuk item dari menu
    def __init__(self, kode_menu, nama_menu, harga):
        self.__kode_menu = kode_menu
        self.__nama_menu = nama_menu
        self.__harga = int(harga)

    def get_code(self):
        return self.__kode_menu

    def get_name(self):
        return self.__nama_menu

    def get_price(self):
        return self.__harga

class Meals(Menu):
    # Class untuk menu yang termasuk kategori Meals,
    # inheritance dari class Menu
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kegurihan):
        super().__init__(kode_menu, nama_menu, harga)
        self.kegurihan = tingkat_kegurihan

class Drinks(Menu):
    # Class untuk menu yang termasuk kategori Drinks,
    # inheritance dari class Menu
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kemanisan):
        super().__init__(kode_menu, nama_menu, harga)
        self.kemanisan = tingkat_kemanisan

class Sides(Menu):
    # Class untuk menu yang termasuk kategori Sides,
    # inheritance dari class Menu
    def __init__(self, kode_menu, nama_menu, harga, tingkat_keviralan):
        super().__init__(kode_menu, nama_menu, harga)
        self.keviralan = tingkat_keviralan

class Orders():
    # Class yang menyimpan pesanan-pesanan pada suatu meja
    def __init__(self, menu, nama):
        self.__nama = nama
        self.__orders = []

        # Append setiap item pada menu ke self.__orders
        for categ in menu:
            for dishes in menu[categ]:
                self.__orders.append(dishes)

        # Set initial value quantity dan harga per item = 0
        self.__quantity = [0 for _ in range(len(self.__orders))]
        self.__price_per_item = self.__quantity[:]

    # Setters and getters
    def get_name(self):
        return self.__nama

    def get_orders(self):
        return self.__orders

    def get_quantity(self):
        return self.__quantity

    def get_item_quantity(self, item):
        # Quantity per item
        index = self.get_orders().index(item)
        list_quantity = self.get_quantity()
        return list_quantity[index]

    def get_total_price(self):
        # Total price dari semua item
        return sum(self.__price_per_item)

    def set_quantity(self, index, new_quantity):
        self.__quantity[index] = new_quantity

    def set_price_per_item(self, index, new_total_price):
        # Total price dari suatu item
        self.__price_per_item[index] = new_total_price

    def set_orders(self, item, quantity):
        # Mengganti jumlah item yang dipesan
        index = self.get_orders().index(item)
        self.set_quantity(index, quantity)
        new_price = quantity * item.get_price()
        self.set_price_per_item(index, new_price)

class Main(tk.Frame):
    # Menu utama/landing page
    def __init__(self, data, orderlist, master=None):
        super().__init__(master)
        self.pack()
        self.data = data
        self.orderlist = orderlist
        self.master.geometry("400x200")
        master.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

        # Tombol-tombol
        button1 = tk.Button(self, text="Buat Pesanan", width=30, bg="#4472C4",
                            fg="white", command=self.buat_pesanan)
        button2 = tk.Button(self, text="Selesai Gunakan Meja", width=30,
                            bg="#4472C4", fg="white", command=self.selesai_gunakan_meja)
        button1.grid(row=0, column=0, padx=10, pady=40)
        button2.grid(row=1, column=0)

    def buat_pesanan(self):
        # Jika "Buat Pesanan" ditekan
        BuatPesanan(self.data, self.orderlist, self.master)

    def selesai_gunakan_meja(self):
        # Jika "Selesai Gunakan Meja" ditekan
        SelesaiGunakanMeja(self.data, self.orderlist, self.master)

class BuatPesanan(tk.Toplevel):
    # Menu buat pesanan, input nama pelanggan
    def __init__(self, data, orderlist, master=None):
        super().__init__(master)
        self.master.geometry("400x200")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.orderlist = orderlist
        self.data = data
        self.nama = tk.StringVar()
        self.create_widgets()

    def btn_back_clicked(self):
        # Tombol back di klik
        self.destroy()

    def btn_next_clicked(self):
        # Tombol lanjut di klik
        if all(self.orderlist):
            # Jika meja penuh
            tkmsg.showinfo(parent=self,
                           title="Meja Penuh", message="Mohon maaf, meja sedang penuh. " + \
                           "Silahkan datang kembali di lain kesempatan.")
            self.destroy()
        else:
            if self.nama.get() == "":
                tkmsg.showwarning(parent=self, title="Nama Kosong",
                                  message="Nama tidak boleh kosong!")
            # Instansiasi class MenuTable dengan opsi "ubah" jika ada meja kosong
            else:
                MenuTable(self, self.nama.get(), self.data,
                          self.orderlist, None, "buat", self.master)

    def create_widgets(self):
        # Membuat widgets berupa label, entry, dan dua tombol
        self.lbl_nama = tk.Label(self, text="Siapa nama Anda?")
        self.lbl_nama.grid(column=0, row=0, pady=60)

        self.ent_nama = tk.Entry(self, textvariable=self.nama)
        self.ent_nama.grid(column=1, row=0, pady=60)

        self.btn_back = tk.Button(self, text="Kembali", width=15,
                                  bg="#4472C4", fg="white",
                                  command=self.btn_back_clicked)
        self.btn_next = tk.Button(self, text="Lanjut", width=15,
                                  bg="#4472C4", fg="white",
                                  command=self.btn_next_clicked)

        self.btn_back.grid(row=1, column=0, padx=(40, 5), pady=20)
        self.btn_next.grid(row=1, column=1, padx=(5, 40), pady=20)

class ModifyMeja(tk.Toplevel):
    # Class yang bertanggung jawab untuk window "Ubah Meja" dan "Selesai Gunakan Meja"
    def __init__(self, table, data, orderlist, table_num, state, master=None):
        super().__init__(master)
        self.table = table                          # Window asal/"parent"
        self.orderlist = orderlist                  # Isi pesanan
        self.new_tabnum = table_num                 # Nomor meja
        self.data = data                            # Menu
        self.state = state                          # Opsi, "ubah" atau "selesai"
        self.button = [None for i in range(10)]     # List untuk menyimpan tombol
        if self.state == "ubah":
            # Jika opsi saat ini "ubah", akan menyimpan sementara pesanan
            # sesuai meja saat ini di instance var self.cur_order
            self.cur_order = orderlist[table_num]
            self.create_ubah_widgets()
        else:
            self.create_selesai_widgets()
        self.create_widgets()
        self.master.geometry("400x200")

    def update_color(self, table_num, color):
        # Mengubah warna tombol dari meja table_num (+ 1)
        self.button[table_num]["bg"] = color

    def create_ubah_widgets(self):
        # Membuat widget yang diperlukan window Ubah Meja,
        # yaitu label, info warna tambahan, dan tombol kembali/OK
        self.lbl_command = tk.Label(
            self, text="Silakan klik meja kosong yang diinginkan:")
        self.lbl_blue = tk.Label(self, text="Biru: Meja Anda")
        self.lbl_green = tk.Label(self, text="Hijau: Meja Pilihan Anda")
        self.btn_ok = tk.Button(self, text="OK", width=15, bg="#4472C4", 
                                fg="white", command=self.btn_ok_clicked)
        self.btn_back = tk.Button(self, text="Kembali", width=15,
                                  bg="#4472C4", fg="white",
                                  command=self.btn_back_clicked)

        self.lbl_command.grid(column = 0, row = 0, pady = (0, 20), 
                              columnspan = 4, sticky = "ew")
        self.lbl_blue.grid(row=9, column=0, padx=(20, 0), sticky="w")
        self.lbl_green.grid(row=10, column=0, padx=(20, 0), sticky="w")
        self.btn_ok.grid(row=11, column=2, columnspan=2, pady=40, padx=5,
                         sticky="w")
        self.btn_back.grid(row=11, column=0, columnspan=2, pady=40,
                           padx=5, sticky="e")

    def create_selesai_widgets(self):
        # Membuat widget yang diperlukan window Selesai Gunakan Meja,
        # yaitu label dan tombol kembali
        self.lbl_command = tk.Label(
            self, text="Silakan klik meja yang selesai digunakan:")
        self.btn_back = tk.Button(self, text="Kembali", width=15, bg="#4472C4",
                                  fg="white", command=self.btn_back_clicked)

        self.lbl_command.grid(column=0, row=0, pady=(0, 20), columnspan=4,
                              sticky="ew")
        self.btn_back.grid(row=11, column=0, columnspan=4,
                           pady=40, padx=5)

    def table_selected(self, tab_nums):
        # Method yang bertanggung jawab handle event sebuah tombol ditekan

        # Jika opsi saat ini adalah "ubah"
        if self.state == "ubah":
            # Jika meja dari tombol yang ditekan kosong
            if not self.orderlist[tab_nums]:
                # Jika meja yang sebelumnya ditekan bukan meja pelanggan
                # saat ini, update warnanya menjadi abu-abu
                if self.orderlist[self.new_tabnum] != self.cur_order:
                    self.update_color(self.new_tabnum, "#b3b3b3")
                
                self.new_tabnum = tab_nums
                # Ubah warna meja yang ditekan menjadi hijau
                self.update_color(self.new_tabnum, "green")
            # Jika meja terisi
            else:
                # Jika meja yang ditekan bukan meja pelanggan saat ini,
                # munculkan pesan error
                if self.orderlist[tab_nums] != self.cur_order:
                    tkmsg.showwarning(parent=self, title="Meja Terisi",
                                      message="Mohon maaf, meja ini sudah terisi. " \
                                      + "Silakan pilih meja lain.")
                
                # Jika meja yang ditekan adalah meja pelanggan saat ini,
                # cukup update warna meja sebelumnya jadi abu-abu
                else:
                    if self.new_tabnum != tab_nums:
                        self.update_color(self.new_tabnum, "#b3b3b3")
                    self.new_tabnum = tab_nums

        # Jika opsi saat ini adalah "selesai"
        else:
            # Jika meja tidak kosong
            if self.orderlist[tab_nums]:
                name = self.orderlist[tab_nums].get_name()
                # Instansiasi class MenuTable dengan opsi "selesai"
                MenuTable(self, name, self.data, self.orderlist,
                          tab_nums, "selesai", self.master)
            # Jika meja kosong, munculkan warning
            else:
                tkmsg.showwarning(parent=self, title="Meja Kosong",
                                  message="Mohon maaf, tidak ada pesanan di meja ini. " \
                                  + "Silakan pilih meja lain.")

    def btn_ok_clicked(self):
        # Jika tombol OK ditekan (opsi "ubah"), ganti nomor meja pada window parentnya
        if self.orderlist[self.new_tabnum] != self.cur_order:
            self.table.new_table_number(self.new_tabnum)
        self.destroy()

    def btn_back_clicked(self):
        # Jika tombol kembali ditekan
        self.destroy()

    def create_buttons(self, row, col):
        # Method yang membuat tombol (satuan)
        tab_num = (col-1)*5 + row                 # Magic number nomor meja
        pad = (0, 10) if col == 0 else (10, 0)    # Set padding sesuai posisi kolom
        self.button[tab_num] = tk.Button(self, text=str(tab_num+1), width=10, fg="white",
                                         command=lambda: self.table_selected(tab_num))
        # Atur warna
        if self.orderlist[tab_num] == 0:
            self.update_color(tab_num, "#b3b3b3") # abu-abu
        elif self.state == "ubah" and self.orderlist[tab_num] == self.cur_order:
            self.update_color(tab_num, "#4472C4") # biru
        else:
            self.update_color(tab_num, "#ff1100") # merah
        self.button[tab_num].grid(row=row+1, column=col, padx=pad, pady=5)

    def create_widgets(self):
        # Membuat widgets (general)

        # Label kosong untuk padding kanan
        self.lbl_empty = tk.Label(self, text="", padx=60)
        # Membuat 10 tombol
        for row in range(5):
            for col in range(1, 3):
                self.create_buttons(row, col)

        # Info warna
        self.lbl_info = tk.Label(self, text="Info", font="SegoeUI 9 bold")
        self.lbl_red = tk.Label(self, text="Merah: Terisi")
        self.lbl_grey = tk.Label(self, text="Abu-abu: Kosong")

        self.lbl_empty.grid(row=1, column=3)
        self.lbl_info.grid(row=6, column=0, padx=(20, 0), sticky="w")
        self.lbl_red.grid(row=7, column=0, padx=(20, 0), sticky="w")
        self.lbl_grey.grid(row=8, column=0, padx=(20, 0), sticky="w")

class MenuTable(tk.Toplevel):
    # Class yang bertanggung jawab untuk window tabel, baik saat memesan
    # atau setelah selesai gunakan meja
    def __init__(
            self, window_parent, nama, data,
            orderlist, tab_num, state, master=None
        ):
        super().__init__(master)
        self.orderlist = orderlist              # List pesanan
        self.data = data                        # Data menu
        self.nama = nama                        # Nama pemesan
        self.window_parent = window_parent      # Window asal/"parent"
        self.state = state                      # Opsi, "buat" atau "selesai"
        # Jumlah baris dan kolom
        self.rows = sum([len(i) for i in self.data.values()]) + 7
        self.cols = 5
        self.boxes = {}                         # Dictionary untuk menyimpan combobox

        # Membuat hal-hal yang diperlukan fitur Buat Pesanan
        if self.state == "buat":
            # Randomize table number
            self.tab_num = r.randint(0, 9)
            while self.orderlist[self.tab_num] != 0:
                self.tab_num = r.randint(0, 9)
            # Membuat orderan kosong dari class Orders
            self.orderlist[self.tab_num] = Orders(self.data, self.nama)
            self.total_price = 0
            self.create_buat_widgets()
        # Membuat/define hal-hal yang diperlukan fitur Selesai Gunakan Meja
        else:
            self.tab_num = tab_num
            self.total_price = self.orderlist[self.tab_num].get_total_price()
        
        # Membuat widget
        self.create_top_widgets()
        self.generate_table()
        self.create_bot_widgets()
        # Handle tombol close ditekan
        self.protocol("WM_DELETE_WINDOW", self.btn_back_clicked)

    def new_table_number(self, new_tabnum):
        # Method untuk mengupdate nomor meja di tampilan dan orderan
        self.orderlist[new_tabnum] = self.orderlist[self.tab_num]
        self.orderlist[self.tab_num] = 0
        self.tab_num = new_tabnum
        self.lbl_table["text"] = f"No. Meja: {self.tab_num+1}"

    def order_update(self, event):
        # Method untuk mengupdate jumlah pesanan dari combobox ke orderan
        for categ in self.data:
            for item in self.data[categ]:
                # Mengambil value semua combobox dalam iterasi, lalu update
                value = self.boxes[item.get_code()].get()
                # Update jika value combobox integer
                if value.isdigit():
                    self.orderlist[self.tab_num].set_orders(item, int(value))
        self.total_price = self.orderlist[self.tab_num].get_total_price()
        self.lbl_total["text"] = f"Total harga: {self.total_price}"

    def btn_ubah_clicked(self):
        # Method jika tombol ubah meja ditekan. Instansiasi class ModifyMeja
        # dengan opsi "ubah"
        ModifyMeja(self, self.data, self.orderlist,
                   self.tab_num, "ubah", self.master)

    def btn_back_clicked(self):
        # Method jika tombol kembali ditekan.
        if self.state == "buat":
            # Kosongkan meja jika opsi saat ini "buat"
            self.orderlist[self.tab_num] = 0
        self.destroy()

    def btn_ok_clicked(self):
        # Method jika tombol OK ditekan
        if self.state == "selesai":
            # Kosongkan meja jika opsi saat ini "selesai"
            self.orderlist[self.tab_num] = 0
            # Ubah warna meja menjadi abu abu pada window sebelumnya (ModifyMeja)
            self.window_parent.update_color(self.tab_num, "#b3b3b3")
            self.destroy()
        else:
            if self.orderlist[self.tab_num].get_total_price() == 0:
                tkmsg.showwarning(parent=self, title="Pesanan Kosong",
                                  message="Pesanan tidak boleh kosong!")
            else:
                self.destroy()
                self.window_parent.destroy()

    def create_buat_widgets(self):
        # Method yang membuat widget yang diperlukan untuk opsi "buat"
        self.btn_ubah = tk.Button(self, text="Ubah", width=5, bg="#4472C4",
                                  fg="white", command=self.btn_ubah_clicked)
        self.btn_ubah.grid(row=0, column=self.cols-1, pady=(0, 20), sticky="w")

    def create_top_widgets(self):
        # Method yang membuat widget bagian atas
        self.lbl_nama = tk.Label(self, text=f"Nama pemesan: {self.nama}")
        self.lbl_table = tk.Label(self, text=f"No. Meja: {self.tab_num+1}")

        self.lbl_nama.grid(row=0, column=0, pady=(0, 20), sticky="e")
        self.lbl_table.grid(row=0, column=self.cols-2,
                            pady=(0, 20), sticky="e")

    def generate_cell(self, row, col, data):
        # Method yang membuat satu cell tabel
        table_row = tk.Entry(self, width=20)
        if col == 0:
            # Padding di kiri jika kolom paling kiri
            table_row.grid(row=row, column=col, padx=(40, 0))
        elif col == self.cols-1:
            if self.state == "selesai":
                # Membedakan ukuran cell jumlah jika opsi "selesai"
                table_row["width"] = 25
            # Padding di kanan jika kolom paling kanan
            table_row.grid(row=row, column=col, padx=(0, 40))
        else:
            table_row.grid(row=row, column=col)
        # Memasukkan data dan 'lock' entry agar tidak bisa diubah
        table_row.insert(tk.END, data)
        table_row['state'] = 'readonly'

    def generate_table(self):
        # Method untuk membuat seisi tabel

        # Posisi baris tabel
        self.row_pos = 1    
        # Dict untuk "judul" tiap kolom
        self.addt_title = {"MEALS": "Kegurihan", "DRINKS": "Kemanisan",
                           "SIDES": "Keviralan"}
        values = tuple([k for k in range(10)])

        # Iterasi kategori menu
        for category in self.data:
            # List judul tiap kolom
            self.tbl_title = ["Kode", "Nama", "Harga",
                              self.addt_title[category], "Jumlah"]
            # Label kategori
            self.lbl_category = tk.Label(self, text=category)
            self.lbl_category.grid(row=self.row_pos, column=0)
            self.row_pos += 1

            # Generate satu baris berisi judul tiap kolom
            for i in range(len(self.tbl_title)):
                self.generate_cell(self.row_pos, i, self.tbl_title[i])
            self.row_pos += 1

            # Iterasi menu
            for menu in self.data[category]:
                # Temporary storing kode, nama, dan harga
                code, name, price = (
                    menu.get_code(), menu.get_name(), menu.get_price())
                self.details = [code, name, price]
                # Generate satu baris menu
                for j in range(len(self.details)):
                    self.generate_cell(self.row_pos, j, self.details[j])
                # Mencetak additional info sesuai masing-masing class
                if category == "MEALS":
                    self.generate_cell(self.row_pos, j+1, menu.kegurihan)
                elif category == "DRINKS":
                    self.generate_cell(self.row_pos, j+1, menu.kemanisan)
                else:
                    self.generate_cell(self.row_pos, j+1, menu.keviralan)

                # Mencetak combobox untuk input jumlah jika opsi "buat"
                if self.state == "buat":
                    self.boxes[code] = ttk.Combobox(self, values=values)
                    # Bind combobox jika ada perubahan nilai, jika enter pada
                    # keyboard ditekan, dan jika user input nilai dan focus out
                    self.boxes[code].bind(
                        '<<ComboboxSelected>>', self.order_update)
                    self.boxes[code].bind('<Return>', self.order_update)
                    self.boxes[code].bind('<FocusOut>', self.order_update)
                    self.boxes[code].current(0)
                    self.boxes[code].grid(
                        row=self.row_pos, column=j+2, padx=(0, 30))
                # Mencetak readonly entry berisi jumlah jika opsi "selesai"
                else:
                    self.generate_cell(
                        self.row_pos,
                        j+2,
                        self.orderlist[self.tab_num].get_item_quantity(menu)
                    )
                self.row_pos += 1

    def create_bot_widgets(self):
        # Mencetak widget bagian bawah dari window
        self.lbl_total = tk.Label(
            self, text=f"Total harga: {self.total_price}", font="Arial 12 bold")
        self.btn_back = tk.Button(self, text="Kembali", width=15,
                                  bg="#4472C4", fg="white", command=self.btn_back_clicked)
        self.btn_ok = tk.Button(
            self, text="OK", width=15, bg="#4472C4", fg="white", command=self.btn_ok_clicked)
        # Mengubah tulisan OK jadi Selesai jika saat ini opsi "Selesai"
        if self.state == "selesai":
            self.btn_ok["text"] = "Selesai"

        self.lbl_total.grid(row=self.rows, column=self.cols-1, sticky="w")
        self.btn_back.grid(row=self.rows+1, column=1, columnspan=2, pady=40)
        self.btn_ok.grid(row=self.rows+1, column=2, columnspan=2, pady=40)

class SelesaiGunakanMeja():
    # Class yang bertanggung jawab untuk fitur selesai gunakan meja
    def __init__(self, data, orderlist, master=None):
        self.master = master
        self.data = data
        self.orderlist = orderlist
        # Instansiasi class ModifyMeja dengan opsi "selesai"
        # tanpa memasukkan "parent" class dan nomor meja
        ModifyMeja(None, self.data, self.orderlist,
                   None, "selesai", self.master)

def main():
    """Fungsi utama menjalankan program"""

    # Deklarasi variabel
    menu = {"MEALS": [], "DRINKS": [], "SIDES": []}
    # Untuk memetakan class yang akan dipakai sesuai kategori
    menu_func = {"MEALS": Meals, "DRINKS": Drinks, "SIDES": Sides}
    # Untuk menyimpan tiap pesanan
    orderlist = [0 for _ in range(10)]

    # Membaca menu
    with open('menu.txt', 'r') as f:
        lines = f.read().splitlines()
        cur_key = ""
        for line in lines:
            if line[:3] == "===":
                cur_key = line[3:]
            else:
                item = line.split(";")
                menu[cur_key].append(menu_func[cur_key](
                    item[0], item[1], item[2], item[3]))

    # Instansiasi window tkinter
    window = tk.Tk()
    cafe = Main(menu, orderlist, window)
    window.mainloop()

if __name__ == '__main__':
    main()
