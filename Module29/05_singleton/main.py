def singleton(cls):
    def wrapper():  # TODO 2) укажите и параметры *args, **kwargs чтобы передать их классу при создании объекта
        if not cls.__init__:  # TODO 3) Этот метод есть у любого класса, проверьте наличие значения у атрибута wrapper
            # TODO 3) тут сначала создайте объект класса, после чего присвойте его же атрибуту wrapper
            return cls()  # TODO это лишняя строка
        return cls   # TODO 4) вернуть надо значение атрибута instance функции-обертки
    # TODO 1) установите начальное значение атрибута instance функции-обертки wrapper, например None - эта строка
    #  выполнится при декорировании, то есть раньше создания объекта декорируемого класса
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()
# TODO 0) Сейчас обеим переменным присваивается сам класс, а не объекты класса

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)