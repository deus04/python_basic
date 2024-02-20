import requests
import json


def list_or_dict(dict_1, dict_2, diff_list):
    for key in dict_1.keys():
        if isinstance(dict_1[key], dict):
            list_or_dict(dict_1[key], dict_2[key], diff_list)
        elif dict_1[key] != dict_2[key] and key in diff_list:
            dict_of_difs[key] = dict_1[key]
    return dict_of_difs


with open('json_old.json', 'r', encoding='utf-8') as file:
    file_old = json.load(file)

with open('json_new.json', 'r', encoding='utf-8') as file:
    file_new = json.load(file)

dict_of_difs = dict()

diff_list = ["cost_per_unit", "staff", "datetime"]  # TODO указал ключ записи словаря вложенного в список, ваш алгоритм
                                                    #  такие словари просто не "обходит" (не проверяет)
# TODO В модуле 21 мы делали рекурсивный поиск ключа сложной вложенной структуры (задача 2), используйте её для решения
#  данной задачи. Только, чтобы решение было общим (для любых вложенных структур) в неё ещё надо добавить обход
#  вложенных списков.
# TODO Предлагаю такой алгоритм программы (псевдокодом):
# 1. читаем оба файла со словарями, преобразуем в словари и присваиваем двум переменным "старый_словарь" и "новый_словарь"
# 2. итерируя по списку ключей выполняем:
#     - находим значение по текущему ключу в старом словаре
#     - находим значение по текущему ключу в новом словаре
#     - если значения разные - создаем в словаре "результата" запись из вида "текущий ключ": "значение в новом словаре"
# 3. Записываем в файл словарь
result = list_or_dict(file_old, file_new, diff_list)
print(result)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4)  # TODO только title в итоговом файле чтото поехал(
