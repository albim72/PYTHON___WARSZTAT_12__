class MojaKlasaBledu(Exception):
    def __init__(self,*args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("funkcja komunikatu błędu...")
        if self.message:
            return f'klasa {self.__class__.__name__} błąd: {self.message}'
        else:
            return f'klasa {self.__class__.__name__}'

try:
    raise MojaKlasaBledu("to jest mój komunikat!")
except MojaKlasaBledu as r:
    print(r)
