from operator import itemgetter

file_text = open('text.txt', 'w')
data = 'Mama myla ramu.'
file_text.write(data)
file_text.close()

file_text = open('text.txt', 'r')
text = file_text.read().lower()
abc_dict = {}
for i_sym in sorted(text):
    if i_sym.isalpha():
        if i_sym in abc_dict:
            abc_dict[i_sym] = int(abc_dict[i_sym]) + 1
        else:
            abc_dict[i_sym] = 1

summ = 0
for i_score in abc_dict.values():
    summ += i_score

analysis_file = open('analysis.txt', 'w')
for i_letter, i_score in sorted(abc_dict.items(), key=itemgetter(1), reverse=True):
    analysis_file.write('{letter} {score}\n'
                        .format(letter=i_letter, score=str(round(i_score / summ, 3))))


