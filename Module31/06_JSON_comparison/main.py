import json


def found_key(selected_elem, search_key):
    if search_key in selected_elem:
        return selected_elem[search_key]
    else:
        if isinstance(selected_elem, dict):
            for i_value in selected_elem.values():
                if isinstance(i_value, dict) or isinstance(i_value, list):  # TODO меня смущает эта повторяющаяся часть
                    result = found_key(i_value, search_key)                 #  }
                    if result:                                              #  }
                        break                                               #  }
        elif isinstance(selected_elem, list):
            for i_value in selected_elem:
                if isinstance(i_value, dict) or isinstance(i_value, list):  #  }
                    result = found_key(i_value, search_key)                 #  }
                    if result:                                              #  }
                        break                                               #  }
        else:
            result = None

        # нужен условный оператор с двумя ветками - для словарей и списков, в каждом по циклу итерирующему по ним
    return result


with open('json_old.json', 'r', encoding='utf-8') as file:
    file_old = json.load(file)

with open('json_new.json', 'r', encoding='utf-8') as file:
    file_new = json.load(file)

dict_of_difs = dict()

diff_list = ["cost_per_unit", "staff", "datetime"]
for i_elem in diff_list:
    first_dict_diff = found_key(file_old, i_elem)
    second_dict_diff = found_key(file_new, i_elem)
    if first_dict_diff != second_dict_diff:
        dict_of_difs[i_elem] = found_key(file_new, i_elem)

result = dict_of_difs
print(result)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)