from abc import ABC, abstractmethod

# Abstract Class
class MetodePembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass

# Subclass 1
class TransferBank(MetodePembayaran):
    def bayar(self, jumlah):
        print(f"Melakukan transfer bank sejumlah Rp{jumlah:,}")

# Subclass 2
class KartuKredit(MetodePembayaran):
    def bayar(self, jumlah):
        print(f"Melakukan pembayaran dengan kartu kredit sejumlah Rp{jumlah:,}")

# Subclass 3
class EWallet(MetodePembayaran):
    def bayar(self, jumlah):
        print(f"Melakukan pembayaran dengan e-wallet sejumlah Rp{jumlah:,}")

# Fungsi untuk memproses pembayaran
def proses_pembayaran(pembayaran: MetodePembayaran, jumlah):
    pembayaran.bayar(jumlah)

# Contoh Penggunaan
proses_pembayaran(TransferBank(), 500000)
proses_pembayaran(KartuKredit(), 250000)
proses_pembayaran(EWallet(), 100000)