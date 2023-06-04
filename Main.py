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

if __name__ == "__main__":
    main()

    