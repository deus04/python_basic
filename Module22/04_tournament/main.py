from operator import itemgetter


first_tour_file = open('first_tour.txt', 'w')
data_first_tour = '80\n' \
                  'Ivanov Serg 80\n' \
                  'Sergeev Petr 92\n' \
                  'Petrov Vasiliy 98\n' \
                  'Vasiliev Maxim 78\n'
first_tour_file.write(data_first_tour)
first_tour_file.close()
# создали файл

first_tour_file = open('first_tour.txt', 'r')
splited_list = []
for i_elem in first_tour_file:
    splited_list.append(i_elem[:-1])
first_tour_file.close()

threshold = splited_list[0]
splited_list.remove(splited_list[0])

second_splited_list = []
for i_elem in splited_list:
    second_splited_list.append(i_elem.split(' '))
# разбили
for i_elem in second_splited_list:
    if threshold >= i_elem[2]:
        second_splited_list.remove(i_elem)
# отсеяли

second_tour_file = open('second_tour.txt', 'w')
second_tour_file.write(str(len(second_splited_list)) + '\n')

number = 1
for i_elem in sorted(second_splited_list, key=itemgetter(2), reverse=True):
    # sorted(abc_dict.items(), key=itemgetter(1), reverse=True)
    second_tour_file.write('{number}) {name}. {surname} {score} \n'
                           .format(number=str(number), name=i_elem[1][0], surname=i_elem[0], score=i_elem[2]))
    number += 1

