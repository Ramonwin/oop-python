''' Function adalah Function adalah blok kode yang bisa dipakai berulang-ulang.
 Kita bisa memanggilnya kapan saja tanpa harus menulis ulang kodenya.'''

#function ke 1
def hello():
    print("hallo semua")
    print("hallo semua")
    print("hallo semua")
    print("hallo semua")

hello()

#function ke-2 dengan argument atau parameter
def mahasiswa(nama):
    print(f"Nama Mahasiswa : {nama}")

mahasiswa("farhan")

#function ke-3 dengan return (mengembalikan data)
def salary(gapok, tunjangan):
    hasil = gapok + tunjangan
    return hasil

total = salary(5000000,1000000)
print(f"take home pay salary adalah : {total}")

#jika dicek lagi
print(total)

# fungsi ke-4
# perbedaan function menggunakan return dan yang menggunakan print()
# print() yaitu langsung menampilkan output ke layar, tapi tidak bisa digunakan lagi datanya
# Pakai print() kalau kamu cuma ingin melihat hasil (misalnya saat debugging atau testing)
# Pakai return kalau kamu ingin mengolah hasil lebih lanjut, atau membuat program yang modular.
def gaji(gapok, tunjangan):
    hasil = gapok + tunjangan
    print(f"gaji adalah : {hasil}")

#jika di cek lagi
total = gaji(4000000,500000)
print(total)

#fungsi ke-5, memanggil fungsi di dalam fungsi
def sapa():
    print("Halo!")

def sapa_user(nama):
    sapa()  # memanggil fungsi lain
    print(f"Selamat datang, {nama}!")

sapa_user("ramon")