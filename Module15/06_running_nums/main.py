length = int((input('Введите длину ряда: ')))
old_list = []
old_list_index = []
new_list = []

for i in range(length):
    old_list.append(i + 1)
    old_list_index.append(i)

shift = int(input('Сдвиг: '))
shift %= length

print('Изначальный список: ', old_list)

for i in range(length):
    old_list_index[i] -= shift
    old_list_index[i] %= length
    new_list.append(old_list[old_list_index[i]])
print('Сдвинутый список: ', new_list)
