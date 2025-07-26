#son giren ilk cikar heaps
stack = []

stack.append("kitap 1")
stack.append("kitap 2")
stack.append("kitap 3")

print("stack:", stack)

#cikarma pop ile yapiliuyor
son_kitap = stack.pop()
print("cikan", son_kitap)

print("kalan:", stack)


#1. ilk aliniyor queue iste
from collections import deque

queue = deque()

# kuiyruga ekleniyor append kodu zateb
queue.append("ali")
queue.append("veli")
queue.append("keli")

print("Queue:", queue)

# pop ile cikart
ilk = queue.popleft()
print("ilk cikan:", ilk)

print("kalan kuyruk:", queue)


#min ve max ogelere hizli eriismi saglar oncelik sirasina gore islem yapilir
import heapq

veriler = [5, 3, 8, 1, 9]
heapq.heapify(veriler)
print("min heap:", veriler)

# en kcuuk ogeyi bulup yazar ve cikarir
en_kucuk = heapq.heappop(veriler)
print("cikan en kucuk:", en_kucuk)

print("kalan heap:", veriler)