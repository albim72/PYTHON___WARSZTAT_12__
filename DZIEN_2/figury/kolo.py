from figura import Figura
import math

class Kolo(Figura):

    def __init__(self,a):
        super().__init__(a,0)

    def pole_figury(self):
        return math.pi*self.a**2

