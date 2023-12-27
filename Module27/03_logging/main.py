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
            except (ErrorOne, ErrorTwo, ErrorThree) as exc:
            # TODO По условию задачи надо ловить любые ошибки, то есть указать тут логично один класс Exception
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
    result = 123
    error_name = random.choice([ErrorOne('Ошибка №1'), ErrorTwo('Ошибка №2'), ErrorThree('Ошибка №3')])
    # TODO достаточно было сделать тут что-то, что выбрасывает исключение, например деление на ноль
    raise error_name
    return result  # TODO недостижимая строка


with open('function_errors.log', 'w'):
    for _ in range(5):
        test()