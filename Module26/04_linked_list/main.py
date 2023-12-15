class LinkedList(list):

    def __init__(self):
        self.linked_list = list()
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