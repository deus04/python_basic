import random
from operator import attrgetter


class Student:
    def __init__(self, full_name, group_number, performance, gpa): # Не пойму почему подчеркивает
        self.full_name = full_name
        self.group_number = group_number
        self.performance = performance
        self.gpa = gpa

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
    gpa = round(sum(performance)/len(performance), 2)
    i_student = Student(full_name, group_number, performance, gpa)
    students_list.append(i_student)

sorted_list = sorted(students_list, key=attrgetter('gpa'))
for i_student in sorted_list:
    i_student.info()

