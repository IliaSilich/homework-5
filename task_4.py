def format_book_info_fstring(book_info):
    title, author, year = map(str.strip, book_info.split(','))
    return f"{author.split()[-1]}, {' '.join(author.split()[:-1])}. {title}. {year}."


def format_book_info_percent(book_info):
    title, author, year = map(str.strip, book_info.split(','))
    return "%s, %s. %s. %s." % (author.split()[-1], ' '.join(author.split()[:-1]), title, year)


def format_book_info_format(book_info):
    title, author, year = map(str.strip, book_info.split(','))
    return "{}, {}. {}. {}.".format(author.split()[-1], ' '.join(author.split()[:-1]), title, year)


input_book_info = input("Введите название книги, автора и год издания, разделенные запятыми: ")

formatted_book_info_fstring = format_book_info_fstring(input_book_info)
print(f"F-strings: {formatted_book_info_fstring}")

formatted_book_info_percent = format_book_info_percent(input_book_info)
print("Percent: %s" % formatted_book_info_percent)

formatted_book_info_format = format_book_info_format(input_book_info)
print("Format: {}".format(formatted_book_info_format))
