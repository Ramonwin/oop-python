quiz="""
    1. buatlah class dengan nama sistemPenilaian dengan atribut
    # absen, tugas, uts, uas
    2. buat 2 buah method, hitungNilaiAkhir & konversiGrade
    3. ketentuan nilai akhir :
        a. nilai Absen * 10%
        b. nilai tugas * 20%
        c. nilai uts * 30%
        d. nilai uas * 40%
    4. nilai akhir = absen + tugas + uts + uas
    5. ketentuan grade :
        a. jika nilai Akhir lebih dari 80 Grade A
        b. jika nilai Akhir 80 atau kurang maka grade B
    6. buat objek & panggil method dari class SistemPenilaian
"""

class sistemPenilaian():
    def __init__(self, absen, tugas, uts, uas):
        self.absen = absen
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def hitungNilaiAkhir(self):
        nilaiAkhir = (self.absen * 0.1) + (self.tugas * 0.2) + (self.uts * 0.3) + (self.uas * 0.4)
        return nilaiAkhir
    
    def konversiGrade(self, nilaiAkhir):
        if nilaiAkhir > 80:
            grade = "A"
        else :
            grade = "B"
        print(f"Gradenya adalah {grade}")

siakad = sistemPenilaian(70,80,90,100)
na = siakad.hitungNilaiAkhir()
print(f"Nilai akhir : {na}")

siakad.konversiGrade(na)