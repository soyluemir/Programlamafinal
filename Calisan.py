from Insan import Insan
class Calisan(Insan):
    def __init__(self, tcno, ad,soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tcno, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor=sektor
        self.__tecrube=tecrube
        self.__maas=maas

    def al_sektor(self): return self.__sektor
    def yap_sektor(self,sektor): self.__sektor=sektor

    def al_tecrube(self): return self.__tecrube
    def yap_tecrube(self,tecrube): self.__tecrube = tecrube
    
    def al_maas(self): return self.__maas
    def yap_maas(self,maas): self.__maas = maas
    
