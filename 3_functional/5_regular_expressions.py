import re
metin = "merhaba, ben utku ve telefon numaram 531-3131."

sonuc = re.search(r"\d{3}-\d{4}", metin)
print(sonuc.group())
#\d{} -> rakami belirtiyor ve yanindaki her zaman cuklu parantez olmali

#belirli kelime grubunu bulmak icin
import re
metin = "iletisim icin utkusnel@gmail.com adresine yazabilirsiniz"
email = re.search(r"[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", metin) #adan zye 0 dan 9a gibi dusun bunlari
print(email.group())

#rakamlari kaldirmak
# \d nin yani digeri gibi dolu degil ici bos olunca temizleid boslukla degisen silinir kafasi iste
metin = "bugun 25 temmuz 2025"
temiz = re.sub(r"\d", "", metin)
print(temiz)
