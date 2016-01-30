def convert_to_base(number, base):
    digits = "0123456789ABCDEF"
    if number < base:
        return digits[number]
    else:
        return convert_to_base(number // base, base) + digits[number % base]


print(convert_to_base(40, 2))