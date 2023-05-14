scroll = [1, 4, -3, 0, 10]
print('Изначальный список: ', scroll)
repit = len(scroll) - 1

for _ in range(repit):
    for i in range(repit):
        if scroll[i] > scroll[i + 1]:
            scroll[i], scroll[i + 1] = scroll[i + 1], scroll[i]
print('Отсортированный список: ', scroll)
