
#
#
# Класс Узел (Node)
#     атрибуты "следующий узел" и "значение" (текущего узнал
#     методы:
#         возвращающий следующий узел
#         возвращий значение, которое храним в узле.

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

# Класс Связанный список (LinkedList)
#    атрибут "корневой узел"
#    методы
#           "Поиск узла с заданным индексом в списке" начиная с корневого - 0. Если ничего не найдено, то вовзращаем
#           пустые значения. Если мы найденный узел - корневой, то в кортеже - первым будет пустой узел.
#           "Добавление значения в связанный список в самое начало"
#           "Получение значения узла с заданным индексом" начиная с корневого - 0.
#           "Удаление узла с заданным индексом" начиная с корневого - 0.


class LinkedList:
    def __init__(self):
        self.root_node = Node()

    def __str__(self):
        node = self.root_node
        result = str()
        while node.next:
            node = node.next
            result = result + str(node) + ' '
        return result

    def append(self, data):
        new_node = Node(data)
        node = self.root_node
        while node.next:
            node = node.next
        node.next = new_node
        #print(new_node)

    def get(self, number):
        node = self.root_node
        for count in range(number):
            node = node.next
            # print('--------')
            # print(node.data)
            # print(node.next)
            # print('--------')

        return node

    def remove(self, number):
        node = self.root_node
        count = 0
        while node.next:
            node = node.next
            count += 1
            # print('----------')
            # print('number_node:', count)
            # print('node:', node.data)
            # print('node_next:', node.next)
            # print('----------')
            if count == number:
                save = node.next
                save_count = count
                # print('save', save)
                # print('save_count', save_count)
                break
        node = self.root_node
        count = 0
        while node.next:
            node = node.next
            count += 1
            if count == save_count - 1:
                node.next = save
            # print('----------')
            # print('number_node:', count)
            # print('node:', node.data)
            # print('node_next:', node.next)
            # print('----------')
    # TODO вариант на одном цикле:
    #  def remove(self, index: int) -> None:
    #         if index > self.__length or index < 0:
    #             return None
    #
    #         curr = self.__head
    #         prev = None
    #         idx = 0
    #         while curr is not None:
    #             if index == idx:
    #                 self.__length -= 1
    #                 if prev is None:
    #                     self.__head = curr.next_
    #                 else:
    #                     prev.next_ = curr.next_
    #
    #             idx += 1
    #             prev = curr
    #             curr = curr.next_

# node_1 = Node(5)
# print(node_1)
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)

print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(3))
print('Удаление второго элемента.')
my_list.remove(2)
print('Новый список:', my_list)

