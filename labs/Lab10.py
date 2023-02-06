import tkinter as tk
import tkinter.messagebox as tkmsg

class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Karung Ajaib")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        """Tombol menu utama"""
        self.label = tk.Label(self, \
                              text = 'Selamat datang Dek Depe di Karung Ajaib. Silahkan pilih Menu yang tersedia')

        self.btn_lihat_daftar_karung = tk.Button(self, \
                                                text = "LIHAT DAFTAR KARUNG", \
                                                command = self.popup_lihat_karung)
        self.btn_masukkan_item = tk.Button(self, \
                                            text = "MASUKKAN ITEM", \
                                            command = self.popup_add_item)
        self.btn_keluarkan_item = tk.Button(self, \
                                        text = "KELUARKAN ITEM", \
                                        command = self.popup_keluarkan_item)
        self.btn_exit = tk.Button(self, \
                                  text = "EXIT", \
                                  command = self.master.destroy)

        self.label.pack()
        self.btn_lihat_daftar_karung.pack()
        self.btn_masukkan_item.pack()
        self.btn_keluarkan_item.pack()
        self.btn_exit.pack()

    # semua item dalam karung
    def popup_lihat_karung(self):
        PopupLihatKarung(self.master)

    # menu masukkan item
    def popup_add_item(self):
        PopupAddItem(self.master)

    # menu keluarkan item
    def popup_keluarkan_item(self):
        PopupKeluarkanItem(self.master)

class PopupLihatKarung(tk.Toplevel):
    def __init__(self,master):
        super().__init__(master)
        self.geometry("280x200")
        self.wm_title("Lihat Karung")

        self.title = tk.Label(self, text='Daftar Karung Ajaib')
        self.nama = tk.Label(self, text='Nama Item')
        self.title.pack()
        self.nama.pack()

        # Tampilkan halaman lihat karung ajaib dengan melihat set
        self.count = 1
        for i in sorted(list(item_set)):
            self.item_list = tk.Label(self, text=f"{self.count}. {i}")
            self.item_list.pack()
            self.count += 1

        self.exit_button = tk.Button(self, text="EXIT", command = self.destroy)
        self.exit_button.grid()
    
# Class Masukkan Item 
class PopupAddItem(tk.Toplevel):
    
    def __init__(self,master):
        super().__init__(master)
        self.wm_title("Masukkan item")
        self.geometry("280x100")
        self.nama_item = tk.StringVar()

        self.title = tk.Label(self, text='Input Masukkan Item')
        self.lbl_item = tk.Label(self, text='Nama Item')
        self.ent_item = tk.Entry(self, textvariable=self.nama_item)

        self.title.grid(row=0, column=1)
        self.lbl_item.grid(row=1, column=0)
        self.ent_item.grid(row=1, column=1)

        self.submit_button = tk.Button(self, text = 'Masukkan', command = self.masukkan_item)
        self.submit_button.grid(row=2, column=1)

    def masukkan_item(self):
        """Memasukkan item ke dalam set"""
        if self.nama_item.get() in item_set:
            # Print warning jika item sudah ada di set
            tkmsg.showwarning(
                title="ItemHasFound",
                message=f"Item dengan nama {self.nama_item.get()} sudah " + \
                        f"ada di dalam KarungAjaib. Item {self.nama_item.get()} tidak " + \
                        f"bisa dimasukkan lagi."
            )
        else:
            item_set.add(self.nama_item.get())
            tkmsg.showinfo(
                title="Berhasil!",
                message=f"Berhasil memasukkan item {self.nama_item.get()}")
        self.destroy()

    
# Class Keluarkan Item
class PopupKeluarkanItem(tk.Toplevel):
    
    def __init__(self, master):
        super().__init__(master)
        self.wm_title("Keluarkan item")
        self.geometry("280x100")
        self.nama_item = tk.StringVar()

        self.title = tk.Label(self, text='Input Keluarkan Item')
        self.lbl_item = tk.Label(self, text='Nama Item')
        self.ent_item = tk.Entry(self, textvariable=self.nama_item)

        self.title.grid(row=0, column=1)
        self.lbl_item.grid(row=1, column=0)
        self.ent_item.grid(row=1, column=1)

        self.submit_button = tk.Button(self, text = 'Ambil', command = self.keluarkan_item)
        self.submit_button.grid(row=2, column=1)

    def keluarkan_item(self):
        """Mengeluarkan item dari set"""
        if self.nama_item.get() not in item_set:
            # Print error jika item tidak ditemukan di dalam set
            tkmsg.showwarning(
                title="ItemNotFound",
                message=f"Item dengan nama {self.nama_item.get()} " + \
                "tidak ditemukan di dalam KarungAjaib.")
        else:
            item_set.remove(self.nama_item.get())
            tkmsg.showinfo(
                title="Berhasil!",
                message=f"Berhasil mengeluarkan item {self.nama_item.get()}")
        self.destroy()
                  
item_set = set()
if __name__ == "__main__":
    root = tk.Tk()
    m=MainWindow(root)
    root.mainloop()