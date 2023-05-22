first_grade = []
second_grade = []

for i in range(160, 178, 2):
    first_grade.append(i)

for i in range(162, 183, 3):
    second_grade.append(i)

first_grade.extend(second_grade)

for i_min in range(len(first_grade)):
    for point in range(i_min, len(first_grade)):
        if first_grade[i_min] > first_grade[point]:
            first_grade[point], first_grade[i_min] = first_grade[i_min], first_grade[point]

print('Отсортированный список учеников:', first_grade)
