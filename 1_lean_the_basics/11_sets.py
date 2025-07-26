meyveler = {"elma", "muz", "armut", "muz"}
print(meyveler)
#koseli parantez eklersem aynilari cikartiot 1 tane kaliyor

meyveler = {"elma", "armut"}
meyveler.add("muz")
print(meyveler)

meyveler.remove("muz")
print(meyveler)

#hata olmasi icin olmayan sey remove ile hata verir ama discard kullanirsan hata vermez
meyveler.discard("ananas")

sayilar = {1,2,3}
for sayi in sayilar:
    print(sayilar)

A = {1,2,3}
B = {3,4,5}
print(A.union(B))
print(A.intersection(B))

ogrenciler = {"ali", "ayse", "mehmet", "ali"}
print(ogrenciler)

ogrenciler.add("zeyneop")
print(ogrenciler)

ogrenciler.discard("ahmet")
#ahmet yok ama hata vermemesini deniyorum

for ogrenci in ogrenciler:
    print(ogrenci)