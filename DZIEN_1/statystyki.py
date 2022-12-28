liczby = [56,101,-1009,5670,340,-245,12,39,0,789,-564]

def pokaz_statystki(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum - minimum
    lelem = len(lista)
    suma = sum(lista)
    avg = suma/lelem
    return minimum,maksimum,rozstep,lelem,suma,avg

wynik = pokaz_statystki(liczby)
print(wynik)
print(type(wynik))

mini,maxi,roz,le,sm,avg = pokaz_statystki(liczby)
print(f'wartość maksymalna: {maxi}, wartość minimalna: {mini}, rozstęp: {roz}, liczba elementów: {le}, '
      f'suma elementów listy: {sm}, średnia arytmetyczna: {avg:.2f}')
