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
        if i % 2 == 1:
            if i == 29 : print(i, "Hari raya Nyepi")
            elif i == 31 : print(i, "Hari raya Idul fitri")
            else: print(i)
elif tanggal == "genap":
    for i in range(1,32):
        if i % 2 == 0:
            if i == 20 : print(i,"Pembayaran THR")
            else: print(i)
else:
    print("Inputan tidak sesuai")        