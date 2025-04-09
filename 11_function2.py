def nilaiAkhir (absen, tugas, uts, uas):
    na = absen + tugas + uts + uas
    print(na)

hasil = nilaiAkhir(10, 20, 30, 35)
print(hasil)
print(hasil)
print(hasil)
print(hasil)
print(hasil)
print(hasil)
print(hasil)
print("========================================")

def nilaiAkhir (absen, tugas, uts, uas):
    na = absen + tugas + uts + uas
    return na

hasil = nilaiAkhir(10, 20, 30, 35)
print(hasil)
print(hasil)
print(hasil)
print(hasil)
print(hasil)
print(hasil)
print(hasil)
print("========================================")

def bem():
    nama = ["gia","melinda","nita","okta"]
    print(nama)

print("perkenalkan kami dari BEM :")
cek = bem()
print(cek)
print(cek)
print(cek)
print("========================================")

def bem():
    nama = ["gia","melinda","nita","okta"]
    for i in nama:
        print(i)
    return nama

print("perkenalkan kami dari BEM :")
cek = bem()
print(cek)
print(cek)
print(cek)
print("========================================")


    
def himsi(nama):
    print(f"Nama saya : {nama}")

def kemahasiswaan():
    print ("hai perkenalan kami dari BEM")
    hasil = bem()
    print(hasil)
    print("===============================")
    print ("hai perkenalan kami dari HIMSI")
    bem()
    print("===============================")

kemahasiswaan()

print("========================================")