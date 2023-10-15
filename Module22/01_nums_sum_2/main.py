file = open('numbers.txt', 'r')
summ = 0
for i_line in file:
    for i_sym in i_line:
        if (i_sym != ' ') and (i_sym != '\n'):
            summ += int(i_sym)
file.close()

file = open('answer.txt', 'w')
file.write(str(summ))