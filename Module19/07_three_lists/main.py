array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
answer = []

print('Задача 1:')
for i_item in array_1:
    if (i_item in array_2) and (i_item in array_3) and (i_item not in answer):
        answer.append(i_item)
for i_item in array_2:
    if (i_item in array_1) and (i_item in array_3) and (i_item not in answer):
        answer.append(i_item)
for i_item in array_3:
    if (i_item in array_2) and (i_item in array_1) and (i_item not in answer):
        answer.append(i_item)

print(' * Решение без множеств:', answer)

answer = set(array_1) & set(array_2) & set(array_3)
print(' * Решение с множествами:', answer)

print('Задача 2:')
answer = []
for i_item in array_1:
    if (i_item not in array_2) and (i_item not in array_3) and (i_item not in answer):
        answer.append(i_item)
print(' * Решение без множеств:', answer)

answer = set(array_1) - set(array_2) - set(array_3)
print(' * Решение с множествами:', answer)

# Задача 2:
#  * Решение без множеств: [1, 5, 10, 40]
#  * Решение с множествами: {40, 1, 10, 5}
#                           /^^^^^^^^^^^^\
# Почему так странно располагаются элементы в множестве?