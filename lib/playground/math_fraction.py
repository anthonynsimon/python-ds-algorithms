# Greatest Common Denominator calculation
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n


class Fraction:

    def __init__(self, top, bottom):
        self.number = top
        self.denominator = bottom

    def __str__(self):
        return "{0}/{1}".format(self.number, self.denominator)

    def to_decimal(self):
        return self.number / self.denominator

    def __add__(self, other):
        number = self.number * other.denominator + self.denominator * other.number
        denominator = self.denominator * other.denominator
        common = gcd(number, denominator)
        return Fraction(number // common, denominator // common)


my_fraction = Fraction(1, 2)
new_fraction = my_fraction + Fraction(1, 2)
print("{0} as decimal is {1}".format(my_fraction, my_fraction.to_decimal()))
print("{0} as decimal is {1}".format(new_fraction, new_fraction.to_decimal()))