def exam_weight():
    weight = int(input('Введите вес контейнера: '))
    if weight > 200:
        print('Ошибка. Вес контейнера не должен превышать 200')
        return exam_weight()
    else:
        return weight


quantity = int(input('Количество контейнеров: '))
containers_list = []

for _ in range(quantity):
    containers_list.append(exam_weight())

print()

new_container_weight = int(input('Введите вес нового контейнера: '))

for i in range(quantity):
    if containers_list[i] >= new_container_weight:
        new_container_number = i + 2

print()
print('Номер, который получит новый контейнер: ', new_container_number)
