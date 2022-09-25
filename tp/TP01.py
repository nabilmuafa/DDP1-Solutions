# Tugas Pemrograman 1 DDP 1 - Kelas H
# Program yang akan mencetak sebuah candi warna-warni
# dengan jumlah yang batu-bata per baris yang ditentukan
# pengguna
#
# Dikerjakan oleh Muhammad Nabil Mu'afa - 2206024972

import turtle as t
import random

#turtle setup
t.title("Candi Warna-Warni")
t.setworldcoordinates(-450, -450, 450, 450) # set skala kanvas
t.penup()
t.bgcolor("green") # set warna background
t.speed(0) #set kecepatan gambar

# meminta input jumlah bata bawah melalui GUI Turtle
jumlah_bata_bawah = int(t.numinput("Input Jumlah", "Selamat datang di Aplikasi Pembuat Candi!\n\n"+\
                                    "Masukkan jumlah batu-bata yang\nanda inginkan untuk lapisan " +\
                                    "paling bawah\n" +\
                                    "(Input nilai desimal akan dibulatkan kebawah): ",
                                    minval=1,
                                    maxval=25))

#meminta input jumlah bata atas melalui GUI Turtle
jumlah_bata_atas = int(t.numinput("Input Jumlah", "Masukkan jumlah batu-bata yang anda\ninginkan untuk lapisan " +\
                                  "atas\n" +\
                                  "(Input nilai desimal akan dibulatkan\nkebawah): ",
                                  minval=1,
                                  maxval=jumlah_bata_bawah))

panjang_bata = t.numinput("Input Ukuran", "Masukkan panjang satu buah batu-\nbata (dalam pixel/px): ",
                              minval=1, 
                              maxval=35)

lebar_bata = t.numinput("Input Ukuran", "Masukkan lebar satu buah batu-bata\n(dalam pixel/px): ",
                            minval=1,
                            maxval=25)

banyak_baris = abs(jumlah_bata_bawah - jumlah_bata_atas + 1) # menyimpan banyak baris yang akan dicetak
jumlah_total_bata = banyak_baris / 2 * (jumlah_bata_atas + jumlah_bata_bawah) # menyimpan total jumlah batu-bata (rumus jumlah suku)

# set up posisi menggambar
x_position = int(panjang_bata * jumlah_bata_bawah / -2)
y_position = int(lebar_bata * banyak_baris / -2)
t.goto(x_position, y_position) # membawa pulpen ke posisi awal
# Kolaborator untuk ide mencari posisi mulai gambar: Rafi Ardiel Erinaldi (KKI)

bata_per_baris = jumlah_bata_bawah
kiri = False # bernilai True jika Turtle menggambar dari kanan ke kiri, dan sebaliknya

# loop untuk menggambar batu-bata
for baris_bata in range(banyak_baris): # loop untuk iterasi baris
    for urutan_bata in range(bata_per_baris): # loop untuk iterasi bata per baris
        # akan fill dengan warna #BC4A3C jika di bawah/atas/pinggir candi
        if urutan_bata == 0 \
        or urutan_bata == bata_per_baris-1 \
        or baris_bata == 0 \
        or baris_bata == banyak_baris-1:
            t.fillcolor("#BC4A3C")
        else: # akan fill random jika batu-bata di tengah
            colors = "%06x" % random.randint(0, 0xFFFFFF)
            t.fillcolor("#"+colors)
        t.begin_fill()
        t.pendown()
        for _ in range(2): # loop gambar per kotak
            t.forward(panjang_bata)
            t.left(90) if not kiri else t.right(90) # pena belok ke kiri jika kiri = False, vice versa
            t.forward(lebar_bata)
            t.left(90) if not kiri else t.right(90)
        t.end_fill()
        t.penup()
        t.forward(panjang_bata)
    # berpindah ke baris diatasnya
    t.left(90) if not kiri else t.right(90)
    t.forward(lebar_bata)
    t.left(90) if not kiri else t.right(90)
    t.forward(panjang_bata/2)
    bata_per_baris -= 1 # karena naik satu baris, jumlah bata per baris berkurang 1
    kiri = not kiri # arah menggambar berubah

# menggambar tulisan jumlah candi
t.penup()
t.goto(0, t.ycor()-lebar_bata*(banyak_baris+2)) # ke posisi tengah bawah candi untuk menggambar
t.pendown()
t.write(f"Candi warna-warni dengan {int(jumlah_total_bata)} batu-bata", align="center", font=('Arial', '15', 'normal'))
t.exitonclick() # akan exit program baru ketika di klik
