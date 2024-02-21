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
        return selected_elem[search_key]
    else:
        for i_value in selected_elem.values():  # TODO так можно итерировать только по словарям, для списков нужен отдельный цикл for i_value in selected_elem:
            if isinstance(i_value, dict) or isinstance(i_value, list):
                result = found_key(i_value, search_key)
                if result:
                    break
        else:
            result = None
        # TODO нужен условный оператор с двумя ветками - для словарей и списков, в каждом по циклу итерирующему по ним
    return result


with open('json_old.json', 'r', encoding='utf-8') as file:
    file_old = json.load(file)

with open('json_new.json', 'r', encoding='utf-8') as file:
    file_new = json.load(file)

dict_of_difs = dict()

diff_list = ["cost_per_unit", "staff", "datetime"]  # TODO заменил один ключ на ключ из словаря вложенного в список
for i_elem in diff_list:
    first_dict_diff = found_key(file_old, i_elem)
    second_dict_diff = found_key(file_new, i_elem)
    if first_dict_diff != second_dict_diff:
        dict_of_difs[i_elem] = found_key(file_new, i_elem)

result = dict_of_difs
print(result)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)