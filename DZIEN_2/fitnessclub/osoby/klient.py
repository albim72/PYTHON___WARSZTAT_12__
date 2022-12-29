from osoby.trener import Trener
from rep.sport import Sport

class Klient(Trener,Sport):
    def __init__(self,nr_klienta,imie,wiek,waga,wzrost,nr_kb,nazwa,miasto,dyscyplina,lata_upr,zyciowka,
                 nr_licencji=""):
        Trener.__init__(self,imie,wiek,waga,wzrost,nr_licencji,"","",nr_kb,nazwa,miasto)
        Sport.__init__(self,dyscyplina,lata_upr,zyciowka)
        self.nr_klienta = nr_klienta
        self.numerklienta()


    def numerklienta(self):
        print(f'przydzielono nr klienta: {self.nr_klienta}')
