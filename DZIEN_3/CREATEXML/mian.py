from xml.etree.ElementTree import Element, SubElement
import xml.etree.ElementTree as ET
from prettyfy import pretty

top = Element("grupa_osob")
os1 = SubElement(top,'osoba')

id = SubElement(os1,'id')
id.text = '56'

imie = SubElement(os1,'imie')
imie.text = 'Jan'

nazwisko = SubElement(os1,'nazwisko')
nazwisko.text = 'Kowalski'

parazdr = SubElement(os1,'param_zdrowia')

waga = SubElement(parazdr,'waga')
waga.text = '78'

wzrost = SubElement(parazdr,'wzrost')
waga.text = '173'
