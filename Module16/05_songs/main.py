def search_time(title):
    for track in violator_songs:
        if track[0] == title:
            return track[1]


violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

how_sounds = int(input('Сколько песен выбрать? '))
len_list = len(violator_songs)
total_time = 0

for i in range(how_sounds):
    print('Название ', i + 1, '-й песни: ', sep='', end='')
    title = str(input(''))
    total_time += search_time(title)

print('Общее время звучания песен:', round(total_time, 2), 'минуты')
