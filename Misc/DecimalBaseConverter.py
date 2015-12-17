class DecimalBaseConverter(object):

    def __init__(self):
        self.__digits = "0123456789ABCDEF"

    def convertToBase(self, number, base):
        if number < base:
            return self.__digits[number]
        else:
            return self.convertToBase(number // base, base) + self.__digits[number % base]


converter = DecimalBaseConverter()
for i in range(10001):
    print(converter.convertToBase(i, 16))