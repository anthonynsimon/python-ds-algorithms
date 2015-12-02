from DataStructures import Stacks


def baseConverter(decimal, base):
    digits = "0123456789ABCDEF"
    stack = Stacks.ALStack()
    number = decimal

    while number > 0:
        rem = number % base
        stack.push(rem)
        number = number // base

    stringOut = ""
    while not stack.isEmpty():
        stringOut += digits[stack.pop()]

    return stringOut

def binaryToDecimal(binary):
    binary = str(binary)
    result = 0
    position = 0
    while position < len(binary):
        if int(binary[position]) == 1:
            result += twoPower((len(binary)-(position+1)))
        position += 1
    return result

def twoPower(n):
    result = 1
    while n >= 1:
        result *= 2
        n -= 1
    return result

print(binaryToDecimal(1101000110001))