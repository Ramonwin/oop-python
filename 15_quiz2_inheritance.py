quiz = """
1. buatlah perhitungan UMK sesuai UMP yang ada di propinsi tersebut
2. buatlah class induk UMP() dengan atribut : nilaiUMP, inflasi, index alfa
3. buatlah method hitung_nilai_umk() di class UMP
4. rumus umk = ump + (ump * (inflasi + alfa))
5. buatlah class anak "UMK()" yang mewarisi class induk "UMP()"
6. tambahan atribut pertumbuhan_ekonomi_daerah di class UMK()
7. final umk = umk + (umk * pertumbuhan_ekonomi_daerah)
8. tampilkan nilai UMK di kota tersebut
9. Input nilai konsumsi perkapita
10. Buatlah Class BatasAtas
10. tentukan nilai batas atas dengan ketentuan
    BatasAtas = Final_UMK + (Final_UMK * Konsumsi_perKapita)
11. tampilkan pesan "Batas Maksimal nilai UMK kota Bandung Adalah : BatasAtas"

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
    def __init__(self,nilaiUMP,inflasi,alfa):
        self.nilaiUMP = nilaiUMP
        self.inflasi = inflasi
        self.alfa = alfa
        
    def hitungUmk(self):
        umkDasar = self.nilaiUMP + (self.nilaiUMP * (self.inflasi + self.alfa))
        return umkDasar


class umk(ump):
    def __init__(self, nilaiUMP, inflasi, alfa, ped):
        super().__init__(nilaiUMP, inflasi, alfa)
        self.ped = ped

    def finalUMK(self):
        hasil = self.hitungUmk() + (self.hitungUmk() * self.ped)
        print(f"FInal UMK kota Bandung adalah : {hasil}")


ump = ump(nilaiUMP,inflasi,alfa)
print(f"Nilai UMK Dasar : {ump.hitungUmk()}")

umk = umk(nilaiUMP,inflasi,alfa,ped)
umk.finalUMK()