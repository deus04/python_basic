class Parent:

    def __init__(self, name, age, children_list):
        self.name = name
        self.age = age
        self.children_list = children_list
        # TODO до присваивания списка детей атрибуту надо проверить соответствие каждого ребенка ограничению по возрасту
        #  указанному в задании. Если ограничение не выполняется, то выбрасывать исключение

    def info(self):
        print('Имя:{}\n'
              'Возраст:{}\n'
              'Список детей:{}\n'.format(
                self.name, self.age, self.children_list
                ))

    def feed_child(self, person):
        for i_child in self.children_list:
            if person.name == i_child:
                person.hunger = 'Покушал'
            else:
                print('Это не его ребенок!')

    def calm_child(self, person):
        for i_child in self.children_list:
            if person.name == i_child:
                person.calm = 'Спокоен'
            else:
                print('Это не его ребенок!')


class Child:

    def __init__(self, name, age, calm, hunger):
        self.name = name
        self.age = age   # должен быть меньше возраста родителя хотя бы на 16 лет. Не понимаю как эту проверку вписать в описание класса
                         # TODO см. комментарий выше
        self.calm = calm        # Спокоен, Бешеный
        self.hunger = hunger    # Голоден, Покушал

    def info(self):
        print('Имя:{}\n'
              'Возраст:{}\n'
              'Состояние спокойствия:{}\n'
              'Состояние голода:{}\n'.format(
                self.name, self.age, self.calm, self.hunger
                ))


person_1 = Parent('Jon', 23, ['Denise'])
person_2 = Parent('Maria', 23, ['Denise', 'Gloria'])
person_3 = Child('Gloria', 3, 'Бешеный', 'Голоден')
person_4 = Child('Denise', 3, 'Бешеный', 'Голоден')

person_1.info()
person_3.info()

person_2.feed_child(person_3)
person_3.info()

person_1.calm_child(person_4)
person_4.info()







