from figura import Figura
from kwadrat import Kwadrat

class Prostokat(Figura):

    def __new__(cls, a:float, b:float):
        if a==b:
            return Kwadrat(a=a)
        return object.__new__(Prostokat)

    def pole_figury(self):
        return self.a*self.b
