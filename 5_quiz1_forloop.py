ketentuan = """
1. buat inputan ganjil dan genap
2. jika ganjil munculkan tanggal ganjil di bulan maret (31 hari)
3. jika genap munculkan tanggal genap di bulan maret (31 hari)
4. jika berada di posisi tgl 20 munculkan pesan "Pembayaran THR"
4. jika berada di posisi tgl 29 munculkan pesan "Hari Raya nyepi"
5. jika berada di posisi tgl 31 munculkan pesan "Hari Raya Idul fitri"
"""

tanggal = input("masukan ganjil / genap : ")

if tanggal == "ganjil":
    for i in range(1,32):
        if i % 2 == 1: print(i)
        if i == 29 : print("Hari raya Nyepi")
        if i == 31 : print("Hari raya Idul fitri")
elif tanggal == "genap":
    for i in range(1,32):
        if i % 2 == 0: print(i)
        if i == 20 : print("Pembayaran THR")
else:
    print("Inputan tidak sesuai")        