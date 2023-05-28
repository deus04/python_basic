
len_list = int(input('Введите длину списка: '))
numbers = [1 if i % 2 == 0 else i % 5 for i in range(len_list)]
print(numbers)
