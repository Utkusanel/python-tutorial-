class Dugum:
    def __init__(self, veri):
        self.veri = veri
        self.sol = None
        self.sag = None
#her dugumun kendi kurali var
# self.sol kendisinden dusukleri
#self.sag kendisinden buyukleri icerir

class BST:
    def __init__(self):
        self.kok = None
#veri ekleme
    def ekle(self, veri):
        self.kok = self._ekle(self.kok, veri)

    def _ekle(self, dugum, veri):
        if dugum is None:
            return Dugum(veri)
        if veri < dugum.veri:
            dugum.sol = self._ekle(dugum.sol, veri)
        else:
            dugum.sag = self._ekle(dugum.sag, veri)
        return dugum
    #veri arama
    def ara(self, veri):
        return self._ara(self.kok, veri)

    def _ara(self, dugum, veri):
        if dugum is None:
            return False
        if veri == dugum.veri:
            return True
        elif veri < dugum.veri:
            return self._ara(dugum.sol, veri)
        else:
            return self._ara(dugum.sag, veri)

agac = BST()
agac.ekle(10)
agac.ekle(5)
agac.ekle(15)

print(agac.ara(10))
print(agac.ara(7)) #listede olmadigi icin false yazar
