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

nieparz = list(filter(lambda x:x%2!=0, num))
print(nieparz)

def warunek(x):
    return x%2!=0

nparz_f = list(filter(warunek,num))
print(nparz_f)

#stwórz listę cube i przekaż do niej wszystkie wartości z listy num podniesione do potęgi 3
#użyj funkcji standardowej map(funkcja,dane) - pierwszy parametr musi być funkcją opisującą warunek transformacji

cube = list(map(lambda x:x**3,num))

print(cube)

def dodaj_trzy(x):
    return x+3

trojka = list(map(dodaj_trzy,num))
print(trojka)

#własne funkcje wyższego rzędu

def filtorwanie(dane,test):
    plus = []
    for element in dane:
        if (test(element)):
            plus.append(element)
    return plus

def ekstra_liczba(n):
    return n >= 100

print(filtorwanie(num,ekstra_liczba))

def mapowanie(dane,transformacja):
    mapa = []
    for element in dane:
        mapa.append(transformacja(element))
    return mapa

def addFive(n):
    return n+5

def kwadrat(n):
    return n**2

print(mapowanie(num,addFive))

print(mapowanie(num,kwadrat))
