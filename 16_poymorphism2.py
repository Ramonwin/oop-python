teks ='''
Polymorphism : berasal dari kata Poly (banyak) dan morph (bentuk) => banyak bentuk

dalam konsep OOP : prinsip bahwa class bisa memiliki banyak bentuk method yg berperilaku
berbeda meskipun nama nya sama
'''
class pkwt():
    def status(self):
        print("Pegawai Kontrak")

class pkwtt():
    def status(self):
        print("Pegawai Tetap")

septi = pkwt()
okta = pkwtt()

for pegawai in (septi, okta):
    pegawai.status()

nilaiUMP = 2500000
inflasi = 0.1
alfa = 0.2
ped = 0.07

class ump():
    def __init__(self,nilaiUMP,inflasi,alfa):
        self.nilaiUMP = nilaiUMP
        self.inflasi = inflasi
        self.alfa = alfa
        
    def hitungUmk(self):
        umkDasar = self.nilaiUMP + (self.nilaiUMP * (self.inflasi + self.alfa))
        return umkDasar


class umk_cmh(ump):
    def finalUMK(self):
        ped = 500000
        hasil = self.hitungUmk() + ped
        print(f"FInal UMK kota Cimahi adalah : {hasil}")

class umk_bdg(ump):
    def finalUMK(self):
        ped = 1000000
        hasil = self.hitungUmk() + ped
        print(f"FInal UMK kota Bandung adalah : {hasil}")

class umk_bogor(ump):
    def finalUMK(self):
        ped = 1500000
        hasil = self.hitungUmk() + ped
        print(f"FInal UMK kota Bogor adalah : {hasil}")

cimahi = umk_cmh(nilaiUMP,inflasi,alfa)
bandung = umk_bdg(nilaiUMP,inflasi,alfa)
bogor = umk_bogor(nilaiUMP,inflasi,alfa)

for umk_kota in (cimahi, bandung, bogor):
    umk_kota.finalUMK()

