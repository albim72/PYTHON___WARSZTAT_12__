import math

print((lambda e:e**3)(45))

b = lambda u,w=2:u/w-3

print(b(4,7))
print(b(4))

def zw(u,w):
    return u/w-3

print(zw(4,6))

def multi(n):
    return lambda a:a*n*math.sqrt(a)

print(multi(6)(7))
