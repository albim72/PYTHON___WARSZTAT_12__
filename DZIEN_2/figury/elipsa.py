from figura import Figura
from kolo import Kolo
import math

class Elipsa(Figura):

    def __new__(cls, a:float, b:float):
        if a==b:
            return Kolo(a=a)
        return object.__new__(Elipsa)

    def pole_figury(self):
        return math.pi*self.a*self.b
