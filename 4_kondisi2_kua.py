latihan ="""
    1. Input Usia
    2. Jika Usia 21 atau lebih munculkan pesan "Boleh Menikah"
    3. Jika Usia dibawah 21 munculkan pesan "Boleh Menikah + Surat izin Ortu"
    4. jika usia dibawah 15 "Belum Boleh, Sekolah dulu Dek"
"""

usia = int(input("masukan usia : "))
if usia >= 21 :
    print("Boleh Menikah")
elif usia >=15 :
    print("Boleh Menikah + Surat izin orangtua")
else :
    print ("Maaf belum boleh, sekolah dulu dek")
