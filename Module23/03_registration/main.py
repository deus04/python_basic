
def examinator(i_line):
    splited_line = i_line.split(' ')
    if len(splited_line) != 3:
        return IndexError
    elif not splited_line[0].isalpha():
        return NameError
    elif not ('@' and '.') in splited_line[1]:
        return SyntaxError
    elif not (splited_line[2][:-1].isdigit() and (10 < int(splited_line[2]) < 99)):
        return ValueError

    else:
        return False




sep = ' --- '

with open('registrations.txt', 'r', encoding='utf-8') as file_data:
    with open('registrations_bad.log', 'w') as reg_bad:
        with open('registrations_good.log', 'w') as reg_good:
            for i_line in file_data:
                try:
                    answer = examinator(i_line)
                    if answer:
                        raise answer
                except IndexError:
                    reg_bad.write(i_line[:-1] + sep + 'НЕ присутствуют все три поля\n')
                except NameError:
                    reg_bad.write(i_line[:-1] + sep + 'Поле «Имя» содержит НЕ только буквы\n')
                except SyntaxError:
                    reg_bad.write(i_line[:-1] + sep + 'Поле «Имейл» НЕ содержит @ и . (точку)\n')
                except ValueError:
                    reg_bad.write(i_line[:-1] + sep + 'Поле «Возраст» НЕ является числом от 10 до 99\n')
                else:
                    reg_good.write(i_line)