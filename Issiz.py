from Insan import Insan
class Issiz(Insan):
    def __init__(self, tcno, ad,soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tcno, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube=tecrube
        self.statu_bul()

    def al_statu(self): return self.__statu
    def yap_statu(self,statu): self.__statu=statu

    def al_tecrube(self): return self.__tecrube
    def yap_tecrube(self,tecrube): self.__tecrube = tecrube
    
    def statu_bul(self):
        mavi, beyaz, yonetici = self.al_tecrube()["mavi"] * 0.2, self.al_tecrube()["beyaz"] * 0.35, self.al_tecrube()["yonetici"] * 0.45
        try:
            if yonetici >= beyaz and yonetici >= mavi:
                self.yap_statu("Yönetici")
            elif beyaz > yonetici and beyaz >= mavi:
                self.yap_statu("Beyaz Yaka")
            elif mavi > yonetici and mavi > beyaz:
                self.yap_statu("Mavi Yaka")
            else:
                print("Hata oluştu")
            return self.al_statu()
        except:
            print("Hata oluştu")
    
    def __str__(self):
        return "Kişi: "+super().__str__()+"\nStatü: "+self.statu_bul()