import random


class warior():  # TODO 1) имена классов пишутся КэмелКейсом; 2) если предков нет, то скобки не нужны
    helth_points = 100  # TODO ошибка в слове "здоровье"
    attack_damage = 20

    def __init__(self, name):   # не до конца понимаю для чего этот блок?
        self.name = name        # Пока предполага, что аргументы которые мы объявляем в __init__
                                # позже можем передавать напрямую в скобка, в заданном порядке
                                # TODO Этот метод вызывается для инициализации атрибутов экземпляра класса при создании
                                #  экземпляра (объекта) класса, как, например, в данном случае для имени

    def punch(self, attacked):
        attacked.helth_points -= self.attack_damage
        print('{} атакует!\n У {} осталось {} здоровья'.format(
            self.name, attacked.name, attacked.helth_points)
        )


unit_1 = warior('Scorpion')
unit_2 = warior('Sub_Zero')

while True:
    if unit_1.helth_points > 0 and unit_2.helth_points > 0:
        change = random.choice([unit_1.name, unit_2.name])
        if change == unit_1.name:
            unit_1.punch(unit_2)
        else:
            unit_2.punch(unit_1)
        print('\n------------------\n')
    else:
        print('\nПобедил {} !!!!'.format(change))
        break
