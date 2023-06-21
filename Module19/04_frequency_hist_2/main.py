text = input('Введите текст: ')
freq_dict = {}
invert_freq_dict = {}

for i_symbol in text:
    if i_symbol in freq_dict:
        freq_dict[i_symbol] += 1
    else:
        freq_dict[i_symbol] = 1

for i_key in sorted(freq_dict):
    print(i_key, ':', freq_dict[i_key])

for i_value in set(freq_dict.values()):
    symbol_list = []
    for i_key in freq_dict:
        if i_value == freq_dict[i_key]:
            symbol_list.append(i_key)
    invert_freq_dict[i_value] = symbol_list

print()
print('Инвертированный словарь частот:')
for i_key in invert_freq_dict:
    print(i_key, ':', invert_freq_dict[i_key])
