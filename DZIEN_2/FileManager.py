class FileManager(object):
    def __init__(self,filename,mode,encod):
        self.filename = filename
        self.mode = mode
        self.encod = encod
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,self.mode,encoding=self.encod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager('testowy.txt','w','utf-8') as f:
    f.write('to jest pierwsza linia tekstu\n')

with FileManager('testowy.txt','r','utf-8') as f:
    print(f.read())

print(f.closed)




