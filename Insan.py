class Insan:
    def __init__(self, tcno, ad, soyad, yas, cinsiyet, uyruk):
        self.__tcno = tcno
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk

    def al_tcno(self): return self.__tcno
    def yap_tcno(self, tc_no): self.__tcno = tc_no

    def al_ad(self): return self.__ad
    def yap_ad(self, ad):self.__ad = ad

    def al_soyad(self): return self.__soyad
    def yap_soyad(self, soyad):self.__soyad = soyad

    def al_yas(self): return self.__yas
    def yap_yas(self, yas): self.__yas = yas

    def al_cinsiyet(self):return self.__cinsiyet
    def yap_cinsiyet(self, cinsiyet): self.__cinsiyet = cinsiyet

    def yap_uyruk(self, uyruk): self.__uyruk = uyruk
    def al_uyruk(self): return self.__uyruk



    def __str__(self):
        return f"TC Kimlik No: {self.al_tcno()}\nAd: {self.al_ad()}\nSoyad: {self.al_soyad()}\nYaş: {self.al_yas()}\nCinsiyet: {self.al_cinsiyet()}\nUyruk: {self.al_uyruk()}"