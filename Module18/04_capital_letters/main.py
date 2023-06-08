user_string = input('Введите строку: ')
split_string = user_string.split()
joined_word_list = []

for word in split_string:
    letter_list = list(word)
    letter_list[0] = letter_list[0].upper()
    joined_words = ''.join(letter_list)
    joined_word_list.append(joined_words)
result = ' '.join(joined_word_list)
print('Результат:', result)

# мне не понравилось :(
