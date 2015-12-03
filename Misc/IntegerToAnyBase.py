def convertIntToBase(number,base):
    digits = "0123456789ABCDEF"
    if number < base:
        return digits[number]
    else:
        return convertIntToBase(number//base, base) + digits[number%base]


for i in range(10000):
    print(convertIntToBase(i,2))