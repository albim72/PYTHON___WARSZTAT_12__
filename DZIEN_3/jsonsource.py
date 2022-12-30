import json

jsonbook = '{"tytul":"Hobbit","autor":"J.R.R. Tolkien","oprawa":"twarda","lstron":245,"cena":23.77}'
print(jsonbook)
print(type(jsonbook))

book = json.loads(jsonbook)
print(book)
print(type(book))

print(book['autor'])

kolor = {
    "id":23423,
    "nazwa_koloru":"zółty ciemny",
    "paleta":"UC567",
    "lodcieni":3,
    "odcienie":["jasny","standard","ciemny"]
}
