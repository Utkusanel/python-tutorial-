meyveler = ["elma", "armut", "kavun"]
print(meyveler)

print(meyveler[0])
print(meyveler[1])
#indeks numaralari 0dan baslar dogal sayi gibi dusun

#append ekkeme kamutu gbi dusun
meyveler.append("karpuz")
print(meyveler)

#belirli numaradakini direkt =ile degistirebilirsin

meyveler[1] = "kivi"
print(meyveler)

del meyveler[2]
print(meyveler)


renkler =["kirmizi", "mavi", "sari"]
print(renkler)

print(renkler[0])
print(renkler[1])

renkler.append("yesil")
print(renkler)

del renkler[0]
print(renkler)