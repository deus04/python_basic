word = str(input('Введите слово: '))
word_list = list(word)
length = len(word)

count = 0
for i in range(int(length / 2)):
    if word_list[i] == word_list[(i + 1) * -1]:
        count += 1

if count == int(length / 2):
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
