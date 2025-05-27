teks = '''
Encapsulation (enkapsulasi) adalah prinsip OOP yang menyembunyikan detail internal suatu objek dari luar.
Jadi, data atau method tertentu tidak bisa diakses secara langsung dari luar kelas,
hanya bisa lewat method tertentu.

Tujuannya: Melindungi data, Membatasi akses langsung ke properti/atribut objek, Mempermudah pemeliharaan kode.
'''

class bankAccount():
    #saldo awal
    #deposit
    #withdraw
    #saldoAkhir
    #tipe akses / access modifier
    #getter & setter
    def __init__(self,nama, balance):
        self.nama = nama            #public
        # self.balance = balance    #public
        # self._balance = balance   #protected
        self.__balance = balance    #private
        
    def deposit(self, amount):
        if amount > 10000:
            self.__balance += amount
            print(f"Deposit berhasil, saldo sekarang : {self.__balance}")
        else:
            print("Deposit minimal harus Rp 10.000")
    
    def withdraw(self, amount):
        if 0 <= amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw berhasil, sisa saldo : {self.__balance}")
        else:
            print("Maaf Saldo Anda Tidak Cukup")
    
    def get_balance(self):
        return self.__balance
    
#buat objek rekening
rekening = bankAccount("Sarah",1000000)

# mengakses method publik / setter
rekening.deposit(500000)
rekening.withdraw(200000)

# Mengakses saldo dengan cara benar
print(f"saldo saat ini : {rekening.get_balance()}")

# Mengakses saldo dengan cara yang salah ❌ akses atribut private secara langsung (tidak disarankan)
#print(rekening.__balance);

# Bisa diakali (tapi jangan dilakukan): 
#print(rekening._bankAccount__balance)  # ⛔ Bisa, tapi ini melanggar encapsulation
