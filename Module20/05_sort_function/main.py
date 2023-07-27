def tpl_sort(tpl):
    for i_elem in tpl:
        if not isinstance(i_elem, int):
            return tpl
    return tuple(sorted(tpl))


tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))
