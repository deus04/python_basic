file = open('zen.txt', 'r')
list_zen = []
for i_line in file:
    list_zen.append(i_line)
list_zen[-1] += '\n'
for i_line in list_zen[::-1]:
    print(i_line, end='')
file.close()
