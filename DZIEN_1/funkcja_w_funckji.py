#przykład 1

def witaj(imie):
    return f'Miło Cię widzieć {imie}'

def osoba(funkcja,imie):
    return funkcja(imie)

print(osoba(witaj,"Leon"))
