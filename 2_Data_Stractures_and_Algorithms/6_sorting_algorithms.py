def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

sayilar = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(sayilar)
print(sayilar)

def insertion_sort(liste):
    for i in range(1, len(liste)):
        anahtar = liste[i]
        j = i - 1
        while j >= 0 and anahtar < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = anahtar

sayilar = [12, 11, 13, 5, 6]
insertion_sort(sayilar)     #insertio_sort() direkt siraliyor
print(sayilar)

#buyuk islemlerde sag ve sol diye (diger dosyalarda gorebilirsin) ayirip ona gore siralar ve birlestirir diger islemde drekt yapmisti
def merge_sort(liste):
    if len(liste) > 1:
        orta = len(liste) // 2
        sol = liste[:orta]
        sag = liste[orta:]

        merge_sort(sol)
        merge_sort(sag)

        i = j = k = 0

        while i < len(sol) and j < len(sag):
            if sol[i] < sag[j]:
                liste[k] = sol[i]
                i += 1
            else:
                liste[k] = sag[j]
                j += 1
            k += 1

        while i < len(sol):
            liste[k] = sol[i]
            i += 1
            k += 1

        while j < len(sag):
            liste[k] = sag[j]
            j += 1
            k += 1

sayilar = [38, 27, 43, 3, 9, 82, 10]
merge_sort(sayilar)     #merge birlestirme komutu
print(sayilar)