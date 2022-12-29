from prostokat import Prostokat
from trojkat import Trojkat

print("____________________________________")
pr = Prostokat(5.6,7.66)
print(f'pole figury: {pr.__class__.__name__} wynosi: {pr.pole_figury():.2f} cm2')

print("____________________________________")
prk = Prostokat(4.4,4.4)
print(f'pole figury: {prk.__class__.__name__} wynosi: {prk.pole_figury():.2f} cm2')

print("____________________________________")
tr = Trojkat(4.7,8.44)
print(f'pole figury: {tr.__class__.__name__} wynosi: {tr.pole_figury():.2f} cm2')
