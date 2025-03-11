
nama_list =[]
jabatan_list=[]

for i in range(3):
    nama = input("masukan nama: ")
    nama_list.append(nama)

# for i in range(3):
#     jabatan = input("masukan jabatan: ")
#     jabatan_list.append(jabatan)

for nama in nama_list:
    print(nama[0])