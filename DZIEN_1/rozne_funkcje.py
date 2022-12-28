#różne definicje funkcji

def fx(h):
    return h**4

n = 120
def policz(a,b,c,y):
    global n
    n = (a+b)*y-c+n + fx(b)
    return n

print(policz(3,6,7,3))
print(n)
