import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]

print('Первая команда:', first_team)
print('Вторая команда:', second_team)

winners = [max(first_team[i_player],second_team[i_player]) for i_player in range(20)]
print('Победители турнира:', winners)
