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

diff_list = ["services", "staff", "datetime"]
result = list_or_dict(file_old, file_new, diff_list)
print(result)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4) # TODO только title в итоговом файле чтото поехал(