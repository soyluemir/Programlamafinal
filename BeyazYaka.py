from Calisan import Calisan
class BeyazYaka(Calisan):
    def __init__(self, tcno, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvikPrimi):
        super().__init__(tcno, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvikPrimi=tesvikPrimi

    def al_tesvik_primi(self): return self.__tesvikPrimi
    def yap_tesvik_primi(self,tesvikPrimi): self.__tesvikPrimi=tesvikPrimi

    def zam_hakki(self):
        if self.al_tecrube() < 24: return self.al_tesvik_primi()
        elif self.al_tecrube() >= 24 and self.al_tecrube() <= 48 and self.al_maas() <= 15000: return (self.al_maas() % self.al_tecrube()) * 5 + self.al_tesvik_primi()
        elif self.al_tecrube() > 48 and self.al_maas() <= 25000: return (self.al_maas() % self.al_tecrube()) * 4 + self.al_tesvik_primi()
        else: return 0

    def yeni_maas(self): return self.al_maas() + self.zam_hakki()