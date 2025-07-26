sayilar = [1, 2, 3]
it = iter(sayilar)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# sadece ne kadar varsa o kadar digeri digeri digeri diyebiliriz kisaca aslinda next it iste

class Sayilar:
    def __init__(self, max):
        self.max = max
        self.sayi = 0 #0dan basla dyoruz

    def __iter__(self):
        return self

    def __next__(self):
        if self.sayi < self.max:
            self.sayi += 1
            return self.sayi #siradaki ile devam et
        else:
            raise StopIteration # bitince durdur

s = Sayilar(5) #1-5 arasi 5 dagil uretecek 

for i in s:
    print(i)
#burada da 5 e kadar cagirdik