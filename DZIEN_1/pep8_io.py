marka = "Jeep"
model = "Cherokee"
rocznik = 2020

sam = "samochód -> marka: {}, model: {}, rocznik: {}."
print(sam.format(marka,model,rocznik))

sam = "samochód -> rocznik: {2}, marka: {0}, model: {1}."
print(sam.format(marka,model,rocznik))

# f-string
print(f"samochód -> marka: {{marka}}, model: \"{model}\", rocznik: {rocznik}")

konkurs = [
    ("Jan",56),
    ("Anna",67),
    ("Olga",34),
    ("Henryk",65),
    ("Olaf",44),
    ("Nadia",68),
    ("Janusz",54),
    ("Dariusz",32),
]

print("___________________________________")
print(list(enumerate(konkurs)))

print("__________________zestawienie wyników konkursu_________________")
for i, (imie,punkty) in enumerate(konkurs):
    print('nr %d: %-9s: %.1f punktów' %(i+1,imie,punkty))
