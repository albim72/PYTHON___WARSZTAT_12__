print("pierwsza linia na dobry początek")

# komentarz podstawowy
"""
komentarz dokumentacyjny - wieloliniowy
"""

'''
komentarz
wieloliniowy
'''

# lista, krotka, zbiór, słownik

imiona = ["Jan", "Piotr", "Anna", "Leon", "Ula", "Olga", "Magda", "Tekla"]

print(imiona)
print(imiona[0])
print(imiona[2])
# CTRL+D -> powielenie zaznaczonego fragmentu kodu

print(imiona[2:5])
print(imiona[:5])
print(imiona[3:])
print(imiona[-1])

s = "lajkonik"
print(s)
print(type(s))

print(s[3])
print(s[1:5])
print(s[-2])

imiona_parzyte = imiona[::2]
print(imiona_parzyte)

test = imiona[2:6:2]
print(test)

tx1 = "grudzień"
tx2 = "Grzegorz"

print(tx1, "-", tx1[::-1])
print(tx2, "-", tx2[::-1])

# krotka
miasta = ("Kraków", "Tarnów", "Płock", "Lublin", "Kraków")
print(miasta[0])

miasta_lista = list(miasta)

print(type(miasta_lista))

miasta_lista.sort()
print(miasta_lista)

miasta = tuple(miasta_lista)
print(miasta)

a = 999
print(a)
print(type(a))

a = 8.99
print(a)
print(type(a))

a = "pięć"
print(a)
print(type(a))

d: float
d = 9.99
print(d)
print(type(d))

d = True
print(d)
print(type(d))

# zbiór
drzewa = {"sosna", "dąb", "jesion", "baobab", "wierzba", "klon", "jabłoń", "dąb"}
print(drzewa)
print(drzewa)
print(drzewa)

drzewa.add("osika")
drzewa.update(["topola", "śliwa", "grusza"])

print(drzewa)

liczby = [3, 3, 6, 8, 1, 2, 3, 4, 5, 2, 3, 4, 5, 2, 5, 8, 42, 23, 5, 2, 2, 4, 1, 2, 3]

liczby_s = set(liczby)
liczby = list(liczby_s)
print(liczby)

# słownik
osoba = {
    "imie": "Karol",
    "nazwisko": "Kot",
    "wiek": 25
}

print(osoba)
print(osoba["nazwisko"])

osoba["miasto"] = "Rzeszów"

print(osoba)

print(osoba.keys())
print(osoba.values())
print(osoba.items())

print("______________ klucze ______________")
for x in osoba:
    print(x)

print("______________ wartości I ______________")
for x in osoba.values():
    print(x)

print("______________ wartości II ______________")
for x in osoba:
    print(osoba[x])

print("______________ pary ______________")
for x,y in osoba.items():
    print(x,':',y)
