from lib.data_structures import stack


def convert_base(decimal, base):
    digits = "0123456789ABCDEF"
    stack = Stacks.StackAA()
    number = decimal
    while number > 0:
        rem = number % base
        stack.push(rem)
        number = number // base

    items = []
    while not stack.is_empty():
        items.append(digits[stack.pop()])
    return "".join(items)

def binary_to_decimal(binary):
    binary = str(binary)
    result = 0
    position = 0
    while position < len(binary):
        if int(binary[position]) == 1:
            result += power_of((len(binary) - (position + 1)))
        position += 1
    return result

def power_of(n):
    result = 1
    while n >= 1:
        result *= 2
        n -= 1
    return result

print(binary_to_decimal(11111111))
print(convert_base(255, 2))