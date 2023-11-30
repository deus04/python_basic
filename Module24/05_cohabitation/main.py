import random


class Human:
    satiety = 50
    home = True

    def __init__(self, name):
        self.name = name

    def info(self):
        print("Name: {}\n"
              "Hunger: {}\n".format(
                self.name, self.satiety
                ))

    def eating(self):
        if home.food > 0:
            home.food -= 1
            self.satiety += 1
        print(self.name, ' поел')

    def go_to_work(self):
        self.satiety -= 1
        home.money += 1
        print(self.name, ' поработал')

    def play(self):
        self.satiety -= 1
        print(self.name, " поиграл")

    def go_shopping(self):
        home.food += 1
        home.money -= 1
        print(self.name, "сходил в магаз")


class Home:
    food = 50
    money = 0

    def info(self):
        print("Fridge: {}\n"
              "Money: {}\n".format(
                self.food, self.money
                ))


def day_by_day(human):
    if human.satiety < 20:
        human.eating()
    elif home.food < 10:
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
if roommate_1.satiety < 1:
    print('Подопечный {} не выжил!'.format(roommate_1.name))
elif roommate_2.satiety < 1:
    print('Подопечный {} не выжил!'.format(roommate_2.name))
else:
    print('Неплохо живем!')

roommate_1.info()
roommate_2.info()
home.info()
