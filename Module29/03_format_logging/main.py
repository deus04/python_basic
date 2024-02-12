import time
import datetime
import functools


def timer(cls, func, date_format):
    def wrapper(*args, **kwargs):
        format = date_format
        for sym in format:
            if sym.isalpha():
                format = format.replace(sym, '%' + sym)

        start_time = time.time()
        print("-Запускается '{}.{}' Дата и время запуска: {}".format(cls.__name__, func.__name__,
                                                                     datetime.datetime.now().strftime(format)))
        result = func(*args, **kwargs)
        end_time = round(time.time() - start_time, 3)
        print("-Завершение '{}.{}' Время работы: {}s".format(cls.__name__, func.__name__, end_time))
        return result
    return wrapper


def log_methods(date_format):
    @functools.wraps(date_format)
    def decorate(cls):
        for i_method in dir(cls):
            if not i_method.startswith('__'):
                cur_method = getattr(cls, i_method)
                decorated_method = timer(cls, cur_method, date_format)
                setattr(cls, i_method, decorated_method)
        return cls
    return decorate


@log_methods("m d Y - H:M:S")
class A:
    def test_sum_1(self):
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


@log_methods("m d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
