
def examinator(i_line):
    splited_line = i_line.split(' ')
    if len(splited_line) != 3:
        return IndexError('НЕ присутствуют все три поля')

    elif not splited_line[0].isalpha():
        return NameError('Поле «Имя» содержит НЕ только буквы')

    elif not ('@' and '.') in splited_line[1]:
        return SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')

    elif not (splited_line[2][:-1].isdigit() and (10 < int(splited_line[2]) < 99)):
        return ValueError('Поле «Возраст» НЕ является числом от 10 до 99')

    else:
        return False


with open('registrations.txt', 'r', encoding='utf-8') as file_data,\
        open('registrations_bad.log', 'w') as reg_bad,\
        open('registrations_good.log', 'w') as reg_good:
    for i_line in file_data:
        try:
            answer = examinator(i_line)
            if answer:
                raise answer
        except (IndexError, NameError, SyntaxError, ValueError) as exc:
            error_message = f'{i_line.rstrip()} - {exc.__class__.__name__} - {exc}\n'
            reg_bad.write(error_message)
        else:
            reg_good.write(i_line)