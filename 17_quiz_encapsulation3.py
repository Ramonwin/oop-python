quiz='''
tambahan :
    1. tambahkan class __bungaKPR(private) -> bunga 15%
    2. tambahkan class potongan(public) dengan ketentuan :
        cicilan = amount + bungaKPR * amount
    3. tampilkan pesan : cicilan sebesar Rp.....
    4. Saldo akhir = Saldo terakhir - cicilan
    5. tampilkan pesan : saldo saat ini sebesar Rp.....
'''

class bankAccount():
    def __init__(self, nama, balance):
        self.nama = nama            #public (bebas akses luar class maupun subclass)
        # self.balance = balance    #public
        # self._balance = balance   #protected (untuk internal / subclass)
        self.__balance = balance    #private (enkapsulasi penuh)
        
    def deposit(self, amount):
        if amount > 10000:
            self.__balance += amount
            print(f"Deposit berhasil, saldo sekarang : {self.__balance}")
        else:
            print("Deposit minimal harus Rp 10.000")
    
    def withdraw(self, amount):
        if 50000 <= amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw berhasil, sisa saldo : {self.__balance}")
        else:
            print("Maaf Saldo Anda Tidak Cukup / Minimal Withdraw Rp 50.000")

    def __bungaKPR(self):
        bunga = 0.15
        return bunga
    
    def potongan(self, amount):
        cicilan = amount + (amount * self.__bungaKPR())
        return cicilan

    def get_balance(self):
        self.__balance -= self.potongan(amount=4000000)
        return self.__balance
    
#buat objek rekening
rekening = bankAccount("Sarah", 100000)

# mengakses method publik / setter
rekening.deposit(5000000)
rekening.withdraw(300000)

# Mengakses saldo dengan cara benar
print(f"Potongan Cicilan KPR : {rekening.potongan(4000000)}")
print(f"saldo saat ini : {rekening.get_balance()}")


