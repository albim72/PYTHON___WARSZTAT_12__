def moja_f(a,*args,**kwargs):
    for key,value in kwargs.items():
        print(f'{key}: {value}')
    for a in args:
        print(f'argument -> {a}')

moja_f(34,5,7,8,pierwszy=12,miasto = "Toruń",ostatni=True)
