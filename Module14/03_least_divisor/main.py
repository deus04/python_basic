def least_divisor(number):
    for step in range(2, number):
        print(number % step)
        if number % step == 0:
            return step
    return number


number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', least_divisor(number))
