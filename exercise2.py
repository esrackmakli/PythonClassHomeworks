# odev2-exercise2

class Ogrenci:
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinifi):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinifi = ogrenciSinifi


class Soru:
    def NetSayisi(self, dogruSayisi, yanlisSayisi):
        net = dogruSayisi - int(yanlisSayisi / 4)
        return net

    def Hesapla(self, net):
        puan = net * 2
        return puan


dogruSayisi = int(input("Ogrencinin dogru sayisini girin: "))
yanlisSayisi = int(input("Ogrencinin yanlis sayisini girin: "))
if dogruSayisi < 0 or dogruSayisi > 50 or yanlisSayisi < 0 or yanlisSayisi > 50:
    print("Doğru ve yanlis sayilari 0'dan kucuk ya da 50'den buyuk olamaz!")
if dogruSayisi + yanlisSayisi > 50 or dogruSayisi + yanlisSayisi < 0:
    print("Doğru ve yanlis sayilarinin toplamı 0'dan az 50'den fazla olamaz!")
else:
    ogrenciBilgileri = Ogrenci("Ahmet", "Kaya", "5-A")
    neti = Soru().NetSayisi(dogruSayisi, yanlisSayisi)
    puani = Soru().Hesapla(neti)
    print(""
          "\nAdı: ", ogrenciBilgileri.ogrenciAdi,
          "\nSoyadi: ", ogrenciBilgileri.ogrenciSoyadi,
          "\nSinifi: ", ogrenciBilgileri.ogrenciSinifi,
          "\nNeti: ", neti,
          "\nPuani: ", puani)
