import datetime
import functools
import time



#
#
# def log_methods(decorator):
#     @functools.wraps(decorator)
#     def decorate(cls):
#         for i_method_name in dir(cls):
#             if i_method_name.startswith('__') is False:
#                 cur_method = getattr(cls, i_method_name)
#                 decorated_method = decorator(cur_method)
#                 setattr(cls, i_method_name, decorated_method)
#             return cls
#         return decorate
#
#
# def create_time(cls):
#     @functools.wraps(cls)
#     def wrapper(*args, **kwargs):
#         instance = cls(*args, **kwargs)
#         print("Время создания:", datetime.datetime.utcnow())
#         return instance
#     return wrapper
#
#
def timer(func):  # TODO  добавьте ещё два параметра - для шаблона даты-времени и для класса (см. ниже комментарий тоже)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now().strformat()  # TODO для получения "форматированной" даты-времени,
                                                          #  используйте метод strftime и укажите ему строку-формат даты-времени
        print("-Запускается '{}'. Дата и время запуска: {}".format(func.__name__, start_time))
        # в print нужно както достать имя класса cls.__name__ чтобы был верный вывод
        # cls у меня есть только в декораторе класса decorate(cls)
        # но если замерять время там, то он показывает именно время инициации и вывод тогда неверный
        # в общем, не понимаю структуру декораторов. Первые 2 задания сделал легко, а вот тут не могу понять
        # кто во что входит и как обернуть правильно
        # TODO подсказал выше и ниже
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now() - start_time
        formated_time = end_time
        print("-Завершение '{}'. Время работы: {}".format(func.__name__, end_time))
        return result
    return wrapper #Нужно перенести таймер из декоратора класса вот сюда


def for_all_methods(decorator):  # TODO тут через параметр принимаем строку с форматом даты-времени (см. ниже комментарий)
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method in dir(cls):
            if not i_method.startswith('__'):
                # start_time = datetime.now()
                # print("-Запускается '{}.{}'. Дата и время запуска: {}".format(cls.__name__, i_method, start_time))
                cur_method = getattr(cls, i_method)
                decorated_method = decorator(cur_method)  # TODO 1) вызываем напрямую timer вместо decorator
                                                          #  2) добавьте ещё два параметра - для шаблона даты-времени и
                                                          #  для класса (или имени класса) - понадобится при выводе в консоль сообщений
                setattr(cls, i_method, decorated_method)
                # end_time = start_time - datetime.now()
                # print("-Завершение '{}.{}'. Время работы: {}".format(cls.__name__, i_method, end_time))
        return cls
    return decorate


@for_all_methods(timer)  # TODO в качестве параметра передаём формат даты-времени (см. шаблон решения в задании)
class A:
    def test_sum_1(self):
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@for_all_methods(timer)  # TODO Аналогично предыдущему
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

# TODO