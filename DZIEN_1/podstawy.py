print("pierwsza linia na dobry początek")

#komentarz podstawowy
"""
komentarz dokumentacyjny - wieloliniowy
"""

'''
komentarz
wieloliniowy
'''

#lista, krotka, zbiór, słownik

imiona = ["Jan","Piotr","Anna","Leon","Ula","Olga","Magda","Tekla"]

print(imiona)
print(imiona[0])
print(imiona[2])
#CTRL+D -> powielenie zaznaczonego fragmentu kodu

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

tx1="grudzień"
tx2="Grzegorz"

print(tx1,"-",tx1[::-1])
print(tx2,"-",tx2[::-1])

#krotka
miasta = ("Kraków","Tarnów","Płock","Lublin")
print(miasta[0])

miasta_lista = list(miasta)

print(type(miasta_lista))
