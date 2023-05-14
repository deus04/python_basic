def serch_films(favorite_films):
    flag = 0
    request = str(input('Введите название фильма: '))
    for i in range(len(films)):
        if films[i] == request:
            flag = 1

    if flag == 1:
        favorite_films.append(request)
    else:
        print('Ошибка: фильма', request, ' у нас нет :(')

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

quantity = int(input('Сколько фильмов хотите добавить? '))
favorite_films = []

for _ in range(quantity):
    serch_films(favorite_films)

print('Ваш список любимых фильмов: ', end='')
for i in range(len(favorite_films)-1):
    print(favorite_films[i], end=', ')
print(favorite_films[-1])