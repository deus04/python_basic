import math

def get_sage_sqrt(number):
    try:
        return round(math.sqrt(number), 2)
    except ValueError:
        #print('Нельзя извлекать квадратный корень из отрицательного числа.')
        return 'Невозможно вычислить'
    except TypeError:
        #print('Введенный элемент не является числом')
        return 'Невозможно вычислить'


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")

# Возможно не понял задачу