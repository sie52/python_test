from collections import UserString

class Mystring(UserString):
    def head(self, n=1):
        # Renvoie les n premières lettres
        return self.data[:n]

    def tail(self, n=1):
        # Renvoie les n dernières lettres 
        return self.data[-n:]

s1 = Mystring("prepa big data")
print(s1.data)       # affiche: prepa big data
print(s1.head())     # affiche: p
print(s1.head(2))    # affiche: pr
print(s1.tail())     # affiche: a
print(s1.tail(3))    # affiche: ata
