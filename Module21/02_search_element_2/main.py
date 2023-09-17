site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def found_key(site, deep, search_key):
    if maximum_deep:
        if deep >= maximum_deep:
            return None

    if search_key in site:
        return site[search_key]
    else:
        deep += 1
        for i_value in site.values():
            if isinstance(i_value, dict):
                result = found_key(i_value, deep, search_key)
                if result:
                    break
        else:
            result = None

    return result


search_key = input('Введите искомый ключ: ')

deep = 0
question_deep = input('Хотите ввести максимальную глубину? Y/N: ').upper()
if question_deep == 'Y':
    maximum_deep = int(input('Введите максимальную глубину: '))
else:
    maximum_deep = 0

result_found_key = found_key(site, deep, search_key)
if result_found_key:
    print('Значение ключа: ', result_found_key)
else:
    print('Такого ключа нет')
