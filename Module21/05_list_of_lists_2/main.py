nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def unpacker(nice_list, very_nice_list):
    if not isinstance(nice_list, int):
        for i_element in nice_list:
            if isinstance(i_element, list):
                for inner_element in i_element:
                    unpacker(inner_element, very_nice_list)
            else:
                very_nice_list.append(i_element)
    else:
        very_nice_list.append(nice_list)

    return very_nice_list


very_nice_list = []
print('Ответ:', unpacker(nice_list, very_nice_list))
