username = ""
password = ""
while username !="admin" or password != "1234":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
print("Akses diterima!")

kode_payroll = int(input("Masukkan kode payroll:  "))
if kode_payroll == 1:
        print("gapok : 10.000.000")
elif kode_payroll == 2:
        print("gapok : 5.000.000")
else :
        print("inputan tidak sesuai")
print("selesai")