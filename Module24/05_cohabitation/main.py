import random


class Human:
    hunger = 50
    home = True

    def __init__(self, name):
        self.name = name

    def info(self):
        print("Name: {}\n"
              "Hunger: {}\n".format(
                self.name, self.hunger
                ))

    def eating(self):
        self.hunger += 1  # TODO голод увеличился от еды? Назовите атрибут словом "сытость"
        Home.fridge -= 1
        # TODO Что если еды в доме меньше? Это не бесконечный ресурс, сначала надо проверить наличие
        #  и только потом уменьшать запас еды и увеличивать сытость
        print(self.name, ' поел')

    def go_to_work(self):
        self.hunger -= 1
        Home.money += 1
        print(self.name, ' поработал')

    def play(self):
        self.hunger -= 1
        print(self.name, " поиграл")

    def go_shopping(self):
        Home.fridge += 1
        Home.money -= 1
        print(self.name, "сходил в магаз")


class Home:
    fridge = 50  # TODO лучше назвать "еда", ведь холодильник не едят
    money = 0

    def info(self):
        print("Fridge: {}\n"
              "Money: {}\n".format(
                self.fridge, self.money
                ))


def day_by_day(human):
    if human.hunger < 20:
        human.eating()
    elif home.fridge < 10:
        human.go_shopping()
    elif home.money < 50:
        human.go_to_work()
    elif dice == 1:
        human.go_to_work()
    elif dice == 2:
        human.eating()
    else:
        human.play()


roommate_1 = Human('Viktor')
roommate_2 = Human('Igor')
home = Home()

for i_day in range(365):
    print('\nДень: ', i_day + 1)
    dice = random.randint(1, 6)
    print('Выпало: ', dice)
    day_by_day(roommate_1)
    dice = random.randint(1, 6)
    print('Выпало: ', dice)
    day_by_day(roommate_2)


print()
if roommate_1.hunger < 1:
    print('Подопечный {} не выжил!'.format(roommate_1.name))
elif roommate_2.hunger < 1:
    print('Подопечный {} не выжил!'.format(roommate_2.name))
else:
    print('Неплохо живем!')

roommate_1.info()
roommate_2.info()
home.info()
