enter_string = input('Введите строку: ')
summator = 1
i = 1
codded_string = []

for symbol in enter_string[:-1]:
    if symbol == enter_string[i]:
        summator += 1
    else:
        codded_string.append(symbol)
        codded_string.append(str(summator))
        summator = 1
    i += 1
codded_string.append(enter_string[-1])
codded_string.append(str(summator))
codded_string = ''.join(codded_string)

print(codded_string)