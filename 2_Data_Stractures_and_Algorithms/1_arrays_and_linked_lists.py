sayilar = [10, 20, 30, 40, 50]

print(sayilar[0])

sayilar.append(60)
print(sayilar)

sayilar.pop(1)
print(sayilar)

class Node:
    def __init__(self, veri):    #yeni dugum olustugunda kullaniliyore
        self.veri = veri        #dugumun sakladigi bildi veri dedim iste
        self.sonraki = None     #dugumun adresi basta bos cunku baglanti sonra eklenicek

birinci = Node("elma")
ikinci = Node("armut")
ucuncu = Node("muz")
dorduncu = Node("cilek"
#en basta N yazmadim n yazdim diye hata verdi 30 dakika ugrastim

birinci.sonraki = ikinci
ikinci.sonraki = ucuncu
ucuncu.sonraki = dorduncu
#burda 1i2ye,2yi3e,3e4u bagliyoruz

gecici = birinci    #degiskeni basa koyar
while gecici is not None:
    print(gecici.veri)
    gecici = gecici.sonraki




