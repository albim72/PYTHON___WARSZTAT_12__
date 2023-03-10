from dataclasses import dataclass,Field
from datetime import datetime

#Field -> 'default','dafault factory','init','repr','hash','compare','metadata','kw_only'
params = {
    'name':Field(None,None,True,True,True,True,None,None),
    'surname':Field(None,None,True,True,True,True,None,None),
    'year_of_birth':Field(None,None,True,True,True,True,None,None)
}

def age(self):
    return datetime.now().year - self.year_of_birth

#dataclass(type(nazwa_klasy,klasy_dziedziczone,atrybuty_klasy))

Person = dataclass(type('Person',(),{'__annotations__':params,'age':property(age)}))

p = Person('Romualda','Tracz',1953)
print(p)
print(p.age)
