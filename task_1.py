def format_number(phone_number):
    if len(phone_number) != 11 or not phone_number.isdigit():
        return "Некорректный номер"

    f_string_fr = f"+375 ({phone_number[2:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
    percent_fr = "+375 (%s) %s-%s-%s" % (phone_number[2:4], phone_number[4:7], phone_number[7:9], phone_number[9:])
    format_fr = "+375 ({}) {}-{}-{}".format(phone_number[2:4], phone_number[4:7], phone_number[7:9], phone_number[9:])

    return f"F-strings: {f_string_fr}\n" \
           f"Percent: {percent_fr}\n" \
           f"Format: {format_fr}"


phone = input("Введите номер телефона (11 цифр): ")

print(format_number(phone))
