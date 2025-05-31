quiz='''
Buatlah sebuah kelas bernama Mahasiswa yang memiliki atribut berikut:

    1. nama (public) → nama siswa

    2. __nilai (private) → nilai siswa

Kelas tersebut harus memiliki:

    1. Method set_nilai(self, nilai) untuk mengatur nilai siswa (hanya nilai antara 0-100).

    2. Method get_nilai(self) untuk mengambil nilai siswa.

    3. Validasi: Jika nilai tidak dalam rentang 0-100, tampilkan pesan error.

'''

class Mahasiswa():
    def __init__(self, nama):
        self.nama = nama  #public
        self.__nilai = 0  #private

    def set_nilai(self, nilai):
        self.__nilai = nilai
        if 0 <= nilai <=100:
            print(f"Nilai yang diinput : {self.__nilai}")
        else:
            print("Error : Nilai harus rentang 0 - 100")
            print(f"Error :Nilai yang diinput : {self.__nilai}")
    
    # def __remedial(self):
    #     if self.__nilai <=60:
    #         print("Nilai Anda di remedial")
    #     else:
    #         print("Nilai anda cukup")
    
    def get_nilai(self):
        #self.__remedial()
        return self.__nilai
    
mhs = Mahasiswa("farhan")
mhs.set_nilai(160)

mhs.get_nilai()


        
    


    
