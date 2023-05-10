
import math
def found_coin(x, y, r):
    if math.sqrt(x ** 2 + y ** 2) <= r:
        return True
    else:
        return False


print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))

if found_coin(x, y, r):
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')
