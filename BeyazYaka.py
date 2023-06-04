from Calisan import Calisan
class BeyazYaka(Calisan):
    def __init__(self, tcno, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvikPrimi):
        super().__init__(tcno, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvikPrimi=tesvikPrimi
