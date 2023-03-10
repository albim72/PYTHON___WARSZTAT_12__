from datetime import date

class Osoba:
    def __init__(self,imie,wiek):
        self.imie = imie
        self.wiek = wiek

    #metoda klasy
    @classmethod
    def ile_od_narodzin(cls,imie,rok):
        return cls(imie,date.today().year - rok)

    #metoda statyczna
    @staticmethod
    def czydorosly(wiek):
        return wiek >=18


pr1 = Osoba("Roman",43)
pr2 = Osoba.ile_od_narodzin("Anna",1974)

print(type(pr1))
print(type(pr2))

print(pr1.wiek)
print(pr2.wiek)

print(pr1.czydorosly(pr1.wiek))
print(pr2.czydorosly(pr2.wiek))

print(Osoba.czydorosly(13))
