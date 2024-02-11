def singleton(cls):
    def wrapper():
        if not cls.__init__:
            return cls()
        return cls
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)