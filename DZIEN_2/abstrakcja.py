from abc import ABC,abstractmethod

class Monster(ABC):
    def __init__(self,rodzaj,sila,dlugosc,waga):
        self.rodzaj = rodzaj
        self.sila = sila
        self.dlugosc = dlugosc
        self.waga = waga

    def opis(self):
        return f'Potwór -> rodzaj: {self.rodzaj}, siła: {self.sila} punktów'

    @abstractmethod
    def sila_uderzenia(self):
        pass

    @abstractmethod
    def dodanie_pkt_sily(self,liczba_zabitych):
        return liczba_zabitych*1.2*self.sila #ciało domyślne metody abstrakcyjnej


class Smok(Monster):

    def sila_uderzenia(self):
        return self.sila + 0.2*self.dlugosc + 0.056*self.waga

    def dodanie_pkt_sily(self, liczba_zabitych):
        return super().dodanie_pkt_sily(liczba_zabitych) + 10


s = Smok("smok chiński",34,45,1200)

print(s.opis())
print(f'siła uderzenia potwora: {s.__class__.__name__} -> {s.sila_uderzenia()} punktów')
print(f'przyrost punktów siły: {s.dodanie_pkt_sily(5)} punktów')
