def czytaj(lista):
    for i,j in enumerate(lista):
        print(f'element listy nr {i+1} -> {j}')
        
def czytaj_slownik(slow):
    for x,y in slow.items():
        print(f'klucz -> {x}: wartość -> {y}')
