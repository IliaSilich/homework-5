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
    for char in message.upper():
        if char == ' ':
            morse_message += ' '
        else:
            for morse_code, letter in morse_alphabet.items():
                if char == letter:
                    morse_message += morse_code
                    break
    return morse_message


user_input = input("Введите сообщение для преобразования в код Морзе: ")

morse_formatted_f = f"f-string: {to_morse_code(user_input)}"
morse_formatted_percent = "%s: %s" % ("%", to_morse_code(user_input))
morse_formatted_format = "format: {}".format(to_morse_code(user_input))

print(morse_formatted_f)
print(morse_formatted_percent)
print(morse_formatted_format)
