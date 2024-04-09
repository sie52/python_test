from math import gcd

class Fraction:
    def __init__(self, numérateur, dénominateur):
        self.numérateur = numérateur
        self.dénominateur = dénominateur

    def invert(self):
        return Fraction(self.dénominateur, self.numérateur)

    def simplify(self):
        pgcd = gcd(self.numérateur, self.dénominateur)
        return Fraction(self.numérateur // pgcd, self.dénominateur // pgcd)

    def __mul__(self, other):
        return Fraction(self.numérateur * other.numérateur, self.dénominateur * other.dénominateur)

    def __add__(self, other):
        nouveau_numérateur = self.numérateur * other.dénominateur + other.numérateur * self.dénominateur
        nouveau_dénominateur = self.dénominateur * other.dénominateur
        return Fraction(nouveau_numérateur, nouveau_dénominateur)

    def __sub__(self, other):
        nouveau_numérateur = self.numérateur * other.dénominateur - other.numérateur * self.dénominateur
        nouveau_dénominateur = self.dénominateur * other.dénominateur
        return Fraction(nouveau_numérateur, nouveau_dénominateur)

    def __truediv__(self, other):
        return Fraction(self.numérateur * other.dénominateur, self.dénominateur * other.numérateur)

    def __str__(self):
        return f"{self.numérateur}/{self.dénominateur}"

    @classmethod
    def from_string(cls, fraction_string):
        numérateur, dénominateur = map(int, fraction_string.split('/'))
        return cls(numérateur, dénominateur)

def main():
    f1 = Fraction(2, 4)
    f2 = Fraction(1, 4)
    f3 = f1 + f2
    f4 = f1 - f2
    f5 = f1 * f2
    f6 = f1 / f2
    f7 = Fraction(4, 10)
    f8 = Fraction.from_string('5/10')

    print(f3.simplify()) # affiche: 3/4
    print(f4.simplify()) # affiche: 1/4
    print(f5.simplify()) # affiche: 1/8
    print(f6.simplify()) # affiche: 2
    print(f7.simplify().simplify()) # affiche: 2/5
    print(f7.invert().simplify()) # affiche: 10/4
    print(f8.simplify()) # affiche: 5/10

main()
