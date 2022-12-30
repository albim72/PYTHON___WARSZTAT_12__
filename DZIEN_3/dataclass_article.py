from dataclasses import dataclass

@dataclass
class Article:
    title:str
    content:str
    author:str

@dataclass(init=False)
class PyArticle(Article):
    language:str
    author:str
    price:int = 30

    def __init__(self,title,price):
        self.title = title
        self.price = price
        self.language = "Python 3"
        self.author = "Marcin Albiniak"
        self.content = "opis wybranych aspektów użycia jęzka Python"

    def rabat(self):
        print(f'publikacja -> {self.title}, autor: {self.author}, cena bazowa: {self.price} zł,'
              f' cena po rabacie: {0.9*self.price:.2f} zł')


art1 = PyArticle("Algorytmiczna teoria gier w Pythonie",67)
print(art1)
art1.rabat()

