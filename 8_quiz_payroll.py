quiz="""
1. buatlah program sederhana payroll dengan ketentuan
2. buat variable gapok = Rp. 10jt
3. buat inputan 2x untuk (nama, jabatan)
4. jika kode jabatan 1 maka tunjangan = Rp 5jt
5. jika kode jabatan 2 maka tunjangan = Rp 2jt
6. jika selain kode diatas munculkan pesan "kode jabatan tidak sesuai"
7. total gaji = gapok + tunjangan
8. tampilkan nama & total gaji
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

