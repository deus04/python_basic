class Parent:

    def __init__(self, name, age, children_list):
        self.name = name
        self.age = age
        ch_list = []
        for i_child in children_list:
            if self.age - i_child.age > 16:
                ch_list.append(i_child)
            else:
                print('{} не может быть ребенком {}'.format(i_child.name, self.name))
        self.children_list = ch_list

    def info(self):
        ch_list = []
        if self.children_list:
            for i_ch in self.children_list:
                ch_list.append(i_ch.name)
        print('Имя:{}\n'
              'Возраст:{}\n'
              'Список детей:{}\n'.format(
                self.name, self.age, ch_list
                ))

    def feed_child(self, person):
        print('{} пытается покормить {}'.format(self.name, person.name))
        flag = 0
        for i_child in self.children_list:
            if person.name == i_child.name:
                flag = 1
                print('Теперь {} не голоден'.format(person.name))
                person.satiety = 'Покушал'
        if flag == 0:
            print('Это не его ребенок!')

    def calm_child(self, person):
        print('{} пытается успокоить {}'.format(self.name, person.name))
        flag = 0
        for i_child in self.children_list:
            if person.name == i_child.name:
                flag = 1
                print('Теперь {} спокоен'.format(person.name))
                person.calm = 'Спокоен'
        if flag == 0:
            print('Это не его ребенок!')


class Child:

    def __init__(self, name, age, calm, hunger):
        self.name = name
        self.age = age
        self.calm = calm        # Спокоен, Бешеный
        self.hunger = hunger    # Голоден, Покушал

    def info(self):
        print('Имя:{}\n'
              'Возраст:{}\n'
              'Состояние спокойствия:{}\n'
              'Состояние голода:{}\n'.format(
                self.name, self.age, self.calm, self.hunger
                ))


child_1 = Child('Gloria', 3, 'Бешеный', 'Голоден')
child_2 = Child('Denise', 3, 'Бешеный', 'Голоден')
parent_1 = Parent('Jon', 23, [child_1])
parent_2 = Parent('Maria', 23, [child_1, child_2])

print()
child_1.info()
child_2.info()
parent_1.info()
parent_2.info()

print('Кормим: ')
parent_1.feed_child(child_1)
child_1.info()
parent_1.feed_child(child_2)
child_2.info()

print('Успокаиваем: ')
parent_1.calm_child(child_1)
child_1.info()
parent_1.calm_child(child_2)
child_2.info()




