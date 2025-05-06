class makhluk():
    def __init__(self,nama):
        self.nama = nama

    def patuh(self):
        print(f"{self.nama} adalah makhluk yang patuh")

    def angkuh(self):
        print(f"{self.nama} adalah makhluk yang angkuh")

#tanpa inheritance
nur = makhluk("malaikat")
nur.patuh()

class malaikat(makhluk):
# kalau tidak ingin mengubah atau menambahkan sesuatu
# maka tidak perlu menggunakan  __init__()
# gunakanlah "pass"
#      pass

# mkt = malaikat("Malaikat Ridwan")
# mkt.patuh()

# jika ingin mengubah atau menambahkan sesuatu
# subclass haru menggunakan __init__() dan 
# super().__init__ agar tetap bisa mewarisi inisialisasi dari class induk

    def __init__(self, nama, asal):
        super().__init__(nama)
        self.asal = asal
        print(f"{self.nama} berasal dari {self.asal}")

mkt = malaikat("Malaikat Ridwan","cahaya")
mkt.patuh()

class jin(makhluk):
    def __init__(self, nama,sifat):
        super().__init__(nama)
        self.sifat= sifat
        print(f"{self.nama} mempunyai sifat {self.sifat} ")

j = jin("Syaiton","Sombong")
j.angkuh()