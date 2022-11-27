class SegitigaSikuSiku:
    def __init__(self, alas, tinggi):
        self.alas = float(alas)
        self.tinggi = float(tinggi)
 
    def get_alas(self):
        return self.alas
 
    def get_tinggi(self):
        return self.tinggi
 
    def get_luas(self):
        return 1/2 * self.get_alas() * self.get_tinggi()