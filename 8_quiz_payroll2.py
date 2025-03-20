quiz="""
1. buatlah program sederhana payroll dengan python
2. buat variable gapok = Rp. 10jt
3. buat inputan 3x, dan tampung dulu untuk (nama, jabatan)
4. jika kode jabatan 1 maka tunjangan = Rp 5jt
5. jika kode jabatan 2 maka tunjangan = Rp 3jt
6. jika selain kode diatas munculkan pesan "kode jabatan tidak sesuai"
7. total gaji = gapok + tunjangan
8. tampilkan nama & total gaji
"""

gapok = 10000000
data_karyawan =[] # List untuk menyimpan data karyawan

for i in range(3):
    nama = input("masukan nama : ")
    kode_jabatan = int(input("masukan kode_jabatan : "))

    if kode_jabatan == 1:
        tunjangan = 5000000
    elif kode_jabatan == 2:
        tunjangan = 3000000
    else :
        tunjangan = 0
        print("kode tidak sesuai")
        #continue 
        #skip iterasi jika kode jabatan tidak valid
    
    total_gaji = gapok + tunjangan
    data_karyawan.append((nama, total_gaji)) #Menambahkan data tuple (nama,total_gaji) sebagai satu elemen ke dalam list
    
print("\nData Payroll Karyawan :")
for nama, total_gaji in data_karyawan:
    print(f"Nama : {nama}")
    print(f"Total gaji : {total_gaji:,}") # `{total_gaji:,}` akan menambahkan pemisah ribuan
    print("============================")





