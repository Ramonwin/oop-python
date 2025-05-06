class makhluk():
    def __init__(self, nama):
        self.nama = nama

    def patuh(self):
        print(f"{self.nama} adalah makhluk yang patuh")

    def angkuh(self):
        print(f"{self.nama} adalah makhluk yang angkuh")
        

class malaikat(makhluk):
    # jika tidak ingin mengubah atau menambahkan apapun, maka tidak perlu menggunakan __init__
    # class anak bisa menggunakan lgsg constructor yg ada di class induk
    # gunakan "pass"
    #pass 

    # kalau ingin mengubah atau menambahkan sesuatu
    # maka subclass harus definisikan __init__() dan
    # memanggil super().__init__() supaya tetap mewarisi inisialisasi dari induk.
    def __init__(self, nama, asal):
        super().__init__(nama)
        self.asal = asal
        print(f"{self.nama} terbuat dari {self.asal}")

class jin(makhluk):
    def __init__(self, nama, sifat):
        super().__init__(nama)
        self.sifat = sifat

    def menggoda(self):
        print(f"{self.nama} punya sifat {self.sifat} dan juga suka menggoda")


class manusia(jin):
    def __init__(self, nama, sifat, akal):
        super().__init__(nama, sifat)
        self.akal = akal


nur = malaikat("malaikat","cahaya")
nur.patuh()

jin = jin("syaiton","sombong")
jin.angkuh()
jin.menggoda()

m = manusia("Fulan","Labil", "Cerdas")
m.menggoda()


