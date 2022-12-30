class Switch(object):
    value = None
    def __new__(cls, value):
        cls.value = value
        return True

def case(*args):
    return any((arg==Switch.value for arg in args))

n = int(input("podaj cyfrę systemu dziesiętnego (0-9): "))
s1 = Switch(n)
s2 = Switch(7)
print(type(s1))

print(s1==s2)
print(s1)
print(isinstance(s1,bool))
while Switch(n):
    if case(0):
        print("n wynosi 0")
        break
    if case(1,4,9):
        print("n jest kwadratem innej cyfry")
        break
    if case(2):
        print("n jest liczbą parzystą")
    if case(2,3,5,7):
        print("n jest liczbą pierwszą")
        break
    if case(6,8):
        print("n jest krotnością liczby")
        break
    print("pisz tylko cyfry!")
    break
