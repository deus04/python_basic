total_orders = int(input('Введите количество заказов: '))
order_dict = {}

for i_order in range(total_orders):
    print(i_order + 1, '-й заказ: ', end='')
    order_list = input().split()
    if not order_dict.get(order_list[0], {}):
        order_dict[order_list[0]] = {order_list[1]: order_list[2]}
    else:
        if not order_dict.get(order_list[0], {}).get(order_list[1]):
            order_dict[order_list[0]][order_list[1]] = order_list[2]
        else:
            order_dict[order_list[0]][order_list[1]] = int(order_list[2]) + int(
                order_dict[order_list[0]][order_list[1]])

for i_key in order_dict.keys():
    print(i_key, ':', sep='')
    for j_key in order_dict[i_key]:
        print('	', j_key, ': ', end='', sep='')
        print(order_dict[i_key][j_key])
