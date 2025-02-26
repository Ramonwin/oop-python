# Jawaban Quiz
apbn = 40000000000
anggaran = 15000

data = input("masukan kategori : ")
if data == "sd" :
    total = 3000000 * 15000
elif data == "smp" :
    total = 2000000 * 15000
elif data == "sma" :
    total = 1000000 * 15000
else :
    total = 0

if total > apbn :
    print("total biaya :", total)
    print("anggaran  APBN :", apbn)
    print("anggaran kurang")
else:
    print("total biaya :", total)
    print("anggaran  APBN :", apbn)
    print("anggaran cukup")
























