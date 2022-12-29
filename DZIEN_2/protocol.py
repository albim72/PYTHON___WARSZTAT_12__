from typing import List, Protocol

class Item(Protocol):
    quantity:float
    price:float

class Product:
    def __init__(self,name:str,quantity:float,price:float):
        self.name = name
        self.quantity = quantity
        self.price = price


def calculate_total(items: List[Item]) -> float:
    return sum([item.quantity*item.price for item in items])

total = calculate_total([
    Product('A',11,145),
    Product('B',2,999),
    Product('C',34,8.89),
    Product('D',200,2.89)
])

print(total)
