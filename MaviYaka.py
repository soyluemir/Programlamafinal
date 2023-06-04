from Calisan import Calisan
class MaviYaka(Calisan):
    def __init__(self, tcno, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranmaPayi):
        super().__init__(tcno, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranmaPayi=yipranmaPayi

    def al_yipranma_payi(self): return self.__yipranmaPayi
    def yap_yipranma_payi(self,yipranmaPayi): self.__yipranmaPayi=yipranmaPayi

    def zam_hakki(self):
        if self.al_tecrube() < 24: return self.al_yipranma_payi() * 10
        elif self.al_tecrube() >= 24 and self.al_tecrube() <= 48 and self.al_maas() <= 15000: return (self.al_maas() % self.al_tecrube()) / 2 + self.al_yipranma_payi() * 10
        elif self.al_tecrube() > 48 and self.al_maas() <= 25000: return (self.al_maas() % self.al_tecrube()) / 3 + self.al_yipranma_payi() * 10
        else: return 0