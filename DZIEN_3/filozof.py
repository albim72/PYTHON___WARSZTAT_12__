odp = input("Czy Ziemia jest płaska? Czy chcesz znać odpowiedź? (t/n) ")
if odp.lower() == "t":
    required = True
else:
    required = False

def odpowiedz(self):
    return "Tak! Ziemia jest płaska!"

def odpowiedz_new(self):
    return "Nie! Ziemia jest elipsoidą!"

def brak(self):
    return "brak odpowiedzi..."


#tworzenie metaklasy
class SednoOdpowiedzi(type):
    def __init__(cls,nazwa_klasy,dziedziczenie,atrybuty):
        if required:
            if nazwa_klasy == "Kopernik" or nazwa_klasy == "Einstein":
                cls.odpowiedz = odpowiedz_new
            else:
                cls.odpowiedz = odpowiedz
        else:
            cls.odpowiedz = brak

class Arystoteles(metaclass=SednoOdpowiedzi):
    pass
class Platon(metaclass=SednoOdpowiedzi):
    pass
class SwTomasz(metaclass=SednoOdpowiedzi):
    pass
class Kopernik(metaclass=SednoOdpowiedzi):
    pass
class Einstein(Kopernik):
    pass

fil1 = Arystoteles()
fil2 = Platon()
fil3 = SwTomasz()
fil4 = Kopernik()
fil5 = Einstein()

print(f'filozof {fil1.__class__.__name__} odpowiada: {fil1.odpowiedz()}')
print(f'filozof {fil2.__class__.__name__} odpowiada: {fil2.odpowiedz()}')
print(f'filozof {fil3.__class__.__name__} odpowiada: {fil3.odpowiedz()}')
print(f'filozof {fil4.__class__.__name__} odpowiada: {fil4.odpowiedz()}')
print(f'filozof {fil5.__class__.__name__} odpowiada: {fil5.odpowiedz()}')


