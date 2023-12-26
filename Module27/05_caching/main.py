

def caching(func):
    def wrapped_func(*args, **kwargs):
        for i_item in args:
            if i_item in wrapped_func.fibonachi_dict:
                return wrapped_func.fibonachi_dict[i_item]
            else:
                result = func(*args, **kwargs)
                wrapped_func.fibonachi_dict[i_item] = result
                return result

    wrapped_func.fibonachi_dict = {}
    return wrapped_func


@caching
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован


print(fibonacci.fibonachi_dict)