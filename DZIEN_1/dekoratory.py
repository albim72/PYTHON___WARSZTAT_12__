import math
import time

def pomiarczasu(funkcja):
    def wrapper(*args):
        starttime = time.perf_counter()
        funkcja(*args)
        endtime = time.perf_counter()
        print(f'czas wykonania funkcji: {endtime-starttime} s')
    return wrapper


def sleep(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()
    return wrapper

@pomiarczasu
@sleep
def big_lista():
    sum([i**5 for i in range(1000000)])


big_lista()

@pomiarczasu
def policz(a,b,c):
    return (a+b)-c

policz(6,3,6)

lt = [i**5 for i in range(1000000)]
@pomiarczasu
def gotowa_lista():
    sum(lt)

print("________________________________________")
gotowa_lista()

#dekorator z funkcją magiczną __name__
def debug(funkcja):
    def wrapper(*args,**kwargs):
        print(f'wołana funkcja to: {funkcja.__name__}')
        funkcja(*args)
    return wrapper

@debug
def info(i):
    print(f'informacja: {i}')

info("nr 2354353454")

@debug
def licz(x,y):
    print(f'wynik: {x/y}')

licz(4,5)

#repeater

def repeater(n):
    def wrapper(funkcja):
        def inner(*args):
            for i in range(n):
                funkcja(*args)
        return inner
    return wrapper

@repeater(n=5)
def komunikat(k,n):
    print(f'ważny komunikat: {k}, numer: {n}')

komunikat("abc",123)
