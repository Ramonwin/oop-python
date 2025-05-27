teks = '''
Encapsulation (enkapsulasi) adalah prinsip OOP yang menyembunyikan detail internal suatu objek dari luar.
Jadi, data atau method tertentu tidak bisa diakses secara langsung dari luar kelas,
hanya bisa lewat method tertentu.

Tujuannya: Melindungi data, Membatasi akses langsung ke properti/atribut objek, Mempermudah pemeliharaan kode.
'''
class BankAccount:
    def __init__(self, name, balance):
        self.name = name            # public
        self.__balance = balance    # private (tidak bisa langsung diakses)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit berhasil. Saldo baru: {self.__balance}")
        else:
            print("Jumlah deposit harus lebih dari 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Penarikan berhasil. Saldo baru: {self.__balance}")
        else:
            print("Penarikan gagal. Dana tidak cukup atau jumlah tidak valid.")

    def get_balance(self):
        return self.__balance

# Membuat objek rekening
akun = BankAccount("Sarah", 1000)

# Mengakses method publik
akun.deposit(500)
akun.withdraw(300)

# Mengakses saldo dengan cara benar
print("Saldo akhir:", akun.get_balance())

# Coba akses atribut private secara langsung (tidak disarankan)
#print(akun.__balance)  # ❌ Akan error

# Bisa diakali (tapi jangan dilakukan): 
#print(akun._BankAccount__balance)  # ⛔ Bisa, tapi ini melanggar encapsulation
