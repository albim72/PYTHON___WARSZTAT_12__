class Specjalna:
    def __init__(self):
        print("instancja została utworzona")

    def __call__(self, *args, **kwargs):
        print("instancja wołana przez funckję magiczną __call__")


ob = Specjalna()
ob()
