#import dane
#import dane as dn
from dane import filia_nb as filia
from dane import book as ksiazka
from funkcje.bfunkcje import czytaj, czytaj_slownik
from klasy.KlasaDanych import KlasaDanych

print(filia)
print(ksiazka)

print("___________________czytanie za pomocą funkcji_______________________")
czytaj(filia)
czytaj_slownik(ksiazka)
print("___________________czytanie za pomocą metod klasy_______________________")
kd = KlasaDanych(filia,ksiazka)
kd.rlista()
kd.rslownik()
