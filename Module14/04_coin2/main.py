def found_coin(x, y, r):
    if abs(x) + abs(y) <= r:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))

found_coin(x, y, r)
