def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print("%i/%i" %(self.num, self.den))

    def __str__(self):
        return ("%i/%i" %(self.num, self.den))

    def showAsDecimal(self):
        print("%f" %(self.num / self.den))

    def __add__(self, other):
        newNum = self.num*other.den + self.den * other.num
        newDen = self.den * other.den
        common = gcd(newNum,newDen)

        return fraction(newNum//common, newDen//common)

myFraction = fraction(1,2)
myFraction.showAsDecimal()
newFrac = myFraction + fraction(1,2)
newFrac.showAsDecimal()