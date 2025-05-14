class makhluk():
    def __init__(self, nama):
        self.nama = nama
    
    def patuh(self):
        print(f"{self.nama} adalah makhluk yang patuh")

    def angkuh(self):
        print(f"{self.nama} adalah makhluk yang angkuh")

#tanpa inheritance
# nur = makhluk("malaikat")
# nur.patuh()

class malaikat(makhluk):
#jika tidak menambah atau merubah sesuatu ga perlu __init__()
# gunakan pass
#    pass
#klau merubah /menambah maka gunakan __init__()
# gunakan super().__init__ agar tetap bisa mewarisi atribut & method dari class induknya
    def __init__(self, nama, asal):
        super().__init__(nama)
        self.asal = asal
        print(f"{self.nama} berasal dari {self.asal}")

nur = malaikat("\nMalaikat Ridwan","Cahaya")
nur.patuh()

class jin(makhluk):
    def __init__(self, nama, sifat):
        super().__init__(nama)
        self.sifat = sifat
        print(f"{self.nama} memiliki sifat {self.sifat}")

j = jin("Ifrit","sombong")
j.angkuh()