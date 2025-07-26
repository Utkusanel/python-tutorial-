#base case ile kodun duracagi noktayi belirlioz
#recursive case de kodun kendini cagirdigi durumda kullanliyor

def faktoriyel(n):      #base case herseye bu kuruluyor iste
    if n == 0 or n == 1:
        return 1
    else:       #else ise direkt recursive cunku temel hal degil
        return n * faktoriyel(n - 1)    #eskiden yaptigim faktoriyel hesabini kullandim
print(faktoriyel(5))

