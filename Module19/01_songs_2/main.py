violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

sound_numbers = ["первой",
                 "второй",
                 "третьей",
                 "четвертой",
                 "пятой",
                 "шестой",
                 "седьмой",
                 "восьмой",
                 "девятой"]

total_len = 0
total_sounds = int(input('Сколько песен выбрать? '))
for i_sound in sound_numbers[:total_sounds]:
    print("Название", i_sound, "песни: ", end='')
    total_len += violator_songs[str(input())]
print('Общее время звучания песен: {:.2f} минуты'.format(total_len))
