students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']  # <=== возможно ошибка структуры
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def interests_and_surnames(dict):
    all_interests = []
    len_surnames = 0
    for i_student in dict:
        all_interests += dict.get(i_student, {}).get('interests', [])
        len_surnames += len(dict.get(i_student, {}).get('surname', ''))
    all_interests = set(all_interests)

    return all_interests, len_surnames


pairs = []
for i_student, i_age in students.items():
    pairs.append((i_student, i_age['age']))
    # почему при такой записи
    # pairs = (i_student, i_age['age']) в список элементы попадают поотдельности, а не парами в кортежах?

all_interests, len_surnames = interests_and_surnames(students)
print('Список пар "ID студента — возраст":', pairs)
print('Полный список интересов всех студентов:', all_interests)
print('Общая длина всех фамилий студентов:', len_surnames)
