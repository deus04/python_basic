user_string = input('Введите строку: ')
user_string = user_string.split()
max_length = 0

for word in user_string:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

print('Самое длинное слово:', longest_word)
print('Длина этого слова:', max_length)
