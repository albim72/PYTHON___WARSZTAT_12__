import math

print((lambda e:e**3)(45))

b = lambda u,w=2:u/w-3

print(b(4,7))
print(b(4))

def zw(u,w):
    return u/w-3

print(zw(4,6))

def multi(n):
    return lambda a:a*n*math.sqrt(a)

print(multi(6)(7))
num = [67,-2,5,2,177,-9,34,122,4,7,1,100,-4,0,5,16,78,93,-56,12]

#stwórz listę nieparz i przekaż do niej wszystkie wartości nieparzyste z listy num
#użyj funkcji standardowej filter(funkcja,dane) - pierwszy parametr musi być funkcją opisującą warunek filtrowania
