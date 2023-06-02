class Insan:
    def __init__(self, tcno, ad, soyad, yas, cinsiyet, uyruk):
        self.__tcno = tcno
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk

    def __str__(self):
        return f"TC Kimlik No: {self.al_tcno()}\nAd: {self.al_ad()}\nSoyad: {self.al_soyad()}\nYaş: {self.al_yas()}\nCinsiyet: {self.al_cinsiyet()}\nUyruk: {self.al_uyruk()}"