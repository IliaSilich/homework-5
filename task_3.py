def count_words_fstring(sentences):
    sentences_list = sentences.split('. ')
    formatted_output = ""
    for index, sentence in enumerate(sentences_list, start=1):
        words = len(sentence.split())
        formatted_output += f"Sentence {index} has {words} words. "

    return formatted_output


def count_words_percent(sentences):
    sentences_list = sentences.split('. ')
    formatted_output = ""
    for index, sentence in enumerate(sentences_list, start=1):
        words = len(sentence.split())
        formatted_output += "Sentence %d has %d words. " % (index, words)

    return formatted_output


def count_words_format(sentences):
    sentences_list = sentences.split('. ')
    formatted_output = ""
    for index, sentence in enumerate(sentences_list, start=1):
        words = len(sentence.split())
        formatted_output += "Sentence {} has {} words. ".format(index, words)

    return formatted_output


input_sentences = input("Введите несколько предложений: ")

formatted_fstring = count_words_fstring(input_sentences)
print(f"F-strings: {formatted_fstring}")

formatted_percent = count_words_percent(input_sentences)
print("Percent: %s" % formatted_percent)

formatted_format = count_words_format(input_sentences)
print("Format: {}".format(formatted_format))
