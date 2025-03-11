nama = "stimik amik"

#cara print
print(nama)
print(nama[7:11])

for i in nama:
    print(i)
    #print(i, end="") #print kesamping

print("\n")
print(f"{nama}\n", end="")
print("".join(nama))


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
