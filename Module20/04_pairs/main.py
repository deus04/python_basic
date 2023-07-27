import random

num_list = [random.randint(1, 100) for i_num in range(10)]
print('Оригинальный список:', num_list)

i_index = 0
new_list = [tuple([num_list[i_index], num_list[i_index + 1]])
            for i_index in range(10) if i_index % 2 == 0]

print('Новый список:', new_list)
