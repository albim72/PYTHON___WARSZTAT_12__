class Osoba:
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolor_oczu = "brązowe"
        self.trener = False
        self.info()
        
    def info(self):
        print("utworozno nowy obiket klasy Osoba...")
        
    def print_osoba(self):
        print(f'osoba -> {self.imie}, wiek: {self.wiek}, waga: {self.waga} kg, '
              f'wzrost: {self.wzrost} cm, kolor oczu: {self.kolor_oczu}')
        
    def czytrener(self):
        return self.trener
