def singleton(cls):
    def wrapper(*args, **kwargs):  # 2) укажите и параметры *args, **kwargs чтобы передать их классу при создании объекта
        if wrapper.instance:
            wrapper.instance = cls()#  3) Этот метод есть у любого класса, проверьте наличие значения у атрибута wrapper
            # 3) тут сначала создайте объект класса, после чего присвойте его же атрибуту wrapper
            return wrapper.instance # 4) вернуть надо значение атрибута instance функции-обертки
    wrapper.instance = None# 1) установите начальное значение атрибута instance функции-обертки wrapper, например None - эта строка
    #  выполнится при декорировании, то есть раньше создания объекта декорируемого класса
    return wrapper
#TODO Возможно я все еще не понел ¯\_(ツ)_/¯

@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()
# TODO 0) Сейчас обеим переменным присваивается сам класс, а не объекты класса

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)