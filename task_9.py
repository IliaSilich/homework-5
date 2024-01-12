def binary_to_int(code):
    binary_str = str(code)
    number = 0
    power = len(binary_str) - 1

    for bit in binary_str:
        if bit == '1':
            number += 2 ** power
        power -= 1

    return number


nrzi_codes = [
    '|¯¯|_|¯¯¯¯¯|_|¯|_',
    '|¯¯¯¯¯¯|___|¯|___|¯',
    '|¯|_|¯|______|¯¯|_',
    '|¯|__|¯¯|___|¯|__|¯',
]

total_sum = 0

for nrzi_code in nrzi_codes:
    binary_code = nrzi_code.replace("|¯", "1").replace("|_", "1").replace("_", "0").replace("¯", "0")
    decimal_value = binary_to_int(binary_code)
    total_sum += decimal_value

    print(f"NRZI: {nrzi_code}")
    print("Binary: %s" % binary_code)
    print("Decimal: {}".format(decimal_value))
    print("=" * 20)

print(f"Total Sum: {total_sum}")
