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
