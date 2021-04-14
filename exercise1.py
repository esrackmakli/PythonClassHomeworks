# class odev1
class Insan:
    def __init__(self, ad, soyad, yas, ulke, sehir):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return self.ad, self.soyad, self.yas, self.ulke, self.sehir, self.yetenekler

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)


kisi = Insan("esra", "cakmaklı", 25, "turkiye", "zonguldak")
kisi.yetenek_ekle("tuval boyamak")
kisi.yetenek_ekle("gitar çalmak")
print(kisi.kisi_bilgileri())


