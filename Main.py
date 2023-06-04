from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
import pandas as pd

def main():
    insan1 = Insan("0001", "ZEKİYE", "ZUBAROĞLU", 75, "KADIN", "Türkiye")
    insan2 = Insan("0002", "ESEN", "GENÇ", 41, "ERKEK", "Türkiye")
    print(str(insan1) + "\n\n" + str(insan2) + "\n\n")

    issiz1 = Issiz("0003", "TÜLAY", "TAY", 39, "KADIN", "Türkiye", {"mavi": 3, "beyaz": 5, "yonetici": 6})
    issiz2 = Issiz("0004", "Omar", "Schaefer", 65, "ERKEK", "Almanya", {"mavi": 20, "beyaz": 14, "yonetici": 13})
    issiz3 = Issiz("0005", "FATMA", "AYAR", 66, "KADIN", "Türkiye", {"mavi": 15, "beyaz": 12, "yonetici": 11})
    print(str(issiz1) + "\n\n" + str(issiz2) + "\n\n" + str(issiz3) + "\n\n")

    calisan1 = Calisan("0006", "NUH", "KIZILTOPRAK", 32, "ERKEK", "Türkiye", "Diğer", 26, 12000)
    calisan2 = Calisan("0007", "YENER", "ÜNNÜ", 25, "ERKEK", "Türkiye", "İnşaat", 28, 19000)
    calisan3 = Calisan("0008", "GÖKAY", "AKDEMİR", 68, "ERKEK", "Türkiye", "Muhasebe", 105, 39000)
    print(str(calisan1) + "\n\n" + str(calisan2) + "\n\n" + str(calisan3) + "\n\n")

    maviyaka1 = MaviYaka("0009", "YELİZ", "BÜYÜKKALAYCI", 55, "KADIN", "Türkiye", "Teknoloji", 15, 12000, 0.25)
    maviyaka2 = MaviYaka("0010", "Martin", "Carson", 72, "ERKEK", "Amerika", "Diğer", 20, 15000, 0.45)
    maviyaka3 = MaviYaka("0011", "AÇELYA", "TAŞDEMİR", 34, "KADIN", "Türkiye", "Muhasebe", 10, 10000, 0.1)
    print(str(maviyaka1) + "\n\n" + str(maviyaka2) + "\n\n" + str(maviyaka3) + "\n\n")

    beyazyaka1 = BeyazYaka("0012", "MUAMMER", "ERBİLEN", 59, "ERKEK", "Türkiye", "Teknoloji", 150, 44000, 5800)
    beyazyaka2 = BeyazYaka("0013", "Sinead", "Haney", 51, "KADIN", "İngiltere", "Teknoloji", 41, 39000, 4200)
    beyazyaka3 = BeyazYaka("0014", "Zain", "Vasquez", 54, "ERKEK", "İngiltere", "Muhasebe", 35, 25000, 2800)
    print(str(beyazyaka1) + "\n\n" + str(beyazyaka2) + "\n\n" + str(beyazyaka3) + "\n\n")

    alanlar = ["Calisan", "Calisan", "Calisan", "MaviYaka", "MaviYaka", "MaviYaka", "BeyazYaka", "BeyazYaka", "BeyazYaka"]
    tc = [calisan1.al_tcno(), calisan2.al_tcno(), calisan3.al_tcno(), maviyaka1.al_tcno(), maviyaka2.al_tcno(), maviyaka3.al_tcno(), beyazyaka1.al_tcno(), beyazyaka2.al_tcno(), beyazyaka3.al_tcno()]
    ad = [calisan1.al_ad(), calisan2.al_ad(), calisan3.al_ad(), maviyaka1.al_ad(), maviyaka2.al_ad(), maviyaka3.al_ad(), beyazyaka1.al_ad(), beyazyaka2.al_ad(), beyazyaka3.al_ad()]
    soyad = [calisan1.al_soyad(), calisan2.al_soyad(), calisan3.al_soyad(), maviyaka1.al_soyad(), maviyaka2.al_soyad(), maviyaka3.al_soyad(), beyazyaka1.al_soyad(), beyazyaka2.al_soyad(), beyazyaka3.al_soyad()]
    yas = [calisan1.al_yas(), calisan2.al_yas(), calisan3.al_yas(), maviyaka1.al_yas(), maviyaka2.al_yas(), maviyaka3.al_yas(), beyazyaka1.al_yas(), beyazyaka2.al_yas(), beyazyaka3.al_yas()]
    cinsiyet = [calisan1.al_cinsiyet(), calisan2.al_cinsiyet(), calisan3.al_cinsiyet(), maviyaka1.al_cinsiyet(), maviyaka2.al_cinsiyet(), maviyaka3.al_cinsiyet(), beyazyaka1.al_cinsiyet(), beyazyaka2.al_cinsiyet(), beyazyaka3.al_cinsiyet()]
    uyruk = [calisan1.al_uyruk(), calisan2.al_uyruk(), calisan3.al_uyruk(), maviyaka1.al_uyruk(), maviyaka2.al_uyruk(), maviyaka3.al_uyruk(), beyazyaka1.al_uyruk(), beyazyaka2.al_uyruk(), beyazyaka3.al_uyruk()]
    sektor = [calisan1.al_sektor(), calisan2.al_sektor(), calisan3.al_sektor(), maviyaka1.al_sektor(), maviyaka2.al_sektor(), maviyaka3.al_sektor(), beyazyaka1.al_sektor(), beyazyaka2.al_sektor(), beyazyaka3.al_sektor()]
    tecrube = [calisan1.al_tecrube() / 12, calisan2.al_tecrube() / 12, calisan3.al_tecrube() / 12, maviyaka1.al_tecrube() / 12, maviyaka2.al_tecrube() / 12, maviyaka3.al_tecrube() / 12, beyazyaka1.al_tecrube() / 12, beyazyaka2.al_tecrube() / 12, beyazyaka3.al_tecrube() / 12]
    maas = [calisan1.al_maas(), calisan2.al_maas(), calisan3.al_maas(), maviyaka1.al_maas(), maviyaka2.al_maas(), maviyaka3.al_maas(), beyazyaka1.al_maas(), beyazyaka2.al_maas(), beyazyaka3.al_maas()]
    yipranma_payi = [0, 0, 0, maviyaka1.al_yipranma_payi(), maviyaka2.al_yipranma_payi(), maviyaka3.al_yipranma_payi(), 0, 0, 0]
    prim = [0, 0, 0, 0, 0, 0, beyazyaka1.al_tesvik_primi(), beyazyaka2.al_tesvik_primi(), beyazyaka3.al_tesvik_primi()]
    yenimaas = [calisan1.yeni_maas(), calisan2.yeni_maas(), calisan3.yeni_maas(), maviyaka1.yeni_maas(), maviyaka2.yeni_maas(), maviyaka3.yeni_maas(), beyazyaka1.yeni_maas(), beyazyaka2.yeni_maas(), beyazyaka3.yeni_maas()]

    calisanlar = pd.DataFrame({"Alan": alanlar, "TC": tc, "Ad": ad, "Soyad": soyad, "Yaş": yas, "Cinsiyet": cinsiyet, "Uyruk": uyruk, "Sektör": sektor, "Tecrübe": tecrube, "Maaş": maas, "Yıpranma Payı": yipranma_payi, "Prim": prim, "Yeni Maaş": yenimaas})
    print("Çalışanlar: \n", calisanlar, "\n")
    print("Çalışanların alanlarına göre ortalama tecrübe ve yeni maaşları: \n", calisanlar.groupby("Alan")[["Tecrübe", "Yeni Maaş"]].mean(), "\n")
    print("Çalışanların maaşları 15000'den fazla olanlar: ", len(calisanlar[calisanlar["Maaş"] > 15000]), "\n")
    print("Çalışanların yeni maaşlarına göre sıralanmış hali: \n", calisanlar.sort_values(by = "Yeni Maaş", ascending = True), "\n")
    print("Tecrübesi 3 yıldan fazla olan beyaz yaka çalışanlar: \n", calisanlar[(calisanlar["Tecrübe"] > 3) & (calisanlar["Alan"] == "BeyazYaka")], "\n")
    print("Yeni maaşı 10000'den fazla olan çalışanların TC ve yeni maaşları: \n", calisanlar[calisanlar["Yeni Maaş"] > 10000][["TC", "Yeni Maaş"]][2:5], "\n")
    calisanlar2 = pd.DataFrame({"Ad": ad, "Soyad": soyad, "Sektör": sektor, "Yeni Maaş": yenimaas})
    print("Çalışanların ad, soyad, sektör ve yeni maaşları: \n", calisanlar2, "\n")







if __name__ == "__main__":
    main()

    