import random

sum_numbers = 0
out_file = open('out_file.txt','w') # Не уверен в этой строке.
# Она нужна чтобы создать чистый файл, но может можно както покрасивее
# TODO один раз откройте файл на запись тут: with open('out_file.txt', 'w') as out_file: а нижеследующий код поместите
#  в этот контекстный менеджер. Так и работа ускорится, за счёт отсутствия открытия/закрытия файла для каждой отдельной
#  записи
try:
    while sum_numbers < 777:
        get_num = int(input("Введите число: "))
        test_your_luck = random.randint(1, 13)
        if test_your_luck != 13:
            with open('out_file.txt', 'a') as out_file:
                out_file.write(str(get_num) + '\n')
            sum_numbers += get_num
        else:
            raise BaseException  # TODO Аналогично предыдущему
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
except BaseException:
        print('Вас постигла неудача!')

