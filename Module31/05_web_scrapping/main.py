import re



# В данном случае запрос request.get заменен на загрзку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()
# По итогу вы так же получаете код сайта в виде одной строки
result = re.findall(r'<h3.*?>(.*?)</h3>', text) #возможно можно както более  красиво сразу заголовки достать
# используйте группы (круглые скобки): re.findall(r'<h3.*?>(.*?)</h3>', text)
#  как здесь работает (.*?) ?
# TODO Эта тема называется "скобочные группы", доп. материал:
#  https://habr.com/ru/articles/349860/#Skobochnye_gruppy__i_perechisleniya_
print(result)

