class Klub:
    def __init__(self,nr_kb,nazwa,miasto):
        self.nr_kb = nr_kb
        self.nazwa = nazwa
        self.miasto = miasto
        
    def k_przypisanie(self):
        print(f"przyspisanie do klubu nr {self.nr_kb}")
        
    def infoklub(self):
        return f'klub: {self.nazwa}, miasto: {self.miasto}'
