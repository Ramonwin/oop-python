quiz ="""
1. Beri nilai untuk variabel nilai Total cuti tahunan 12 hari & cuti bersama 4 hari
2. Input Dinamis pengajuan cuti
3. maksimal ambil cuti adalah 3 hari
4. Hitung total sisa cuti, dan munculkan pesan sisa cuti adalah : ....
5. total sisa cuti = total cuti tahunan - cuti bersama - pengajuan cuti
6. Jika pengajuan cuti lebih dari 3 hari, munculkan pesan
 "Maaf tidak bisa,pengajuan melebihi batas maksimal"
"""

# Jawaban Quiz
totCuti = 12
cutBer = 4

ambilCuti = int(input("Masukan pengajuan cuti : "))

if ambilCuti == 1:
    sisaCuti = totCuti - cutBer - ambilCuti
    print("Sisa cuti adalah : " , sisaCuti)
elif ambilCuti == 2:
    sisaCuti = totCuti - cutBer - ambilCuti
    print("Sisa cuti adalah : " , sisaCuti)
elif ambilCuti == 3 :
    sisaCuti = totCuti - cutBer - ambilCuti
    print("Sisa cuti adalah : " , sisaCuti)
else :
    print("Maaf tidak bisa, pengajuan melebihi batas maksimal")
