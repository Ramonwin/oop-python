#membuat class
class unggas:
    #pass #pernyataan kosong. Artinya: Python akan melewati baris itu tanpa melakukan apa-apa
    #__init__ Konstruktor, fungsi yang dipanggil saat objek dibuat
    #self : Referensi ke objek itu sendiri
    def __init__(self, inputnama, inputsayap, inputcakar):
        self.nama = inputnama
        self.sayap = inputsayap
        self.cakar = inputcakar

    def terbang(self):
        print(f"burung {self.nama} terbang menggunakan {self.sayap} dan mencengkram menggunakan {self.cakar}")


#buat objek
burung = unggas("Elang","2 Sayap","Cakar Tajam")
burung.terbang()


class persegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitungLuas(self):
        Luas = self.panjang * self.lebar
        print(f"Luas Persegi Panjang adalah : {Luas}")

pp = persegiPanjang(10,5)
pp.hitungLuas()

