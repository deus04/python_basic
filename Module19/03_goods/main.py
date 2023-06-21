goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

print(list(goods))

for i_goods in goods:
    print(i_goods, '-', end=' ')
    quantity_sum = 0
    price_sum = 0
    for goods_value in store[goods[i_goods]]:
        quantity_sum += goods_value['quantity']
        price_sum += goods_value['price'] * goods_value['quantity']
    print(quantity_sum, 'штук, стоимость {:,d} рублей'.format(price_sum)) # не помню как разделить на триады через пробел