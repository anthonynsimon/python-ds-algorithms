def greatestCommonDenominator(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class fraction:

    def __init__(self, top, bottom):
        self.__number = top
        self.__denominator = bottom

    def __str__(self):
        return "{0}/{1}".format(self.__number, self.__denominator)

    def asDecimal(self):
        return self.__number / self.__denominator

    def __add__(self, other):
        number = self.__number * other.denominator + self.__denominator * other.number
        denominator = self.__denominator * other.denominator
        common = greatestCommonDenominator(number, denominator)
        return fraction(number//common, denominator//common)


myFraction = fraction(1,2)
newFrac = myFraction + fraction(1,2)
print("{0} as decimal is {1}".format(myFraction, myFraction.asDecimal()))
print("{0} as decimal is {1}".format(newFrac, newFrac.asDecimal()))