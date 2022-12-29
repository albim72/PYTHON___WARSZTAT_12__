from pojazd import Pojazd

sm = Pojazd()
odl = float(input("podaj odległość [km]: "))
lt = float(input("podaj liczbę spalonych litrów paliwa: "))
cn = float(input("podaj cenę za litr paliwa: "))
print(f'spalanie na trasie {odl} km -> {sm.spalanie100(odl,lt):.2f} [l/100km]')
print(f'koszt przejazdu na trasie: {odl} km wynosi: {sm.kosztprzejazdu(odl,lt,cn):.2f} zł')
