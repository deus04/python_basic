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
for size_skaters in skates:
    for size_people in people:
        if size_people == size_skaters:
            count += 1
            people.remove(size_people)

print('Наибольшее кол-во людей, которые могут взять ролики:', count)
