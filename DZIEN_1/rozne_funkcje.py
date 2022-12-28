#różne definicje funkcji
#przykład 1
import math

def fx(h):
    return h**4

n = 120
def policz(a,b,c,y):
    global n
    n = (a+b)*y-c+n + fx(b)
    return n

print(policz(3,6,7,3))
print(n)

#przykład 2

def gx(n,m=3,k=3,b=5):
    return math.sqrt(n+m)*k-b

print(gx(2,7,8,12))
print(gx(6,4,2))
print(gx(5,8))
print(gx(9))
print(gx(11,7,b=15))

