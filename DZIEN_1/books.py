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

    def setoprawa(self,nowaoprawa):
        self.oprawa = nowaoprawa

    def getoprawa(self):
        return self.oprawa


b1 = Book(23,"Wiedźmin","Andrzej Sapkowski",39)
print(f'rabat na zakup książki: {b1.rabat():.2f} zł')
b1.setcena(46)
print(f'nowy rabat na zakup książki: {b1.rabat():.2f} zł -> do zapłaty: {b1.cena - b1.rabat():.2f} zł')
b1.setoprawa("twarda")
print(f'rodzaj oprawy: {b1.getoprawa()}')

print("___________________________________________________________")

b2 = Book(27,"Hobbit","J.R.R. Tolkien",32)
print(f'rabat na zakup książki: {b2.rabat():.2f} zł -> do zapłaty: {b2.cena - b2.rabat():.2f} zł')
print(f'rodzaj oprawy: {b2.oprawa}')
