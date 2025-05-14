quiz="""
1. buatlah sistem payroll sederhana menggunakan function
2. buatlah 4 function (gajiPokok, allowance, potongan, takeHomePay)
3. ketentuan gajipokok : 
   a. jika lamaKerja kurang dari 5 tahun maka gapok = 5juta
   b. jika lamaKerja 5 tahun atau lebih maka gapok = 10juta 
4. ketentuan allowance : 
   a. jika lamaKerja kurang dari 5 tahun maka tunjangan = 2juta
   b. jika lamaKerja 5 tahun atau lebih maka tunjangan = 4juta 
5. totalGaji = gapok + allowance
6. ketentuan potongan = '5%' dari total gaji
7. Output :
================================
masukan nama karyawan :Farhan
masukan lama kerja (tahun) : 7
================================
Nama Karyawan : Farhan
Gaji Pokok : 10000000
Tunjangan : 4000000
pph21 : 700000.0
================================
Total gaji adalah : 13300000.0
================================
"""

print("===============================")
nama = input("masukan nama karyawan :")
lamaKerja = int(input("masukan lama kerja (tahun) : "))

def gajiPokok(lamaKerja):
    if lamaKerja < 5 :
        gapok = 5000000
    else :
        gapok = 10000000
    return gapok

def allowance(lamaKerja):
    if lamaKerja < 5 :
        tunjangan = 2000000
    else :
        tunjangan = 4000000
    return tunjangan

def potongan(totalGaji):
    pajak = 0.05 * totalGaji
    return pajak

def takeHomePay():
    print("===============================")
    gp = gajiPokok(lamaKerja)
    tj = allowance(lamaKerja)
    hasil = gp + tj
    pph21 = potongan(hasil)
    totalGaji = hasil - pph21
    print(f"Gaji Pokok : {gp}")
    print(f"Tunjangan : {tj}")
    print(f"pph21 : {pph21}")
    print("================================")
    print(f"Total gaji adalah : {totalGaji}")
    print("================================")

takeHomePay()