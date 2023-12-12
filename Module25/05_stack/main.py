import operator


class Stack:
    stack_list = list()

    def add_task(self, name):
        self.stack_list.append(name)

    def delete_task(self):
        self.stack_list.pop()


class TaskManager:
    manager_stack = Stack()
    pairs_list = list()

    def new_task(self, name, priority):
        self.manager_stack.add_task(name)
        self.pairs_list.append([name, priority])

    def __str__(self):
        main_str = str()
        sorted_pairs_list = sorted(self.pairs_list, key=operator.itemgetter(1))
        dict_pairs = dict()
        for i_item in sorted_pairs_list:
            if i_item[1] in dict_pairs:
                dict_pairs[i_item[1]] += '; {}'.format(i_item[0])
            else:
                dict_pairs[i_item[1]] = i_item[0]
        for i_key, i_value in dict_pairs.items():
            main_str += '{} {}\n'.format(i_key, i_value)
        return main_str


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)









