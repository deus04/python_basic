# TODO Видимо задание не вполне было ясно. Нужно создать два класса Узел и Связанный список, и реализовать основные
#  методы для работы с ними:
#
#
# Класс Узел (Node)
#     атрибуты "следующий узел" и "значение" (текущего узнал
#     методы:
#         возвращающий следующий узел
#         возвращий значение, которое храним в узле.
#
# Класс Связанный список (LinkedList)
#    атрибут "корневой узел"
#    методы "Добавление значения в связанный список в самое начало"
#           "Поиск узла с заданным индексом в списке" начиная с корневого - 0. Если ничего не найдено, то вовзращаем
#           пустые значения. Если мы найденный узел - корневой, то в кортеже - первым будет пустой узел.
#           "Получение значения узла с заданным индексом" начиная с корневого - 0.
#           "Удаление узла с заданным индексом" начиная с корневого - 0.
class LinkedList(list):  # TODO не стоит от list наследовать, просто создайте свой класс без наследования

    def __init__(self):
        self.linked_list = list()  # TODO принципиально не верно, наша структура данных это "связанный список" (точнее
                                   #  "односвязный список"), а не индексируемый список как list из состава python.
                                   #  Доп.материал: https://proproprogs.ru/structure_data/std-odnosvyaznyy-spisok-struktura-i-osnovnye-operacii?ysclid=lq89gzzt22640613064
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        self.end = len(self.linked_list)
        if self.start != self.end:
            return self.linked_list[self.start]
        else:
            raise StopIteration

    def __str__(self):
        result = list()
        for i_item in self.linked_list:
            result.append(i_item[0])
        return str(result)

    def append(self, new_item):
        next_link = None
        if not self.linked_list:
            self.linked_list.append([new_item, next_link])
        else:
            self.linked_list.append([new_item, self.linked_list[::-1][0][0]])
            # TODO возможно чтото намудрил

    def get(self, index):
        return self.linked_list[index][0]

    def remove(self, index):
        return self.linked_list.remove(self.linked_list[index])


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
for i_elem in my_list:
    print(i_elem)