class bankAccount():
    def __init__(self, nama, balance):
        self.nama = nama            #public (bebas akses, dari luar, subclass)
        # self.balance = balance      #public
        # self._balance = balance     # protected (internal / subclass)
        self.__balance = balance    # private (enkapsulasi penuh)
    
    def set_deposit(self, amount): #setter
        if amount >10000 :
            self.__balance += amount
            print(f"Deposit berhasil, saldo sekarang : {self.__balance}")
        else:
            print("Deposit minimal Rp. 10.000")
    
    def set_withdraw(self, amount): #setter
        if 50000 <= amount <= self.__balance:
            self.__balance -= amount
            print(f"withdraw berhasil, sisa saldo : {self.__balance}")
        else :
            print("Saldo Tidak cukup / Penarikan minimal Rp. 50.000")
    
    def get_balance(self): #getter
        return self.__balance
    
#buat objek
rekening = bankAccount("Farhan",1000000)

#akses method publik
rekening.deposit(500000)
rekening.withdraw(300000)

#akses balance cara yg benar
print(f"Saldo Akhir adalah : {rekening.get_balance()}")

# cara yang salah 
#print(rekening.self__balance)