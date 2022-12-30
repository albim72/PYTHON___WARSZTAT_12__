class SilniaError(Exception):
    
    def __init__(self,n):
        self.n = n
        
    def __str__(self):
        return f'wartość n = {self.n}. Funkcja silnia jest niezdefiniowana dla liczb ujemnych!'
