def search_synonym(synonym_dict):
    word = input('Введите слово: ')
    answer = str
    flag = 0
    for i_key in synonym_dict:
        if i_key.lower() == word.lower():
            answer = synonym_dict[i_key]
            flag = 1
            print(i_key, synonym_dict[i_key])

    if flag == 1:
        print(answer)
        return answer
    else:
        print('Такого слова в словаре нет.')
        search_synonym(synonym_dict)


number_word_pairs = int(input('Введите количество пар слов: '))
synonym_dict = {}

for number in range(number_word_pairs):
    print(number + 1, '-я пара: ', sep='', end='')
    pair = input().split(' - ')
    synonym_dict[pair[0]] = pair[1]
    synonym_dict[pair[1]] = pair[0]

synonym = search_synonym(synonym_dict)
print('Синоним: ', synonym) # не понимаю почему возвращает None

# 1-я пара: Привет - Здравствуйте
# 2-я пара: Печально - Грустно
# 3-я пара: Весело - Радостно

# Введите количество пар слов: 3
# 1-я пара: Привет - Здравствуйте
# 2-я пара: Печально - Грустно
# 3-я пара: Весело - Радостно
# Введите слово: lf
# Такого слова в словаре нет.
# Введите слово: здравствуйте
# Здравствуйте Привет
# Привет
# Синоним:  None