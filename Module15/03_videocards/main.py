quantity = int(input('Количество видеокарт: '))
old_videocards_list = []

for i in range(quantity):
    print(i + 1, "Видеокарта: ", end='')
    old_videocards_list.append(int(input()))

maximum = 0
for i in range(quantity):  # TODO вместо цикла можно использовать функцию max
    if maximum < old_videocards_list[i]:
        maximum = old_videocards_list[i]

new_videocards_list = []
for i in range(quantity):
    if old_videocards_list[i] != maximum:
        new_videocards_list.append(old_videocards_list[i])

print('Старый список видеокарт', old_videocards_list)
print('Новый список видеокарт', new_videocards_list)
