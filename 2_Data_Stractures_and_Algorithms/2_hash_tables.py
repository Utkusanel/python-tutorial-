notlar = {
    "ali": 85,
    "veli": 90,
    "keli":70
}
print(notlar["keli"])

notlar["deli"] = 100
notlar["veli"] = 60

del notlar["ali"]
print(notlar.keys())

print(notlar.values())
print(notlar.items())

for isim, notu in notlar.items():
    print(isim, "->", notu)