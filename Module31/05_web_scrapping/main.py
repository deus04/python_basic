import re


with open('examples.html', 'r') as f:
    text = f.read()
result = re.findall(r'<h3.*?>(.*?)</h3>', text)
# TODO Эта тема называется "скобочные группы", доп. материал:
#  https://habr.com/ru/articles/349860/#Skobochnye_gruppy__i_perechisleniya_
print(result)

