def contacts(phone_book_dikt):
    choose = int(input('Выберете действие\n'
                      '1) Добавить контакт\n'
                      '2) Поиск человека по фамилии\n'
                      'Выбор: '))
    if choose == 1:
        name, surname = tuple(input('Введите имя и фамилию нового контакта (через пробел):').split())
        if phone_book_dikt.get((name, surname),{}):
            print('Такой человек уже есть в контактах.')
        else:
            phone_number = int(input('Введите номер телефона: '))
            phone_book_dikt = {(name, surname):phone_number}
        print('Текущий словарь контактов', phone_book_dikt)
    elif choose == 2:
        surname = input('Введите фамилию для поиска: ')
        for i_contact in phone_book_dikt:
            if surname in i_contact:
                print(i_contact[0],i_contact[1],phone_book_dikt[i_contact])
            else:
                print('Такой контакт не найден')
    contacts(phone_book_dikt)


phone_book_dikt= {}
contacts(phone_book_dikt)