binary_str = input("Введите число в двоичной системе: ")
decimal = int(binary_str, 2)
octal = oct(decimal)
hexadecimal = hex(decimal)


print(f"Decimal: {decimal}, Octal: {octal}, Hexadecimal: {hexadecimal}.")
print("Decimal: %d, Octal: %s, Hexadecimal: %s." % (decimal, octal, hexadecimal))
print("Decimal: {}, Octal: {}, Hexadecimal: {}.".format(decimal, octal, hexadecimal))
