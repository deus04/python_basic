row = str(input('Введите строку: '))

new_row = row[row.rindex('h') - 1:row.index('h'):-1]

print('Развёрнутая последовательность между первым и последним h:', new_row)
