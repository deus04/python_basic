def summ_numbers(number):
    summ = 0
    for symbol in number:
        summ += int(symbol)
    return summ


def number_digits(number):
    count = 0
    number = int(number)
    while number > 0:
        number //= 10
        count += 1
    return count


number = str(input('Введите число: '))
print('Сумма чисел:', summ_numbers(number))
print('Количество цифр в числе:', number_digits(number))
print('Разность суммы и количества цифр:', summ_numbers(number) - number_digits(number))
