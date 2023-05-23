def came_or_gone():
    count_guests = len(guests)
    print('Сейчас на вечеринке', count_guests, 'человек:', guests)
    ansver = str(input('Гость пришёл или ушёл? '))
    if ansver == 'Пора спать':
        print('\nВечеринка закончилась, все легли спать.')
    else:
        if ansver == 'пришёл':
            name = str(input('Имя гостя: '))
            if count_guests >= 6:
                print('Прости,', name, ', но мест нет.')
            else:
                guests.append(name)
        elif ansver == 'ушёл':
            name = str(input('Имя гостя: '))
            guests.remove(name)
            print('Пока,', name,'!')
        came_or_gone()


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

came_or_gone()


