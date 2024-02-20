import re



# В данном случае запрос request.get заменен на загрзку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()
# По итогу вы так же получаете код сайта в виде одной строки
result = re.findall(r'<h3>.*</h3>', text) #TODO возможно можно както более  красиво сразу заголовки достать
h3_list = []
for i_elem in result:
    i_elem = i_elem[4:-5]
    h3_list.append(i_elem)
print(h3_list)
