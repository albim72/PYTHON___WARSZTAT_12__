try:
    n=1
    c=0
    print(n)
    wynik = n/c
except NameError:
    print("wartość n jest niezdefiniowana")
except Exception as ex:
    print(ex)
except:
    print("całkowicie nieznany błąd")
else:
    print(wynik)
finally:
    y = 99
    print(f"otatecznie y={y}")

print("ciąg dalszy")
