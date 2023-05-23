total_players = int(input('Кол-во человек: '))
number = int(input('Какое число в считалочке? '))
print('Значит выбывает каждый ', 7, '-й человек', sep='')
players = []
start_player = 1
looser = 0

for i in range(total_players):
    players.append(i + 1)
print()

while len(players) != 1:
    print('Текущий круг людей', players)
    start_player = looser % len(players)
    looser = (start_player + number - 1) % len(players)
    print('Начало счёта с номера', players[start_player])
    print('Выбывает человек под номером', players[looser])
    players.remove(players[looser])
    print()
print('Остался человек под номером', players[0])
