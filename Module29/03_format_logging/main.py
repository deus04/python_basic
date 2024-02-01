from datetime import datetime
import functools


def log_methods(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        print('- Запускается {}. Дата и время запуска: {}'.format(cls.__name__, datetime.utcnow()))
        result = cls(*args, **kwargs)
        return result
    return wrapper


@log_methods
class A:
    def test_sum_1(self):
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods
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

#TODO почемуто выдает ошибку TypeError: function() argument 'code' must be code, not str