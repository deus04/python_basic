import zipfile
from operator import itemgetter

# file_zip = zipfile.ZipFile('voyna-i-mir.zip', 'r')
# file_data = file_zip.read('voyna-i-mir.txt')
# TODO так и не понял как брать файл из архива.
#  В результате выдает кучку чисел, возможно дело в кодировке


file = open('voyna-i-mir.txt', 'r', encoding='utf-8')
file_data = file.read()
abc_dict = {}
for i_sym in file_data:
    if i_sym in abc_dict:
        abc_dict[i_sym] = int(abc_dict[i_sym]) + 1
    else:
        abc_dict[i_sym] = 1

analysis_file = open('analysis.txt', 'w')
for i_letter, i_score in sorted(abc_dict.items(), key=itemgetter(1), reverse=True):
    analysis_file.write('{letter} {score}\n'
                        .format(letter=i_letter, score=str(i_score)))