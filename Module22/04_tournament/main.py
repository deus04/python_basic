from operator import itemgetter

def sort(list):
    flag = 0
    for i_elem in list:
        for j_elem in list:
            print(i_elem[2],'<',j_elem[2],'?')
            if i_elem[2] < j_elem[2]:
                i_elem, j_elem = j_elem, i_elem
                flag = 1
                print('сортируем ------ ', list)
    if flag:
        sort(list)
    else:
        return list

first_tour_file = open('first_tour.txt', 'w')
data_first_tour = '80\n'\
                  'Ivanov Serg 80\n'\
                  'Sergeev Petr 92\n'\
                  'Petrov Vasiliy 98\n'\
                  'Vasiliev Maxim 78\n'
first_tour_file.write(data_first_tour)
first_tour_file.close()
# создали файл

first_tour_file = open('first_tour.txt', 'r')
splited_list =[]
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
# TODO не пойму почему не работает сортировка. Не переписывает эл-ты в списке
# TODO короч сделал через itemgetter ¯\_(ツ)_/¯
# print(second_splited_list)
# second_splited_list = sort(second_splited_list)
# print()
# print(second_splited_list)

second_tour_file = open('second_tour.txt', 'w')
second_tour_file.write(str(len(second_splited_list)) + '\n')

number = 1
for i_elem in sorted(second_splited_list, key=itemgetter(2), reverse=True):
    #sorted(abc_dict.items(), key=itemgetter(1), reverse=True)
    second_tour_file.write('{number}) {name}. {surname} {score} \n'
                           .format(number=str(number), name=i_elem[1][0], surname=i_elem[0], score=i_elem[2]))
    number += 1
print(second_splited_list)



