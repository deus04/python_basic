def search(number, string):
    count = 0
    for symbol in str(string):
        if symbol == str(number):
            count += 1
    return count


def examination(year):
    flag = 0
    for number in str(year):
        if search(number, year) >= 3:
            flag = 1

    return flag


start_year = int(input('Введите первый год: '))
end_year = int(input('Введите второй год: '))

print('Годы от', start_year,'до', end_year, 'с тремя одинаковыми цифрами:')
for year in range(start_year, end_year):
    if examination(year) == 1:
        print(year)
