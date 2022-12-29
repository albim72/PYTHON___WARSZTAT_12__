class Sport:
    def __init__(self,dyscyplina,lata_upr,zyciowka):
        self.dyscyplina = dyscyplina
        self.lata_upr = lata_upr
        self.zyciowka = zyciowka
        self.d_przypisanie()
        
    def d_przypisanie(self):
        print(f"przypisanie do dyscypliny: {self.dyscyplina}")
        
    def infosport(self):
        return f'{self.dyscyplina}, czas uprawiania /lata/: {self.lata_upr}, wynik życiowy: {self.zyciowka}'
