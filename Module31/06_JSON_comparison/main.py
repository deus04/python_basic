import requests
import json


def list_or_dict(dict_1, dict_2, diff_list):
    for key in dict_1.keys():
        if isinstance(dict_1[key], dict):
            list_or_dict(dict_1[key], dict_2[key], diff_list)
        elif dict_1[key] != dict_2[key] and key in diff_list:
            dict_of_difs[key] = dict_1[key]
    return dict_of_difs


def found_key(selected_elem, search_key):
    if search_key in selected_elem:
        print('поиск..', selected_elem[search_key])
        return selected_elem[search_key]
    else:
        if isinstance(selected_elem, list):
            print('!!!!!!!!!!!!!!') #TODO почемуто не заходит сюда
                                    # TODO потому что сейчас found_key всегда получает словарь, список может быть только
                                    #  вложенным...
            for i_elem in selected_elem:
                result = found_key(i_elem, search_key)
                if result:
                    break
        else:
            for i_value in selected_elem.values():
                # TODO ...вот тут могут быть списки
                if isinstance(i_value, dict):
                    result = found_key(i_value, search_key)
                    if result:
                        break
            else:
                result = None
    return result


with open('json_old.json', 'r', encoding='utf-8') as file:
    file_old = json.load(file)

with open('json_new.json', 'r', encoding='utf-8') as file:
    file_new = json.load(file)

dict_of_difs = dict()

diff_list = ["services", "staff", "datetime"]  #  указал ключ записи словаря вложенного в список, ваш алгоритм
                                                    #  такие словари просто не "обходит" (не проверяет)
#  В модуле 21 мы делали рекурсивный поиск ключа сложной вложенной структуры (задача 2), используйте её для решения
#  данной задачи. Только, чтобы решение было общим (для любых вложенных структур) в неё ещё надо добавить обход
#  вложенных списков.
#  Предлагаю такой алгоритм программы (псевдокодом):
# 1. читаем оба файла со словарями, преобразуем в словари и присваиваем двум переменным "старый_словарь" и "новый_словарь"
# 2. итерируя по списку ключей выполняем:
#     - находим значение по текущему ключу в старом словаре
#     - находим значение по текущему ключу в новом словаре
#     - если значения разные - создаем в словаре "результата" запись из вида "текущий ключ": "значение в новом словаре"
# 3. Записываем в файл словарь
for i_elem in diff_list:
    first_dict_diff = found_key(file_old, i_elem)
    print(i_elem, 'в первом ', first_dict_diff)
    second_dict_diff = found_key(file_new, i_elem)
    print(i_elem, 'во втором', second_dict_diff)
    if first_dict_diff != second_dict_diff:
        dict_of_difs[i_elem] = found_key(file_new,i_elem)
    print('-'*20)

result = dict_of_difs
print(result)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4)  #  только title в итоговом файле чтото поехал(
    # TODO укажите параметр ensure_ascii=False чтобы json мог содержать не только с латинские буквы


#{'services': [{'id': 22222225, 'title': 'Ð¡ÑÑÐ¸Ð¶ÐºÐ°', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], 'datetime': '2022-01-25T13:00:00+03:00'}