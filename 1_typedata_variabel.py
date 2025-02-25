print('hallo stimik amik')
#membuat variabel
angka = 75 
nama = 'Keysia' # case sensitif
Nama = 'Gia'    # case sensitif
print(Nama)     # cetak output Nama

buah = ['apel','mangga','jeruk']         # list : bisa diubah 
hewan = ('kucing','kelinci','gajah')    # tuple : tidak bisa diubah
nilai = {70,80,80,80,90}                # set : unik
mahasiswa = {'nama':'Fariz','usia':20}  # dict : key - value

#untuk melihat tipe datanya
print(type(angka))
print(type(nama))
print(type(buah))
print(type(hewan))
print(type(nilai))
print(type(mahasiswa))
"""
QUIZ
hitung nilai akhir dengan ketentuan 
absen 10%, tugas 20%, uts 30%, uas 40%
"""
absen = 70
tugas = 80
uts = 90
uas = 100

nilaiAkhir = (absen * 0.1) + (tugas * 0.2) + (uts * 0.3) + (uas * 0.4)
print ('Nilai Akhir Adalah : ', nilaiAkhir)

