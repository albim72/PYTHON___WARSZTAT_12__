from figura import Figura

class Kwadrat(Figura):

    def __init__(self,a):
        super().__init__(a,0)

    def pole_figury(self):
        return self.a**2

