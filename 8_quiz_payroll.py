quiz="""


"""

gapok = 10000000
for i in range(2):
    nama = input("masukan nama: ")
    jabatan = int(input("masukan jabatan: "))
    if jabatan == 1:
        total_gaji = gapok + 5000000
        print ("Nama :", nama, "-- Total gaji :", total_gaji)
        print ("===========================================")
    elif jabatan == 2:
        total_gaji = gapok + 2000000
        print ("Nama :", nama, "-- Total gaji :", total_gaji)
        print ("===========================================")
    else:
        print("kode jabatan tidak sesuai")
        print ("===========================================")

