quiz='''
Buatlah sebuah kelas bernama Mahasiswa yang memiliki atribut berikut:

    1. nama (public) → nama siswa

    2. __nilai (private) → nilai siswa

Kelas tersebut harus memiliki:

    1. Method set_nilai(self, nilai) untuk mengatur nilai siswa (hanya nilai antara 0-100).

    2. Method get_nilai(self) untuk mengambil nilai siswa.

    3. Validasi: Jika nilai tidak dalam rentang 0-100, tampilkan pesan error.
'''

class mahasiswa():
    def __init__(self,nama):
        self.nama = nama
        self.__nilai = 0

    def set_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai = nilai
        else:
            print ("Error : Nilai harus diantara 0 - 100")

    def get_nilai(self):
        return self.__nilai
        
mhs = mahasiswa("Farhan")
# print(mhs.__nilai) ❌ AttributeError: 'Student' object has no attribute '__grade'

# Ini CARA YANG BENAR (pakai method) ✅

mhs.set_nilai(85)
print(mhs.get_nilai())
