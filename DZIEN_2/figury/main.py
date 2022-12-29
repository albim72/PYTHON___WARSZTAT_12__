from prostokat import Prostokat
from trojkat import Trojkat
from trapez import Trapez
from elipsa import Elipsa

print("____________________________________")
pr = Prostokat(5.6,7.66)
print(f'pole figury: {pr.__class__.__name__} wynosi: {pr.pole_figury():.2f} cm2')

print("____________________________________")
prk = Prostokat(4.4,4.4)
print(f'pole figury: {prk.__class__.__name__} wynosi: {prk.pole_figury():.2f} cm2')

print("____________________________________")
tr = Trojkat(4.7,8.44)
print(f'pole figury: {tr.__class__.__name__} wynosi: {tr.pole_figury():.2f} cm2')

print("____________________________________")
trp = Trapez(7.3,5.6,4.55)
print(f'pole figury: {trp.__class__.__name__} wynosi: {trp.pole_figury():.2f} cm2')

print("____________________________________")
elp = Elipsa(5.5,7)
print(f'pole figury: {elp.__class__.__name__} wynosi: {elp.pole_figury():.2f} cm2')

#zbuduj klasę Kolo(Figura) -> pole kola -> pi*a**2
#koło jest podzbiorem elips, zbuduj w klasie elipsa konstruktor __new__ i utwórz w klasie elipsa opcję
#przekształcemnia klasy Elipsa w klasę Kolo pod warunkiem równosci obu półosi elipsy (promień okręgU)

print("____________________________________")
kl = Elipsa(6,6)
print(f'pole figury: {kl.__class__.__name__} wynosi: {kl.pole_figury():.2f} cm2')
