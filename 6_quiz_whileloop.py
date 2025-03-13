"""
Buatlah program sederhana
1. login sesuai username="admin" dan password=1234
2. jika berhasil input kode payroll
3. jika kode payroll 1, maka munculkan pesan "Gapok : Rp. 10.000.000
4. jika kode payroll 2, maka munculkan pesan "Gapok : Rp. 5.000.000
5. lalu munculkan pesan "selesai"
"""

username =""
password =""

while username != "admin" or password !=1234:
    username = input("masukan username : ")
    password = int(input("masukan password : "))
print("selamat datang")

kode_payroll = int(input("masukan kode payroll : "))
if kode_payroll == 1 :
    print("gapok : Rp. 10.000.000")
elif kode_payroll == 2 :
    print ("gapok : Rp 5.000.000")
else : 
    print("inputan tidak sesuai")

print("Selesai")