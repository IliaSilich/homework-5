input_text = input("Введите несколько слов, разделенных пробелами: ")

words = input_text.split()
words.reverse()
reversed_words = ' '.join(words)

print(f"F-strings: {reversed_words}")
print("Percent: %s" % reversed_words)
print("Format: {}".format(reversed_words))
