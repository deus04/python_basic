import re


my_list = ['9999999999', '999999-999', '99999x9999']
k = 0

for i_num in my_list:
    k += 1
    print(k, '-й номер:', end=' ', sep='')
    if re.match(r'[8-9]{1}\d{9}', i_num) and len(i_num) == 10:
        print('все в порядке')
    else:
        print('не подходит')