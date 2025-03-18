#akses nilai list
list1 = ["python","javascript","php",1993,2021]
list2 = [1,2,3,4,5]

print(list1)
print(list2)
print(list1[1])
print(list2[1:5])

#update nilai list
list1[4] = 2025
print ("nilai list1 index ke-4 yang telah di ubah : ", list1[4])
print ("nilai keseluruhan list1 : ", list1)

#hapus nilai list
del list1[3]
print ("nilai list 1, setelah dihapus : ", list1)

#insert nilai list
list1.append("C++")
print ("nilai list1 yang sudah ditambahkan : ", list1)

#akses & insert menggunakan looping
#1. akses
for i in list1 :
    print ("looping list1 :", i)

#2. insert
list_kosong =[]
for i in range(11):
    list_kosong.append(i)
print("list yg sudah ditambahkan use loop:", list_kosong)

