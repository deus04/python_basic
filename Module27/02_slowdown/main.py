import time


def my_decorator(func):
    def wrapped_func(*args, **kwargs):
        print('Ожидаем 5 секунд')
        time.sleep(5)
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@my_decorator
def test():
    print('<Тут чтото происходит...>')


test()