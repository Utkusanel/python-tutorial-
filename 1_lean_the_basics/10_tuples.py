renkler = ("kirmizi", "mavi", "yesil")
print(renkler)

print(renkler[0])
print(renkler[2])

#renkler[0] = "turuncu"
#hata ornegi tupllar degistirilemez

renk = ("kirmizi",) #virgul omazsa str olark algilar
print(type(renk))

renkler = ("kirmizi", "mavi", "yesil")
for renk in renkler:
    print(renk)


meyveler = ("elma", "armut", "muz", "kiraz")
for meyve in meyveler:
    print(meyve)