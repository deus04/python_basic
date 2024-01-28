import random
import datetime


class ErrorOne(Exception):
    pass


class ErrorTwo(Exception):
    pass


class ErrorThree(Exception):
    pass


def logging(func):

    def wrapper(*args, **kwargs):
        print('Название функции: ', func.__name__)
        print(func.__doc__)
        with open('function_errors.log', 'a', encoding='utf-8') as errors_log:
            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                print("Ошибка!")
                date_time = datetime.datetime.now()
                error_message = f'Функция {func.__name__} вернула ошибку: ' \
                                f'{exc.__class__.__name__} - {exc} - {date_time}\n'
                errors_log.write(error_message)
    return wrapper


@logging
def test():
    '''
    Некоторая тестовая функция
    :return: print('text')
    :raise Exseption:
    '''

    print('<Тут чтото происходит...>')
    error_name = random.choice([ErrorOne('Ошибка №1'), ErrorTwo('Ошибка №2'), ErrorThree('Ошибка №3')])
    raise error_name


with open('function_errors.log', 'w'):
    for _ in range(5):
        test()