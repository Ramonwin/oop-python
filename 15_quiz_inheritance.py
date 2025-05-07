quiz = """
1. buatlah perhitungan UMK sesuai UMP yang ada di propinsi tersebut
2. buatlah class induk UMP() dengan atribut : nilaiUMP, inflasi, index alfa
3. buatlah method hitung_nilai_umk() di class UMP
4. rumus umk = ump + (ump * (inflasi + alfa))
5. buatlah class anak "UMK()" yang mewarisi class induk "UMP()"
6. tambahan atribut pertumbuhan_ekonomi_daerah di class UMK()
7. final umk = umk + (umk * pertumbuhan_ekonomi_daerah)
8. tampilkan nilai UMK di kota tersebut

keterangan : nilai ump = 2,5juta
            inflasi = 10%
            index alfa = 20%
            pertumbuhan ed = 7%    
"""
nilaiUMP = 2500000
inflasi = 0.1
alfa = 0.2
ped = 0.07
class ump():
    def __init__(self, nilaiUMP, inflasi, alfa):
        self.nilai = nilaiUMP
        self.inflasi = inflasi
        self.alfa = alfa

    def hitung_umk(self):
        nilai = (self.nilai) + (self.nilai * (self.inflasi + self.alfa))
        return nilai

class umk(ump):
    def __init__(self, nilaiUMP, inflasi, alfa, ped):
        super().__init__(nilaiUMP, inflasi, alfa)
        self.ped = ped
    
    def finalUMK(self):
        final = self.hitung_umk() + (self.hitung_umk() * self.ped)
        print(f"final umk Bandung : {final}")
        
nilaiSub = ump(nilaiUMP,inflasi,alfa)
print(f"subtotal umk : {nilaiSub.hitung_umk()}")

nilaiFinal = umk(nilaiUMP,inflasi,alfa,ped)
nilaiFinal.finalUMK()







