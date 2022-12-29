#silnia -> n! = 1*2*3*...*n
#double -> max 1.8E+308
#n?? n=171 , min 2.4E-324
import sys
sys.set_int_max_str_digits(1000000)
sys.setrecursionlimit(0x1000000)
def silnia(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych")
    wynik=1
    for i in range(1,n+1):
        wynik*=i
    return wynik

def silnia_rek(n):
    if n < 0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych")
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)


try:
    n = int(input("podaj wartość argumentu n funkcji silnia: "))
    print(f'silnia z {n} wynosi: {silnia(n)}')
    print(f'silnia rekurencyjna z {n} wynosi: {silnia_rek(n)}')
except ValueError as d:
    print(d)
except Exception as ex:
    print(ex)
    raise
