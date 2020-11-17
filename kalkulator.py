class kalkulator:
    def __init__ (self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def pertambahan(self):
        pertambahan = self.angka1 + self.angka2
        return pertambahan
    
    def pengurangan(self):
        pengurangan = self.angka1 - self.angka2
        return pengurangan
    
    def perkalian(self):
        perkalian = self.angka1 * self.angka2
        return perkalian
    
    def pembagian(self):
        pembagian = self.angka1 / self.angka2
        return pembagian

class kalakulator2:
    def __init__ (self, angka3):
        self.angka3 = angka3
    
    def akar(self):
        akar = self.angka3**(1/2)
        return akar

    def kuadrat(self):
        kuadrat = self.angka3**2
        return kuadrat


print("Menghitung Pertambahan")
menghitung_pertambahan = kalkulator(float(input("Masukkan Angka 1 : ")), float(input("Masukkan Angka 2 : ")))
print("Hasil Pertambahan : ", menghitung_pertambahan.pertambahan(),"\n")
print("Menghitung Pengurangan")
menghitung_pengurangan = kalkulator(float(input("Masukkan Angka 1 : ")), float(input("Masukkan Angka 2 : ")))
print("Hasil Pengurangan : ", menghitung_pengurangan.pengurangan(),"\n")
print("Menghitung Perkalian")
menghitung_perkalian = kalkulator(float(input("Masukkan Angka 1 : ")), float(input("Masukkan Angka 2 : ")))
print("Hasil Perkalian : ", menghitung_pengurangan.perkalian(),"\n")
print("Menghitung Pembagian")
menghitung_pembagian = kalkulator(float(input("Masukkan Angka 1 : ")), float(input("Masukkan Angka 2 : ")))
print("Hasil Pembagian : ", menghitung_pembagian.pembagian(),"\n")
print("Menghitung Akar")
menghitung_akar = kalakulator2(float(input("Masukkan Angka : ")))
print("Hasil Akar : ", menghitung_akar.akar(),"\n")
print("Menghitung Angka Kuadrat")
menghitung_kuadrat = kalakulator2(float(input("Masukkan Angka : ")))
print("Hasil Angka Kuadrat : ", menghitung_kuadrat.kuadrat())