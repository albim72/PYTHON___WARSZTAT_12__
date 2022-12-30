import shutil
s = "taki krótki tekst, który wyśrodkujemy...."
r = 673485783476384756438
def print_center(s):
    print(s.center(shutil.get_terminal_size().columns))


print_center(s)
print_center(str(r))
