def rekap_matkul_npm(data_nilai):
    # Initialisasi dictionary kosong
    matkul_recap = dict()
    # Iterasi data input
    for npm, matkul, grade in data_nilai:
        # Jika key matkul belum ada di dictionary, akan membuat key baru
        # dengan value list kosong
        if matkul not in matkul_recap:
            matkul_recap[matkul] = []
        # Menambahkan npm ke key matkul yang sudah ada
        matkul_recap[matkul].append(npm)
 
    return matkul_recap