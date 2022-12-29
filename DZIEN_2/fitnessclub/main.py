from osoba import Osoba
from osoby.trener import Trener

os1 = Osoba("Feliks",45,99,178)
os1.print_osoba()
print(f'czy osoba jest trenerem personalnym? ({os1.czytrener()})')

print("_______________________________________")

os2 = Osoba("Olga",29,54,170)
os2.kolor_oczu = "niebieskie"
os2.print_osoba()
print(f'czy osoba jest trenerem personalnym? ({os2.czytrener()})')

print("_______________________________________")

tr1 = Trener("Jacek",37,80,189,"k654534",10,True,56,"złoty drążek","Tarnów")
tr1.print_osoba()
tr1.print_trener()
tr1.k_przypisanie()
print(tr1.infoklub())
print(f'czy osoba jest trenerem personalnym? ({tr1.czytrener()})')

print("_______________________________________")

tr2 = Trener("Ala",30,51,172,"RG66545",6,True,111,"Paker","Toruń")
tr2.print_osoba()
tr2.print_trener()
tr2.k_przypisanie()
print(tr2.infoklub())
print(f'czy osoba jest trenerem personalnym? ({tr2.czytrener()})')

print("_______________________________________")

