class Book:
    
    # deklaracja stanu -> konstruktor klasy -> __new__ , __init__
    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()
        
    #definicja zachowania -> funkcje klasy -> metody
    
    def create_book(self):
        print("nowa pozycja książkowa została utworzona...")
        
    def rabat(self):
        return 0.1*self.cena
    
    def setcena(self,nowacena):
        self.cena = nowacena
