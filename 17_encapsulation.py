class bankAccount():
    def __init__(self, nama, balance):
        self.nama = nama            #public (bebas akses)
        # self.balance = balance    #public
        # self._balance = balance   #protected (untuk internal / subclass)
        self.__balance = balance    #private (enkapsulasi penuh)
        
    def deposit(self, amount):
        if amount > 10000:
            self.__balance += amount
            print(f"Deposit berhasil, saldo sekarang : {self.__balance}")
        else:
            print("Deposit minimal Rp. 10.000")
    
    def withdraw(self, amount):
        if 0 <= amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw berhasil, sisa saldo : {self.__balance}")
        else:
            print("Maaf Saldo Anda Tidak Cukup")
    
    def get_balance(self): #getter
        return self.__balance
    
#buat objek
rekening = bankAccount("Farhan",1000000)

#akses method publik
rekening.deposit(500000)
rekening.withdraw(300000)

#akses balance cara yg benar
print(f"Saldo Akhir adalah : {rekening.get_balance()}")

# Mengakses saldo dengan cara yang salah ❌ akses atribut private secara langsung (tidak disarankan)
#print(rekening.__balance);

# Bisa diakali (tapi jangan dilakukan): 
#print(rekening._bankAccount__balance)  # ⛔ Bisa, tapi ini melanggar encapsulation
