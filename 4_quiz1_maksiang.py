quiz= """
## Buatlah program makan siang gratis dengan ketentuan
1. buat 3 kategori pilihan SD, SMP, SMA (input dinamis)
2. jika SD : kuota sebanyak 3.000.000 siswa
3. jika SMP : kuota sebanyak 2.000.000 siswa
4. jika SMA : kuota sebanyak 1.000.000 siswa
5. anggaran per siswa sebesar Rp. 15.000
6. anggaran dari APBN Rp. 40 Milliar
7. hitunglah total biaya per kategori => jumlah siswa * anggaran persiswa
8. jika anggaran APBN kurang dari total biaya,
    munculkan pesan "Anggaran kurang"
9. jika anggaran APBN Lebih dari total biaya,
    munculkan pesan "Anggaran cukup"
10. tampilkan total biaya, anggaran APBN, dan pesan
"""

# Jawaban Quiz
apbn = 40000000000
anggaran = 15000

data = input("masukan kategori : ")
if data == "sd":
    total = 3000000 * 15000
elif data == "smp":
    total = 2000000 * 15000
elif data == "sma":
    total = 1000000 * 15000
else:
    total = 0

if total > apbn:
    print("total biaya :", total)
    print("anggaran  APBN :", apbn)
    print("anggaran kurang")
else:
    print("total biaya :", total)
    print("anggaran  APBN :", apbn)
    print("anggaran cukup")