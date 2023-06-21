def search_synonym(synonym_dict):
    word = input('Введите слово: ')
    # if word:#in synonym_dict.keys():
    #
    #     return synonym_dict[word]
    # if word: #in synonym_dict.values():
    for i_key in synonym_dict:
        print(i_key)
        if i_key.lower() == word.lower():
            return synonym_dict[i_key] # не знаю как правильно взять ключи через значение
        elif synonym_dict[i_key].lower() == word.lower():
            return i_key
        else:
            print('Такого слова в словаре нет.')
            search_synonym(synonym_dict)    # не нравится что есть итерация через ключ, и то оно не хочет раотать
            # мне обесчали, что со списками будет искаться проще


number_word_pairs = int(input('Введите количество пар слов: '))
synonym_dict = {}

for number in range(number_word_pairs):  # вообще хз как сделать вывод "первая","вторая", .... их может быть оч много
    print(number + 1, '-я пара: ', sep='', end='')
    pair = input().split(' - ')
    synonym_dict[pair[0]] = pair[1]

print('Синоним: ', search_synonym(synonym_dict))
