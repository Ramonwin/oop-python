class sistemPenilaian():
    def __init__(self, absen, tugas, uts, uas):
        self.absen = absen
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def hitungNilaiAkhir(self):
        nilaiAkhir = (self.absen * 0.1) + (self.tugas * 0.2) + (self.uts * 0.3) + (self.uas * 0.4)
        return nilaiAkhir
    
    def konversiGrade(self,nilaiAkhir):
        if nilaiAkhir > 80:
            grade = "A"
        else :
            grade ="B"
        print(f"Grade nya adalah : {grade}")

siakad = sistemPenilaian(70,80,90,100)
na = siakad.hitungNilaiAkhir()
print(f"Nilai akhir : {na}")

siakad.konversiGrade(na)


# print(f"Grade : {siakad.konversiGrade}")


