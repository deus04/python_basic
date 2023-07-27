def is_prime(num):
    count = 0
    for i in range(2, num + 1):
        if num % i == 0:
            count += 1

    if count == 1:
        return True
    else:
        return False


def crypto(iter):
    prime_list = []
    if isinstance(iter, (str, list, tuple)):
        # для списков и строк
        iter = list(iter)
        for i_index, i_symbol in enumerate(iter):
            if is_prime(i_index):
                prime_list.append(i_symbol)
    elif isinstance(iter, dict):
        for i_index, i_symbol in iter.items():
            if is_prime(i_index):
                prime_list.append(i_symbol)

    return prime_list


iter = (1,2,3,4,5,6) #tuple
# iter = {
#         1: 'Alexander',
#         2: 'Krug',
#         3: 22,
#         4: 'health food'
#         }                  # dict
#iter = 'О Дивный Новый мир!' # str
#iter = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # list
print(crypto(iter))
# не понял как сделать доп пункт