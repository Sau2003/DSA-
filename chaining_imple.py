class Myhash:
    def __init__(self,b):
        self.BUCKET=b
        self.table=[[]for x in range(b)]

    def insert(self,x):
        i=x%self.BUCKET
        self.table[i].append(x) 

    def remove(self,x):
        i=x%self.BUCKET
        self.table[i].remove(x)

    def search(self,x):
        i=x%self.BUCKET
        return x in self.table[i]            