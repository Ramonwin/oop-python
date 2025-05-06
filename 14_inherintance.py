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



nur = malaikat("malaikat","cahaya")
nur.patuh()




# jin = makhluk("syaiton")
# jin.angkuh()



