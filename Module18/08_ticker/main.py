first_string = list(input('Первая строка: '))
second_string = list(input('Вторая строка: '))

flag = 0
shift = 0

for i_symbol in first_string:
    if first_string != second_string:
        first_string.append(first_string[0])
        first_string.remove(first_string[0])
        shift += 1
    else:
        flag = 1
        break
if flag == 1:
    print('Первая строка получается из второй со сдвигом', shift)
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')