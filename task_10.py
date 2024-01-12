def pluralize_word(word):
    if word.endswith(('s', 'x', 'z', 'ch', 'sh')):
        pluralized_word = f"{word}es"
    elif word.endswith('y') and len(word) > 1 and word[-2] not in 'aeiou':
        pluralized_word = f"{word[:-1]}ies"
    else:
        pluralized_word = f"{word}s"

    return pluralized_word


input_word = input("Введите слово на английском языке: ")
result = pluralize_word(input_word)
print(f"Множественное число: {result}")
