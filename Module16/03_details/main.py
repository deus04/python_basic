shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

search = str(input('Название детали: '))
count = 0
price = 0

for product in shop:
    if product[0] == search:
        count += 1
        price += product[1]

print('Кол-во деталей — ', count)
print('Общая стоимость —', price)
