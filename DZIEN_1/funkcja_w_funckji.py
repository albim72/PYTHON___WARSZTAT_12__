#przykład 1

def witaj(imie):
    return f'Miło Cię widzieć {imie}'

def konkurs(imie,punkty):
    return f'uczetnik konkursu {imie}, liczba punktów: {punkty}'

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Olga",56))


#przykład 2

def rejestracja(oplata):
    def lista():
        return "jesteś na liście zawodników"
    def brak():
        return "jeśli chcesz być na liście startowej, zapłać niezwłocznie"
    def error():
        return "błędne dane, 0  brak wpłaty, 1  wpłata"

    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error


print(rejestracja(1)())
print(rejestracja(0)())
print(rejestracja(33)())
