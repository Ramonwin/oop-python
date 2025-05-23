quiz = """
1. buatlah perhitungan UMK sesuai UMP yang ada di propinsi tersebut
2. buatlah class induk UMP() dengan atribut : nilaiUMP, inflasi,index alfa
3. buatlah method hitung_nilai_umk() di class UMP
4. rumus umk = ump + (ump * (inflasi + alfa))
5. buatlah class anak "UMK()" yang mewarisi class induk "UMP()"
6. tambahan atribut pertumbuhan_ekonomi_daerah di class UMK()
7. final umk = umk + (umk * pertumbuhan_ekonomi_daerah)
8. tampilkan nilai UMK di kota tersebut
9. buat inputan masukan konsumsi perkapita satuan(%)
10. buatlah class Batas Atas dengan atribut konsumsi perkapita
11. rumus menghitung batasAtas = UMK + (UMK * konsumsi perkapita / 100)
12. tampilkan pesan "batas maksimal umk bdg adalah {batasAtas}

keterangan : nilai ump = 2,5juta
            inflasi = 10%
            index alfa = 20%
            pertumbuhan ed = 7%    
"""

class ump():
    def __init__(self, nilaiUMP, inflasi, alfa):
        self.nilaiUMP = nilaiUMP
        self.inflasi = inflasi
        self.alfa = alfa

    def hitungUmk(self):
        umkDasar = self.nilaiUMP + (self.nilaiUMP * (self.inflasi + self.alfa))
        return umkDasar

class umk(ump):
    def __init__(self, nilaiUMP, inflasi, alfa,ped):
        super().__init__(nilaiUMP, inflasi, alfa)
        self.ped = ped
    
    def pertumbuhan_ekonomi(self):
        return self.ped
        


nilai = ump(25000000,0.1,0.2)
sub_nilai = nilai.hitung_umk()
print(f"sub nilai : {sub_nilai}")

umk = umk(25000000,0.1,0.2,0.065)
sub1 = umk.hitung_umk()
ped = umk.pertumbuhan_ekonomi()
finalUMK = sub1 + (sub1 * ped)
print(f"Final Nilai UMK Kota Bandung Adalah : {finalUMK}")






