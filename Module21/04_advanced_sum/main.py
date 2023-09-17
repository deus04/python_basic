
def summator(some_object, *args):
    result = 0
    if isinstance(some_object, list):
        for inner_object in some_object:
            if isinstance(inner_object, list):
                result += summator(inner_object)
            else:
                result += inner_object
    else:
        for inner_object in some_object:
            result += inner_object
    return result


some_object = [[1, 2, [3]], [1], 3]
print(summator(some_object))
some_object = (1, 2, 3, 4, 5)
print(summator(some_object))

