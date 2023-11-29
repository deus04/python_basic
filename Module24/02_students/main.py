import random
from operator import attrgetter


class Student:
    def __init__(self, full_name, group_number, performance, gpa): # Не пойму почему подчеркивает
        # TODO 1) помечайте вопросы с помощью TODO, тогда их лучше видно
        #  2) подчеркивает потому-что точно такие же имена задействованы для глобальных переменных, что не особо важно,
        #  ведь мы не используем глобальные переменные, но в теории ухудшает чтение кода
        self.full_name = full_name
        self.group_number = group_number
        self.performance = performance
        self.gpa = gpa  # TODO это атрибут для списка оценок

    def info(self):
        print('Ф.И.:{}\n'
              'Номер группы:{}\n'
              'Успеваемость:{}\n'
              'Средний балл:{}\n'.format(
                self.full_name, self.group_number, self.performance, self.gpa
                                        ))


students_list = []
for i_student in range(10):
    full_name = '{} {}'.format(
        random.choice(['Иван', 'Алексей', 'Виктор', 'Георгий', 'Сергей']),
        random.choice(['Иванов', 'Петров', 'Котов', 'Козлов', 'Амбучбекович'])
    )
    group_number = random.randint(1, 3)
    performance = [random.randint(1, 5)
                   for i_item in range(5)]
    gpa = round(sum(performance)/len(performance), 2)  # TODO перенесите данный расчёт в метод класса Student
    i_student = Student(full_name, group_number, performance, gpa)
    students_list.append(i_student)

sorted_list = sorted(students_list, key=attrgetter('gpa'))  # TODO а тут используйте ключ в виде лябда-функции: key=lambda x: x.get_gpa()
for i_student in sorted_list:
    i_student.info()

