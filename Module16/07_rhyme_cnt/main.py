
#Задача подласть гадатсь ненавижу!
#Скатал из интернета! Фу ужас отвратительно!
total_players = int(input('Кол-во человек: '))
number = int(input('Какое число в считалочке? '))
print('Значит выбывает каждый ', 7, '-й человек', sep= '')
players = []
start_player = 1
looser = 0

for i in range(total_players):
    players.append(i + 1)
print()

while len(players) != 1:
   print('Текущий круг людей', players)  # TODO отступ должен быть ровно 4 пробела, не 3
   start_player = looser % len(players) # НЕОЧЕВИДНЫЙ ХОД!  todo этот приём достаточно часто используется и в других
                                                         #  задачах курса
   looser = (start_player + number - 1) % len(players) # У меня все было точно также, но СУММА в скобках! ФУ НЕПОНИМАЮ
   print('Начало счёта с номера', players[start_player])
   print('Выбывает человек под номером', players[looser])
   players.remove(players[looser])
   print()
print('Остался человек под номером', players[0])
# Очень расстроился, когда увидел, что на разборе ДЗ 8 задача, а не эта
# Требую РАЗБОРА!!
# TODO а что именно тут не ясно, на каком шаге сложность?
