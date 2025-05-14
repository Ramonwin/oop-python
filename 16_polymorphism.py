teks = '''
Polymorphism : berasal dari kata poly (banyak) dan morph (bentuk) => banyak bentuk

dalam konsep OOP : sebuah prinsip bahwa class dapat memiliki banyak bentuk method yang
berperilaku beda walaupun namanya sama
'''

class pkwt():
    def biodata(self):
        print('Saya pegawai kontrak')

class pkwtt():
    def biodata(self):
        print('Saya adalah pegawai tetap')

septi = pkwt()
okta = pkwtt()

# septi.biodata()
# okta.biodata()

for pegawai in (septi, okta):
    pegawai.biodata()


nilaiUMP = 2500000
inflasi = 0.1
alfa = 0.2

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

class umk_pwk(ump):
    def finalUMK(self):
        ped = 2000000
        hasil = self.hitungUmk() + ped
        print(f"FInal UMK kota Bogor adalah : {hasil}")
    
cmh = umk_cmh(nilaiUMP,inflasi,alfa)
bdg = umk_bdg(nilaiUMP,inflasi,alfa)
pwk = umk_pwk(nilaiUMP,inflasi,alfa)

for umk_kota in (cmh,bdg,pwk):
    umk_kota.finalUMK()