start_list = [5, 8, 9, 4, 2, 9, 1, 8]


def hoare_sort(start_list):
    result_1, result_2, result_3 = [], [], []

    support_element = start_list[-1]
    lower_elts = [elem for elem in start_list if elem < support_element]
    equal_elts = [elem for elem in start_list if elem == support_element]
    bigger_elts = [elem for elem in start_list if elem > support_element]

    if lower_elts:
        result_1 = hoare_sort(lower_elts)

    result_2 = equal_elts

    if bigger_elts:
        result_3 = hoare_sort(bigger_elts)

    return result_1 + result_2 + result_3


print(hoare_sort(start_list))
