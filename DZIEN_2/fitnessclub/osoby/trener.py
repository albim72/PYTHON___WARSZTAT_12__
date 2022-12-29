from osoba import Osoba
from rep.klub import Klub

class Trener(Osoba,Klub):

    def __init__(self,imie,wiek,waga,wzrost,nr_licencji,lata_dosw,expert,
                 nr_kb,nazwa,miasto):
        Osoba.__init__(self,imie,wiek,waga,wzrost)
        Klub.__init__(self,nr_kb,nazwa,miasto)
        self.nr_licencji = nr_licencji
        self.lata_dosw = lata_dosw
        self.expert = expert
        self.trener = True

    def print_trener(self):
        print(f'trener nr licencji: {self.nr_licencji}, lata doświadczenia: {self.lata_dosw}, '
              f'poziom ekspercki ({self.expert})')
        

