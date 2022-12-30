class MojeSlowniki(dict):
    def __missing__(self, key):
        return "taki klucz nie istnieje"

konkurs = {'Ala':87,'Ola':45,'Jan':62,'Olaf':88}
print(konkurs['Jan'])
#print(konkurs['Ula'])

ms = MojeSlowniki(konkurs)
print(ms['Ola'])
print(ms['Ula'])
