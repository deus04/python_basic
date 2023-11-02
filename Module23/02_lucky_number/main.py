import random

sum_numbers = 0
out_file = open('out_file.txt','w') # Не уверен в этой строке.
# Она нужна чтобы создать чистый файл, но может можно както покрасивее
try:
    while sum_numbers < 777:
        get_num = int(input("Введите число: "))
        test_your_luck = random.randint(1, 13)
        if test_your_luck != 13:
            with open('out_file.txt', 'a') as out_file:
                out_file.write(str(get_num) + '\n')
            sum_numbers += get_num
        else:
            raise BaseException
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
except BaseException:
        print('Вас постигла неудача!')

