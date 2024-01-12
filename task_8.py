morse_alphabet = {
    '.-  ': 'А', '-...': 'Б', '- --': 'В', '--. ': 'Г',
    '-.. ': 'Д', '.   ': 'Е', '...-': 'Ж', '--..': 'З',
    '..  ': 'И', '.---': 'Й', '-.- ': 'К', '.-..': 'Л',
    '--  ': 'М', '-.  ': 'Н', '--- ': 'О', '.--.': 'П',
    '.-. ': 'Р', '... ': 'С', '-   ': 'Т', '..- ': 'У',
    '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч',
    '----': 'Ш', '--.-': 'Щ', '-. -': 'Ъ', '-.--': 'Ы',
    '-..-': 'Ь', '. -.': 'Э', '..--': 'Ю', '.-.-': 'Я',
}


def to_morse_code(message):
    morse_message = ''
    for i in range(0, len(message), 4):
        symbol = message[i:i+4]
        for morse_code, letter in morse_alphabet.items():
            if symbol == morse_code:
                morse_message += letter
                break
    return morse_message


user_input = input("Введите код Морзе для преобразования в сообщение: ")

user_input = ''.join(filter(lambda x: x in '-. ', user_input))
morse = to_morse_code(user_input)

print(f"f-string: {morse}")
print("%s: %s" % ("%", morse))
print("format: {}".format(morse))
