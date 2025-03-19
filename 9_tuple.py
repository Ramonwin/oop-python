# Fitur .count()
print(">>> Fitur .count()")
tuple_score = ('Sarah', 'Septi', 'Okta', 'Sarah', 'Sarah', 'Haris', 'haris')
score_budi = tuple_score.count('Sarah')
score_sud = tuple_score.count('Haris')
print(score_budi) # akan menampilkan output 4
print(score_sud) # akan menampilkan output 3

# Fitur .index()
print(">>> Fitur .index()")
tuple_score = ('Sarah', 'Septi', 'Okta', 'Sarah', 'Sarah', 'Haris', 'haris')
score_pertama_sud = tuple_score.index('haris')
print(score_pertama_sud) # akan menampilkan output 2

#akses nilai tuple
tuple1 = ('python','golang','php',1993,2021)
print (tuple1)

#cara seperti ini tidak bisa dilakukan, karena pada prinsipnya 
#tuple bersifat immutable (tidak dapat diubah nilainya setelah dibuat)
#namun ada cara alternatif yaitu dengan cara menggabungkan melalui variable baru

# tuple1[1] = 'TypeScript'
# print(tuple1) 

tuple2 = ('TypeScript','JavaScript')
tuple3 = tuple1 + tuple2
print(tuple3)



