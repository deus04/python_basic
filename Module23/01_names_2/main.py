with open('people.txt', 'w', encoding='utf-8') as textfile:
    textfile.write('Василий\n'
                   'Николай\n'
                   'Надежда\n'
                   'Никита\n'
                   'Ян\n'
                   'Ольга\n'
                   'Евгения\n'
                   'Кристина')

number_str = 0
total_simbols = 0
with open('people.txt', 'r', encoding='utf-8') as textfile:
    for i_str in textfile:
        number_str += 1
        count_simbols = 0
        try:
            for i_simbol in i_str:
                if i_simbol != '\n':
                    count_simbols += 1
            total_simbols += count_simbols
            if count_simbols < 3:
                raise BaseException
        except BaseException:
            print(f'Ошибка! В строке {number_str} меньше 3х символов!')
print('Общее количество символов:', total_simbols)
