from funkcje.bfunkcje import *

class KlasaDanych:
    def __init__(self,lista,slownik):
        self.lista = lista
        self.slownik = slownik
                
    def rlista(self):
        return czytaj(self.lista)
    
    def rslownik(self):
        return czytaj_slownik(self.slownik)
