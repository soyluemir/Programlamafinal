from Insan import Insan
class Issiz(Insan):
    def __init__(self, tcno, ad,soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tcno, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube=tecrube
