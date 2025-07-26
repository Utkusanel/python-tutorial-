try:
    sayi = int("abc")
    print(sayi)
except:
    print("hat a")

try:
    sayi = int("abc")
except ValueError:
    print("hat a sayi gir ")

try:
    x=10/2
except ZeroDivisionError:
    print("sifira bolunmez ")
else :
    print("hata yok sonuc:", x)
finally:
    print("bu herzamma calisir")

try:
    sayi = int("on")
    print(sayi)
except:
    print("hatali giris")