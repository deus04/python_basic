file_name = input('Название файла: ')
special_symbols = list('@№$%^&\*()')

for symbol in special_symbols:
    if file_name.startswith(symbol):
        print('Ошибка: название начинается на один из специальных символов.')
        break
    elif not file_name.endswith('.txt' or '.docx'):
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
        break
    else:
        print('Файл назван верно.')
        break

# мне не очень нравится структура. Цикл вверху какбудто лишний,
# но не знаю как его вписать в ветвление