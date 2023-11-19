import random
from operator import attrgetter

class Student():
    full_name = 'Иван Иванов'
    group_number = 1
    performance = []
    gpa = 1      #TODO не совсем пониаю, правильно ли я задаю эти
                 # параметры, учитывая то, что позже я все переписываю

    def info(self):
        print('Ф.И.:{}\n'
              'Номер группы:{}\n'
              'Успеваемость:{}\n'
              'Средний балл:{}\n'.format(
            self.full_name, self.group_number, self.performance, self.gpa
        ))

    def create_names(self):
        self.full_name = '{} {}'.format(
            random.choice(['Иван', 'Алексей', 'Виктор', 'Георгий', 'Сергей']),
            random.choice(['Иванов', 'Петров', 'Котов', 'Козлов', 'Амбучбекович'])
        )

    def create_group_number(self):
        self.group_number = random.randint(1, 3)

    def create_performance(self):
        self.performance = [random.randint(1, 5)
                            for i_item in range(5)]

    def determine_GPA(self):
        gpa = 0
        for i_item in self.performance:
            gpa += i_item
        self.gpa = round(gpa / len(self.performance), 2)


students_list = [Student()
                 for i_student in range(10)]

for i_student in students_list:
    i_student.create_names()
    i_student.create_group_number()
    i_student.create_performance()
    i_student.determine_GPA()

sorted_list = sorted(students_list, key=attrgetter('gpa'))

for i_student in sorted_list:
    i_student.info()

