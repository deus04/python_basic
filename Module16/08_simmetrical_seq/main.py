num = int(input('Кол-во чисел: '))
number_list = []
for _ in range(num):
    number_list.append(int(input('Число: ')))

ansver = []
print("Последовательность:", number_list)
flag = 0

if len(number_list) < 2:
    print('Ничего добавлять не нужно')
else:
    for _ in range(len(number_list)):
        count = 0
        for i in range(int(len(number_list) / 2)):
            if number_list[i] == number_list[(i + 1) * -1]:
                count += 1
        if count == int(len(number_list) / 2):
            break
        else:
            flag = 1
            ansver.append(number_list[0])
            number_list.remove(number_list[0])
    if flag == 0:
        print('Ничего добавлять не нужно')


new_list = []
count = len(ansver)
for i in range(-1, -count - 1, -1):
    new_list.append(ansver[i])

print('Нужно приписать чисел:', count)
print('Сами числа:', new_list)