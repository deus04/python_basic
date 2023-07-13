symbols_string = input('Введите строку: ')
key_sym = 0
symbols_dict = {}
for i_sym in symbols_string: # заполняем словарь
    if i_sym not in symbols_dict:
        symbols_dict[i_sym] = 1
    else:
        symbols_dict[i_sym] = int(symbols_dict[i_sym]) + 1

for i_sym in symbols_dict: # проверяем
    if symbols_dict[i_sym] % 2 == 1:
        key_sym += 1

if key_sym > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')