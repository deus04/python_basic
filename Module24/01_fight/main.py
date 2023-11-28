import random


class Warior:
    health_points = 100
    attack_damage = 20

    def __init__(self, name):
        self.name = name

    def punch(self, attacked):
        attacked.health_points -= self.attack_damage
        print('{} атакует!\n У {} осталось {} здоровья'.format(
            self.name, attacked.name, attacked.health_points)
        )


unit_1 = Warior('Scorpion')
unit_2 = Warior('Sub_Zero')

while True:
    if unit_1.health_points > 0 and unit_2.health_points > 0:
        change = random.choice([unit_1.name, unit_2.name])
        if change == unit_1.name:
            unit_1.punch(unit_2)
        else:
            unit_2.punch(unit_1)
        print('\n------------------\n')
    else:
        print('\nПобедил {} !!!!'.format(change))
        break
