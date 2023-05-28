vowels = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы', 'А', 'Я', 'У', 'Ю', 'О', 'Е', 'Ё', 'Э', 'И', 'Ы']
text = str(input('Введите текст: '))
print()

ansver = [] # возможно ответ можно получить както через срез, но не уверен
for i_word in text:
    for i_vowel in vowels:
        if i_vowel == i_word:
          ansver.append(i_word)

print(ansver)
