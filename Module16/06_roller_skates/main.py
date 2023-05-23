skates = []
people = []

total_skates = int(input('Кол-во коньков: '))
for i in range(total_skates):
    print('Размер ', i + 1, '-й пары: ', sep='', end='')
    size = int(input(''))
    skates.append(size)
print()

total_people = int(input('Кол-во людей: '))
for i in range(total_people):
    print('Размер ноги ', i + 1, '-ого человека: ', sep='', end='')
    size = int(input(''))
    people.append(size)
print()

count = 0
for size_people in range(total_people):
    for size_skaters in range(total_skates):
        if people[size_people] == skates[size_skaters]:
            count += 1
            people[size_people] = 0
            skates[size_skaters] = 0
# TODO алгоритм не верный, насчитывает вдвое больше людей чем их в реальности есть.
#  Сделайте так: итерируя по списку коньков с помощью цикла for проверяйте наличие такого размера в списке людей
#  (оператор in) и если совпало - то увеличивайте счётчик и убрайте размер только из списка людей (это важно! список
#  коньков не надо модифицировать)


print('Наибольшее кол-во людей, которые могут взять ролики:', count)
