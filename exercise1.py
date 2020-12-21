# class odev1
import self as self


class Insan():
    def __init__(self, ad, soyad, yas, ulke, sehir, yetenekler):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []


kisi = Insan("esra", "cakmaklı", 25, "turkiye", "zonguldak", "")


def yetenek_ekle():
    kisi.yetenekler.append('tuval boyamak')
    kisi.yetenekler.append('mızıka çalmak')
    kisi.yetenekler.append('güzel yemek yapmak')
    print("yetenekler: " + str(kisi.yetenekler))


def kisi_bilgileri(kisi):
   return print("ad soyad: " + kisi.ad,
          kisi.soyad + "\n" + "yas: " + str(kisi.yas) + "\n" + "ulke: " + kisi.ulke + "\n" + "sehir: " + kisi.sehir)


kisi_bilgileri(kisi)
yetenek_ekle()
