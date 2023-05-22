first = [1, 5, 3]
second = [1, 5, 1, 5]
third = [1, 3, 1, 5, 3, 3]

first.extend(second)  # added second, count and remove '5'
count = first.count(5)
print('Кол-во цифр 5 при первом объединении:', count)
for _ in range(count):
    first.remove(5)

first.extend(third)  # added third and count '3'
count = first.count(3)
print('Кол-во цифр 3 при втором объединении:', count)

print('Итоговый список:', first)
