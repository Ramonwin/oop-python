# while loop

# while kondisi:
#     aksi 1
#     aksi 2

# akhir dari program


#counted loop
angka = 1
print("angka sekarang =>", angka)
#print(f"angka sekarang => {angka}")

#counted loop
angka = 1
while angka <= 5:
        print("angka saat ini = ", angka)
        angka += 1

#uncounted loop

password = ""
while password != "1234":
        password = input("Masukkan password: ")
print("Password benar, Akses diterima!")

#infinite loop
while True:
        print("Hati -hati ini infinite loop, tidak akan berhenti!, kecuali pake break")  # Harus ada break agar bisa keluar


